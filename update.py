#!/usr/bin/env python3
from urllib.request import urlretrieve
from urllib.parse import urljoin
import os
from bs4 import BeautifulSoup

def update(delete_partial=False,
           sourceurl='https://climate.mri-jma.go.jp/pub/ocean/JRA55-do/jra55do_latest.html',
           basedir='mirror'):

    os.makedirs(basedir, exist_ok=True)

    urlretrieve(urljoin(sourceurl, 'index.html'), os.path.join(basedir, 'index.html'))

    sourcefn = os.path.join(basedir, os.path.basename(sourceurl))
    urlretrieve(sourceurl, sourcefn)

    # download all .nc files linked from sourceurl, into the same directory structure
    soup = BeautifulSoup(open(sourcefn), 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.endswith('.nc'):
            outfn = os.path.normpath(os.path.join(basedir, href))
            outfntmp = outfn+'-partial'
            if os.path.exists(outfn):
                print('--- skipping', outfn, '(already exists)')
            elif os.path.exists(outfntmp):
                if delete_partial:
                    print('### DELETING', outfn)
                    os.remove(outfntmp)
                else:
                    print('*** skipping', outfn, '(already downloading)')
            else:
                if not delete_partial:
                    os.makedirs(os.path.dirname(outfn), exist_ok=True)
                    print('downloading', outfn)
                    urlretrieve(urljoin(sourceurl, href), outfntmp)
                    os.rename(outfntmp, outfn)
    print('done')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=
        'Download/update JRA55-do v1.5.0.1 data in directory "./mirror".\
        JRA55-do v1.5.0.1 is an atmospheric dataset designed for forcing ocean and sea ice models, available from https://climate.mri-jma.go.jp/pub/ocean/JRA55-do/.\
        Latest version of this script: https://github.com/COSIMA/JRA55-do-1-5-0-1')
    parser.add_argument('-d', '--delete_partial',
                        action='store_true', default=False,
                        help="delete partially-downloaded files; don't download anything")
    args = parser.parse_args()
    delete_partial = vars(args)['delete_partial']
    update(delete_partial=delete_partial)