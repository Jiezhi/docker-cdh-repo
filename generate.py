#! /usr/bin/env python3
import sys
import os
import shutil
import time
from string import Template
from os.path import join

# type_lst = ['cm', 'cdh']
os_lst = ['redhat7']
# os_lst = ['redhat7', 'redhat6', 'sles12', 'ubuntu1604', 'ubuntu1804', 'sles12', 'generic']

def generate(templatefile, dockerfile_dir, version, ops):
    if not os.path.exists(dockerfile_dir):
        os.makedirs(dockerfile_dir)
    file_path = join(dockerfile_dir,  'Dockerfile')
    v = version.split('.')[0]
    with open(templatefile, 'r')as f, open(file_path, 'w') as wf:
        content = f.read()
        template = Template(content)
        wf.write(template.substitute(v=v, version=version, os=ops))


def make_file(version):
    for ops in os_lst:
        # if os.path.exists(ops):
            # shutil.rmtree(ops)
            # time.sleep(3)
        generate('Dockerfile.template', ops, version, ops)
        generate('Dockerfile-CDH.template', join(ops, 'cdh'), version, ops)
        generate('Dockerfile-CM.template', join(ops, 'cm'), version, ops)
        generate('Dockerfile-Parcel.template', 'parcel', version, ops)

if __name__ == '__main__':
    version = sys.argv[1]
    make_file(version)