#!/usr/bin/env python3
from urllib.request import urlretrieve
from urllib.parse import urljoin
import os
from bs4 import BeautifulSoup

sourceurl = 'https://climate.mri-jma.go.jp/pub/ocean/JRA55-do/jra55do_latest.html'

basedir = 'mirror'
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
        else:
            print('downloading', outfn)
            os.makedirs(os.path.dirname(outfn), exist_ok=True)
            if os.path.exists(outfntmp):
                os.remove(outfntmp)
            urlretrieve(urljoin(sourceurl, href), outfntmp)
            os.rename(outfntmp, outfn)
print('done')
