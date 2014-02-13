import pandas as pd, numpy as np, statsmodels.api as sm
from synthicity.urbanchoice import *
from synthicity.utils import misc
import time, copy

SAMPLE_SIZE=100

##############
#  ESTIMATION
##############

def hlcms_estimate(dset,year=None,show=True):

  assert "locationchoicemodel" == "locationchoicemodel" # should match!
  returnobj = {}
  
  # TEMPLATE configure table
  choosers = dset.fetch_batshh(tenure='sales')
  # ENDTEMPLATE
  
    
  # TEMPLATE specifying output names
  output_csv, output_title, coeff_name, output_varname = [u'coeff-reslocation-sales-%s.csv', u'RESIDENTIAL LOCATION CHOICE MODELS (SALES-%s)', u'res_sales_location_%s', u'sales_household_building_ids']
  # ENDTEMPLATE
 
  # TEMPLATE specifying alternatives
  alternatives = dset.fetch('nodes').join(dset.variables.compute_res_building_averages(dset,year,sales=1,rent=0))
  # ENDTEMPLATE
  
  
  t1 = time.time()

    # TEMPLATE creating segments
  segments = choosers.groupby([u'income_quartile'])
  # ENDTEMPLATE
    
  for name, segment in segments:

    name = str(name)
    if name is not None: tmp_outcsv, tmp_outtitle, tmp_coeffname = output_csv%name, output_title%name, coeff_name%name
    else: tmp_outcsv, tmp_outtitle, tmp_coeffname = output_csv, output_title, coeff_name

    # TEMPLATE dependent variable
    depvar = "_node_id"
    # ENDTEMPLATE
    global SAMPLE_SIZE
        
    sample, alternative_sample, est_params = interaction.mnl_interaction_dataset(
                                        segment,alternatives,SAMPLE_SIZE,chosenalts=segment[depvar])

    print "Estimating parameters for segment = %s, size = %d" % (name, len(segment.index)) 

    # TEMPLATE computing vars
    data = pd.DataFrame(index=alternative_sample.index)
    data["ln_price"] = (alternative_sample.sales_price.apply(np.log1p)).astype('float')
    data["sales_price x income"] = ((alternative_sample.sales_price*alternative_sample.HHINCOME).apply(np.log)).astype('float')
    data["accessibility"] = (alternative_sample.nets_all_regional1_30.apply(np.log1p)).astype('float')
    data["reliability"] = (alternative_sample.nets_all_regional2_30.apply(np.log1p)).astype('float')
    data["average_income"] = (alternative_sample.demo_averageincome_average_local.apply(np.log)).astype('float')
    data["income x income"] = ((alternative_sample.demo_averageincome_average_local*alternative_sample.HHINCOME).apply(np.log)).astype('float')
    data["ln_units"] = (alternative_sample.residential_units.apply(np.log1p)).astype('float')
    data = data.fillna(0)
    # ENDTEMPLATE
    if show: print data.describe()

    d = {}
    d['columns'] =  data.columns.tolist()
    data = data.as_matrix()
    fnames = [u'ln_price', u'sales_price x income', u'accessibility', u'reliability', u'average_income', u'income x income', u'ln_units']
    
    fit, results = interaction.estimate(data,est_params,SAMPLE_SIZE)
    
    fnames = interaction.add_fnames(fnames,est_params)
    if show: print misc.resultstotable(fnames,results)
    misc.resultstocsv(fit,fnames,results,tmp_outcsv,tblname=tmp_outtitle)
    
    d['null loglik'] = float(fit[0])
    d['converged loglik'] = float(fit[1])
    d['loglik ratio'] = float(fit[2])
    d['est_results'] = [[float(x) for x in result] for result in results]
    returnobj[name] = d
    
    dset.store_coeff(tmp_coeffname,zip(*results)[0],fnames)

  print "Finished executing in %f seconds" % (time.time()-t1)
  return returnobj

