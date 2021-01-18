#!/bin/bash

# Main script task: Reduce light intensity for povray files from LigandScout and execute povray.
# Loop over all given povray files and changes the light intensity in the .pov file from 06 to 0.3.
# Then povray is executed without screen output (same as -D option!)
# author: @dmachalz

# Print a usage statement
echo 'Usage: bash povray4ligsct.sh <povfile1.pov> <povfile2.pov> <povfile3.pov>'

# Looping over all provided povray files
for pov_file in $@; do
	# Check whether the light intensity is acutally to high
	if [ $(grep "0.6,0.6,0.6" $pov_file | wc -l) == "2" ]; then
    # Change light intensity inplace (directly in the file)
		sed -i '0,/<300.0,-100.0,100.0>, rgb <0.6,0.6,0.6>/s//<300.0,-100.0,100.0>, rgb <0.3,0.3,0.3>/' $pov_file
    # Execute povray. Assume that the required ini file has the same filename. When written out with LigandScout this is always the case.
		povray $pov_file ${pov_file}.ini -D
	else
    # Execute povray. Assume that the required ini file has the same filename. When written out with LigandScout this is always the case.
		povray $pov_file ${pov_file}.ini -D
	fi
done
