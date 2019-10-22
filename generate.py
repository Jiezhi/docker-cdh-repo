#! /usr/bin/env python3
import sys
import os
import shutil
import time
from string import Template
from os.path import join

type_lst = ['cm', 'cdh']
os_lst = ['redhat7']

def generate(type, version, ops):
    file_dir = join(ops, type)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file_path = join(file_dir,  'Dockerfile')
    v = version.split('.')[0]
    with open('Dockerfile.template', 'r')as f, open(file_path, 'w') as wf:
        content = f.read()
        template = Template(content)
        wf.write(template.substitute(type=type, version=version, os=ops))


def make_file(version):
    for ops in os_lst:
        if os.path.exists(ops):
            shutil.rmtree(ops)
            time.sleep(5)
        for type in type_lst:
            generate(type, version, ops)

if __name__ == '__main__':
    version = sys.argv[1]
    make_file(version)