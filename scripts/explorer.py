from urbansim.maps import dframe_explorer as de
import orca
import sys

runnum = orca.get_injectable("run_number")

parcel_output = 'runs/run%d_parcel_output.csv' % runnum
zone_output = 'runs/run%d_simulation_output.json' % runnum
outfile = '/var/www/html/sim_explorer%d.html' % runnum

de.start(
    zone_output,
    parcel_output,
    port=8080,
    host='0.0.0.0',
    write_static_file=outfile
)
