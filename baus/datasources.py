import numpy as np
import pandas as pd
import geopandas as gp
import os
from urbansim_defaults import datasources
from urbansim_defaults import utils
from urbansim.utils import misc
import orca
import preprocessing
from utils import (geom_id_to_parcel_id, parcel_id_to_geom_id, nearest_neighbor, 
                   SimulationSummaryData)


#####################
# TABLES AND INJECTABLES
#####################

DATA_DIR = "myData"

@orca.injectable('year')
def year():
    try:
        if orca.get_injectable("iter_var") is not None:
            return orca.get_injectable("iter_var")
    except:
        pass
    # if we're not running simulation, return base year
    return 2014


@orca.injectable()
def initial_year():
    return 2010


@orca.injectable()
def final_year():
    return 2040


@orca.injectable(cache=True)
def store(settings):
    return pd.HDFStore(os.path.join(DATA_DIR, settings["store"]))


@orca.injectable(cache=True)
def limits_settings(settings, scenario):
    # for limits, we inherit from the default
    # limits set the max number of job spaces or res units that may be
    # built per juris for each scenario - usually these represent actual
    # policies in place in each city which limit development

    d = settings['development_limits']

    if scenario in d.keys():
        print "Using limits for scenario: %s" % scenario
        assert "default" in d

        d_scen = d[scenario]
        d = d["default"]
        for key, value in d_scen.iteritems():
            d.setdefault(key, {})
            d[key].update(value)

        return d

    print "Using default limits"
    return d["default"]


@orca.injectable(cache=True)
def inclusionary_housing_settings(settings, scenario):
    # for inclustionary housing, each scenario is different
    # there is no inheritance

    s = settings['inclusionary_housing_settings']

    if scenario in s.keys():
        print "Using inclusionary settings for scenario: %s" % scenario
        s = s[scenario]

    elif "default" in s.keys():
        print "Using default inclusionary settings"
        s = s["default"]

    d = {}
    for item in s:
        # this is a list of cities with an inclusionary rate that is the
        # same for all the cities in the list
        print "Setting inclusionary rates for %d cities to %.2f" %\
            (len(item["values"]), item["amount"])
        # this is a list of inclusionary rates and the cities they apply
        # to - need tro turn it in a map of city names to rates
        for juris in item["values"]:
            d[juris] = item["amount"]

    return d


@orca.injectable(cache=True)
def building_sqft_per_job(settings):
    return settings['building_sqft_per_job']


# Overwrite urbansim default's summary
@orca.injectable("summary", cache=True)
def simulation_summary_data(run_number):
    return SimulationSummaryData(run_number)


@orca.step()
def fetch_from_s3(settings):
#    import boto
    # fetch files from s3 based on config in settings.yaml
    s3_settings = settings["s3_settings"]

#    conn = boto.connect_s3()
#    bucket = conn.get_bucket(s3_settings["bucket"], validate=False)

    for file in s3_settings["files"]:
        file = os.path.join(DATA_DIR, file)
#        if os.path.exists(file):
#            continue
#        print "Downloading " + file
#        key = bucket.get_key(file, validate=False)
#        key.get_contents_to_filename(file)


# key locations in the Bay Area for use as attractions in the models
@orca.table(cache=True)
def landmarks():
    return pd.read_csv(os.path.join(DATA_DIR, 'landmarks.csv'),
                       index_col="name")


@orca.table(cache=True)
def baseyear_taz_controls():
    return pd.read_csv(os.path.join(DATA_DIR,
                       "baseyear_taz_controls.csv"), index_col="taz1454")


@orca.table(cache=True)
def base_year_summary_taz():
    return pd.read_csv(os.path.join('output',
                       'baseyear_taz_summaries_2010.csv'),
                       index_col="zone_id")


# non-residential rent data
@orca.table(cache=True)
def costar(parcels):
    df = pd.read_csv(os.path.join(misc.data_dir(), '2015_08_29_costar.csv'))

    df["PropertyType"] = df.PropertyType.replace("General Retail", "Retail")
    df = df[df.PropertyType.isin(["Office", "Retail", "Industrial"])]

    df["costar_rent"] = df["Average Weighted Rent"].astype('float')
    df["year_built"] = df["Year Built"].fillna(1980)

    df = df.dropna(subset=["costar_rent", "Latitude", "Longitude"])

    # now assign parcel id
    df["parcel_id"] = nearest_neighbor(
        parcels.to_frame(['x', 'y']).dropna(subset=['x', 'y']),
        df[['Longitude', 'Latitude']]
    )

    return df


