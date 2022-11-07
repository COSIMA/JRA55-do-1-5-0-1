# JRA55-do v1.5.0.1

JRA55-do v1.5.0.1 is an atmospheric dataset designed for forcing ocean and sea ice models, downloaded from https://climate.mri-jma.go.jp/pub/ocean/JRA55-do/

NCI already hosts JRA55-do v1.5.0 at `/g/data/qv56/replicas/input4MIPs/CMIP6/OMIP/MRI/MRI-JRA55-do-1-5-0` but that dataset finishes at 15 Jul 2020.
JRA55-do v1.5.0.1 extends this to the present as a near-real-time dataset, updated daily, running from 1 Jan 2020 to 4 days behind the present day.
Data for the past 30 days are preliminary, and replaced day-by-day by final, higher-quality data.

To update, do
```
qsub update.sh
```

Andrew Kiss (andrew.kiss@anu.edu.au)
5 April 2022
