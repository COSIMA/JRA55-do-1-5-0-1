#!/bin/bash
#PBS -P x77
#PBS -q copyq
#PBS -l ncpus=1,walltime=10:00:00,jobfs=100GB,storage=gdata/hh5+gdata/ik11
#PBS -l wd

module purge
module use /g/data/hh5/public/modules
module load conda/analysis3

time ./update.py