@orca.table(cache=True)
def zoning_lookup():
    return pd.read_csv(os.path.join(DATA_DIR, "zoning_lookup.csv"),
                       index_col='id')


# zoning for use in the "baseline" scenario
@orca.table(cache=True)
def zoning_baseline(parcels, zoning_lookup, settings):
    df = pd.read_csv(os.path.join(DATA_DIR,
                     "2015_12_21_zoning_parcels.csv"),
                     index_col="geom_id")
    df = pd.merge(df, zoning_lookup.to_frame(),
                  left_on="zoning_id", right_index=True)
    df = geom_id_to_parcel_id(df, parcels)

    return df


@orca.table(cache=True)
def new_tpp_id():
    return pd.read_csv(os.path.join(DATA_DIR, "tpp_id_2016.zip"),
                       index_col="parcel_id")


@orca.table(cache=True)
def zoning_scenario(parcels_geography, scenario, settings):
    scenario_zoning = pd.read_csv(
        os.path.join(DATA_DIR, 'zoning_mods_%s.csv' % scenario))

    for k in settings["building_type_map"].keys():
        scenario_zoning[k] = np.nan

    def add_drop_helper(col, val):
        for ind, item in scenario_zoning[col].iteritems():
            if not isinstance(item, str):
                continue
            for btype in item.split():
                scenario_zoning.loc[ind, btype] = val

    add_drop_helper("add_bldg", 1)
    add_drop_helper("drop_bldg", 0)

    return pd.merge(parcels_geography.to_frame().reset_index(),
                    scenario_zoning,
                    on=['zoningmodcat'],
                    how='left').set_index('parcel_id')


#@orca.table(cache=True)
#def parcels(store):
#    return store['parcels']

@orca.table(cache=True)
def parcels():
    df = gp.GeoDataFrame.from_file(os.path.join(DATA_DIR,
                                            '09_01_2015_parcel_berkeley.shp'))
    df.set_index('PARCEL_ID', drop=False, inplace=True)
    return df


@orca.table(cache=True)
def parcels_zoning_calculations(parcels):
    return pd.DataFrame(index=parcels.index)


@orca.table()
def taz(zones):
    return zones


@orca.table(cache=True)
def parcel_rejections():
    url = "https://forecast-feedback.firebaseio.com/parcelResults.json"
    return pd.read_json(url, orient="index").set_index("geomId")


@orca.table(cache=True)
def parcels_geography(parcels):
    df = pd.read_csv(
        os.path.join(DATA_DIR, "02_01_2016_parcels_geography.csv"),
        index_col="geom_id")
    df = geom_id_to_parcel_id(df, parcels)
    
    # this will be used to map juris id to name
    juris_name = pd.read_csv(
        os.path.join(DATA_DIR, "census_id_to_name.csv"),
        index_col="census_id").name10

    df["juris_name"] = df.jurisdiction_id.map(juris_name)

    df.loc[2054504, "juris_name"] = "Marin County"
    df.loc[2054505, "juris_name"] = "Santa Clara County"
    df.loc[2054506, "juris_name"] = "Marin County"
    df.loc[572927, "juris_name"] = "Contra Costa County"
    # Added to make proportional_elcm step of simulations work
    df.loc[124131, "juris_name"] = "Berkeley"
    # assert no empty juris values
    assert True not in df.juris_name.isnull().value_counts()

    df["pda_id"] = df.pda_id.str.lower()

    # danville wasn't supposed to be a pda
    df["pda_id"] = df.pda_id.replace("dan1", np.nan)

    return df


@orca.table(cache=True)
def manual_edits():
    return pd.read_csv(os.path.join(DATA_DIR, "manual_edits.csv"))


def reprocess_dev_projects(df):
    # if dev projects with the same parcel id have more than one build
    # record, we change the later ones to add records - we don't want to
    # constantly be redeveloping projects, but it's a common error for users
    # to make in their development project configuration
    df = df.sort_values(["geom_id", "year_built"])
    prev_geom_id = None
    for index, rec in df.iterrows():
        if rec.geom_id == prev_geom_id:
            df.loc[index, "action"] = "add"
        prev_geom_id = rec.geom_id

    return df


