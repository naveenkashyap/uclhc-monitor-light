#!/bin/bash

# go to desired directory
cd $HOME/uclhc-monitor-light

# prepare output file
echo "last run time: " > prev_runtime.txt
date >> prev_runtime.txt
date >> daemon_output.txt

# call daemon script
python daemon.py >> daemon_output.txt

#prepare output file for next run
#echo >> daemon_output.txt
#echo "----------------------------" >> daemon_output.txt
#echo >> daemon_output.txt
#echo >> daemon_output.txt
