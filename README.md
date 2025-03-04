**NOTE:** this is now redundant, as JRA55v1.5.0 and v1.5.0.1 are combined in v1.6.0 available from
`/g/data/qv56/replicas/input4MIPs/CMIP6Plus/OMIP/MRI/MRI-JRA55-do-1-6-0`
see https://github.com/COSIMA/access-om3/issues/205#issuecomment-2597118474

# JRA55-do v1.5.0.1

JRA55-do v1.5.0.1 is an atmospheric dataset designed for forcing ocean and sea ice models, available from https://climate.mri-jma.go.jp/pub/ocean/JRA55-do/

NCI already hosts JRA55-do v1.5.0 at `/g/data/qv56/replicas/input4MIPs/CMIP6/OMIP/MRI/MRI-JRA55-do-1-5-0` but that dataset finishes at 15 Jul 2020.
JRA55-do v1.5.0.1 extends this to the present as a near-real-time dataset, updated daily, running from 1 Jan 2020 to 4 days behind the present day.
Data for the past 30 days are preliminary, and replaced day-by-day by final, higher-quality data. See `check_JRA55do1p5p0p1.ipynb`.

JRA55-do v1.5.0.1 is available at `/g/data/ik11/inputs/JRA-55/JRA55-do-1-5-0-1/mirror-2024-04-11`. This contains only finalised data and extends to the end of January 2024 (which is the end of the JRA55-do dataset).
To see the exact end time of each file, do
```
find mirror-2024-04-11/ -name *2024*.nc -exec sh -c "echo {}; ncdump -t -v time {} | grep 2024 | grep ';' | grep -v ':[a-z]'" ';'
```

_NB: `/g/data/ik11/inputs/JRA-55/JRA55-do-1-5-0-1/mirror` [contained unfinalised data for 2023-12-10T15:00:00 onwards](https://github.com/COSIMA/JRA55-do-1-5-0-1/issues/1),
so has been renamed `mirror-DO-NOT-USE`. Use `mirror-2024-04-11` instead._

To download/update JRA55-do v1.5.0.1 data in directory "./mirror", do
```
qsub update.sh
```
You can do this several times if you want to download in parallel to speed it up.

Partially-downloaded `.nc` files have `-partial` appended. Downloading is skipped for any `.nc` file for which a corresponding `.nc-partial` exists (so that downloads can proceed in parallel). Check for `-partial` files with `find . -name "*.nc-partial"` after all update jobs have completed. If any exist, you'll need to do
```
./update.py -d
```
to delete the partial files, then
```
qsub update.sh
```
to try downloading them again.