# shared between demolish and build tables below
def get_dev_projects_table(scenario, parcels):
    df = pd.read_csv(os.path.join(DATA_DIR, "development_projects.csv"))
    df = reprocess_dev_projects(df)

    # this filters project by scenario
    if scenario in df:
        # df[scenario] is 1s and 0s indicating whether to include it
        df = df[df[scenario].astype('bool')]

    df = df.dropna(subset=['geom_id'])

    cnts = df.geom_id.isin(parcels.geom_id).value_counts()
    if False in cnts.index:
        print "%d MISSING GEOMIDS!" % cnts.loc[False]

    df = df[df.geom_id.isin(parcels.geom_id)]

    geom_id = df.geom_id  # save for later
    df = df.set_index("geom_id")
    df = geom_id_to_parcel_id(df, parcels).reset_index()  # use parcel id
    df["geom_id"] = geom_id.values  # add it back again cause it goes away

    return df


@orca.table(cache=True)
def demolish_events(parcels, settings, scenario):
    df = get_dev_projects_table(scenario, parcels)

    # keep demolish and build records
    return df[df.action.isin(["demolish", "build"])]


@orca.table(cache=True)
def development_projects(parcels, settings, scenario):    
    df = get_dev_projects_table(scenario, parcels)

    #take care of columns in buildings
    for col in [
            'res_sqft', 'res_p_sqrt', 'nres_r_ft', 'ACRES']:
        df[col] = 0
    df["redf_year"] = 2012  # default base year
    df["sale_price"] = np.nan  # null sales price
    df["bldg_sqft"] = df.building_sqft.fillna(0)
    df["nres_sqft"] = df.non_residential_sqft.fillna(0)
    df["res_units"] = df.residential_units.fillna(0).astype("int")
    df["PARCEL_ID"] = df.parcel_id
    df["APN"] = df.raw_id
    df["COUNTY_ID"] = df.county.map(settings["reverse_county_id_map"])
    df["DEVELOPMEN"] = df.development_projects_id
    df["GEOM_ID"] = df.geom_id
    df["IMPUTATION"] = "_"
    df["X"] = df.x
    df["Y"] = df.y
    df["ZONE_ID"] = parcels.to_frame(columns=['GEOM_ID', 'ZONE_ID']).loc[parcels['GEOM_ID'] == df['GEOM_ID'].iloc[0], 'ZONE_ID'].iloc[0]
    df["bld_year"] = df.year_built
    df["bldgt_id"] = df.building_type_id
    df["costar_r"] = None
    df["costar_t"] = None
    df["geometry"] = None
    df["impr_value"] = None
    df['sqft_unit'] = None
    df['sale_year'] = df.last_sale_year
    df['price_per_sqft'] = None
    df['lot_size_per_unit'] = None
    df['vacant_residential_units'] = None
    df['juris_ave_income'] = None
    df['vacant_job_spaces'] = None
    df['vacant_res_units'] = None
    df['building_age'] = None
    df['tmnode_id'] = None
    df['building_id'] = None
    df['new_construction'] = None
    df['transit_type'] = None
    df['vmt_res_cat'] = None
    df['historic'] = None
    df['modern_condo'] = None
    df['zone_id'] = None
    df['general_type'] = None
    df['sqft_per_job'] = None
    df['node_id'] = None
    df['is_sanfran'] = None
    df['job_spaces'] = None
    df['unit_price'] = None
    df['bldg_id'] = None
    
    for col in [
            'residential_sqft', 'residential_price', 'non_residential_rent']:
        df[col] = 0
    df["redfin_sale_year"] = 2012  # default base year
    df["redfin_sale_price"] = np.nan  # null sales price
    df["stories"] = df.stories.fillna(1)
    df["building_sqft"] = df.building_sqft.fillna(0)
    df["non_residential_sqft"] = df.non_residential_sqft.fillna(0)
    df["residential_units"] = df.residential_units.fillna(0).astype("int")
    df["deed_restricted_units"] = 0

    df["building_type"] = df.building_type.replace("HP", "OF")
    df["building_type"] = df.building_type.replace("GV", "OF")
    df["building_type"] = df.building_type.replace("SC", "OF")

    building_types = settings["building_type_map"].keys()
    # only deal with building types we recorgnize
    # otherwise hedonics break
    df = df[df.building_type.isin(building_types)]

    # we don't predict prices for schools and hotels right now
    df = df[~df.building_type.isin(["SC", "HO"])]

    # need a year built to get built
    df = df.dropna(subset=["year_built"])
    df = df[df.action.isin(["add", "build"])]

    print "Describe of development projects"
    # this makes sure dev projects has all the same columns as buildings
    # which is the point of this method
    print df[orca.get_table('buildings').local_columns].describe()

    return df


