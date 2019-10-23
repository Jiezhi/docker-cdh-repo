#! /usr/bin/env python3
"""
Ref: https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/cm_ig_create_local_package_repo.html
"""
import sys
import os
import shutil
import time
import urllib
from urllib import request
from string import Template
from os.path import join

# COPY_CONF = 'COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf'
#   wget --recursive --no-parent --no-host-directories https://archive.cloudera.com/cdh$v/$version/parcels/ -P $HTTP_DIR; \ 
#   wget --recursive --no-parent --no-host-directories https://archive.cloudera.com/gplextras$v/$version/parcels/ -P $HTTP_DIR; \

WGET_BASE = 'wget -nv --recursive --no-parent --no-host-directories https://archive.cloudera.com/{sub_url} -P $HTTP_DIR'
WGET_CM = ['cm{v}/{version}/{ops}/', 'cm{v}/{version}/allkeys.asc', ]
WGET_CDH = ['cdh{v}/{version}/{ops}/', 'gplextras{v}/{version}/{ops}/']
# WGET_PARCEL = ['cdh$v/$version/parcels/', 'gplextras$v/$version/parcels/']

os_lst = ['redhat7', 'redhat6', 'sles12', 'ubuntu1604', 'ubuntu1804']

def valid_url(url):
    url = 'https://archive.cloudera.com/' + url
    try:
        ret = request.urlopen(url)
        print(url, ' is ok')
    except Exception as e:
        print('error with ', url)
        return False
    return True

def generate(dockerfile_dir, version, ops, wget_lst):
    if not os.path.exists(dockerfile_dir):
        os.makedirs(dockerfile_dir)
    file_path = join(dockerfile_dir,  'Dockerfile')
    v = version.split('.')[0]
    with open('Dockerfile.template', 'r')as f, open(file_path, 'w') as wf:
        content = f.read()
        template = Template(content)
        urls = []
        for sub_url in wget_lst:
            sub_url = sub_url.format(v=v, version=version, ops=ops)
            if valid_url(sub_url):
                url = WGET_BASE.format(sub_url=sub_url)
                urls.append(url)
        wf.write(template.substitute(WGET=' ;\\\n  '.join(urls)))


def make_file(version):
    for ops in os_lst:
        generate(join(ops, 'cdh'), version, ops, WGET_CDH)
        generate(join(ops, 'cm'), version, ops, WGET_CM)
    # not like other os
    generate('parcels', version, 'parcels', WGET_CDH)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception("input version to generate")
    if sys.argv[1] == 'clean':
        os_lst.append('parcels')
        for ops in os_lst:
           if os.path.exists(ops):
                shutil.rmtree(ops)
    else:
        version = sys.argv[1]
        make_file(version)