import os
from baus import models
from baus import ual
import orca
from maps import dframe_explorer

#os.system('python baus.py -c --mode preprocessing')
#
#os.system('python baus.py -c --mode estimation')
#os.system('python baus.py -c --mode feasibility')
os.system('python baus.py -c --mode simulation')

try:
    f = open(os.path.join(os.getenv('DATA_HOME', "."), 'RUNNUM'), 'r')
    run_number = int(f.read())
    f.close()
except:
    run_number = 1
f = open(os.path.join(os.getenv('DATA_HOME', "."), 'RUNNUM'), 'w')
f.write(str(run_number + 1))
f.close()

d = {tbl: orca.get_table(tbl).to_frame() for tbl in 
         ['buildings', 'residential_units', 'households', 'results']}
dframe_explorer.start(d, 
        center=[37.7792, -122.2191],
        zoom=11,
#        shape_json='runs/run{}_simulation_output.json'.format(run_number-1),
        shape_json='runs/run945_simulation_output.json',
#        shape_json='data/zones.json',
        geom_name='ZONE_ID', # from JSON file
        join_name='zone_id', # from data frames
        precision=2)