def check_for_preproc(store, preproc_table, filename):
    if preproc_table not in store:
        return gp.GeoDataFrame.from_file(os.path.join(DATA_DIR, filename))
    return store[preproc_table]


@orca.table(cache=True)
def jobs(store):
    return check_for_preproc(store, 'jobs_preproc', 
                             '09_01_2015_job_berkeley.shp')


@orca.table(cache=True)
def households(store):
    return check_for_preproc(store, 'households_preproc',
                             '09_01_2015_households_berkeley.shp')


@orca.table(cache=True)
def buildings(store):
    df = check_for_preproc(store, 'buildings_preproc',
                             '09_01_2015_building_berkeley.shp')
#    if df.index.name == 'APN':
    return df
#    return df.set_index('APN')


@orca.table(cache=True)
def residential_units(store):
    return store['residential_units_preproc']


@orca.table(cache=True)
def household_controls_unstacked():
    return pd.read_csv(os.path.join(DATA_DIR, "household_controls.csv"),
                       index_col='year')


# the following overrides household_controls
# table defined in urbansim_defaults
@orca.table(cache=True)
def household_controls(household_controls_unstacked):
    df = household_controls_unstacked.to_frame()
    # rename to match legacy table
    df.columns = [1, 2, 3, 4]
    # stack and fill in columns
    df = df.stack().reset_index().set_index('year')
    # rename to match legacy table
    df.columns = ['base_income_quartile', 'total_number_of_households']
    return df


@orca.table(cache=True)
def employment_controls_unstacked():
    return pd.read_csv(
        os.path.join(DATA_DIR, "employment_controls.csv"),
        index_col='year')


# the following overrides employment_controls
# table defined in urbansim_defaults
@orca.table(cache=True)
def employment_controls(employment_controls_unstacked):
    df = employment_controls_unstacked.to_frame()
    # rename to match legacy table
    df.columns = [1, 2, 3, 4, 5, 6]
    # stack and fill in columns
    df = df.stack().reset_index().set_index('year')
    # rename to match legacy table
    df.columns = ['empsix_id', 'number_of_jobs']
    return df


@orca.table(cache=True)
def zone_forecast_inputs():
    return pd.read_csv(
        os.path.join(DATA_DIR, "zone_forecast_inputs.csv"),
        index_col="zone_id")


# this is the set of categories by zone of sending and receiving zones
# in terms of vmt fees
@orca.table(cache=True)
def vmt_fee_categories():
    return pd.read_csv(
        os.path.join(DATA_DIR, "vmt_fee_zonecats.csv"),
        index_col="taz")


@orca.table(cache=True)
def superdistricts():
    return pd.read_csv(
        os.path.join(DATA_DIR, "superdistricts.csv"),
        index_col="number")


@orca.table(cache=True)
def abag_targets():
    return pd.read_csv(os.path.join(DATA_DIR, "abag_targets.csv"))


@orca.table(cache=True)
def taz_geography(superdistricts):
    tg = pd.read_csv(
        os.path.join(DATA_DIR, "taz_geography.csv"),
        index_col="zone")

    # we want "subregion" geography on the taz_geography table
    # we have to go get it from the superdistricts table and join
    # using the superdistrcit id
    tg["subregion_id"] = \
        superdistricts.subregion.loc[tg.superdistrict].values
    tg["subregion"] = tg.subregion_id.map({
        1: "Core",
        2: "Urban",
        3: "Suburban",
        4: "Rural"
    })
    return tg


# these are shapes - "zones" in the bay area
@orca.table(cache=True)
def zones():
    # sort index so it prints out nicely when we want it to
    return gp.GeoDataFrame.from_file(os.path.join(DATA_DIR,
                       '09_01_2015_zones_berkeley.shp')).sort_index()


# this specifies the relationships between tables
orca.broadcast('buildings', 'residential_units', cast_index=True,
               onto_on='building_id')
orca.broadcast('residential_units', 'households', cast_index=True,
               onto_on='unit_id')
orca.broadcast('parcels_geography', 'buildings', cast_index=True,
               onto_on='parcel_id')
# not defined in urbansim_Defaults
orca.broadcast('tmnodes', 'buildings', cast_index=True, onto_on='tmnode_id')
orca.broadcast('taz_geography', 'parcels', cast_index=True,
               onto_on='zone_id')
