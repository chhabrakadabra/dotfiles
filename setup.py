#!/usr/bin/env python

import io
import os
import subprocess
import sys
from distutils.command.install import install
from functools import partial
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

ansible_file = partial(os.path.join, here, 'ansible')

class CustomInstall(install):
    def run(self):
        super().run()

        print('Starting ansible...')
        hosts_file = ansible_file('hosts.yaml')
        playbook_file = ansible_file('playbook.yaml')
        cmd = f'ansible-playbook -i {hosts_file} {playbook_file}'
        process = subprocess.Popen(cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   shell=True)
        for line in io.TextIOWrapper(process.stdout):
            sys.stdout.write(line)
        print('Ansible run finished...')


setup(
    name="abhin-dotfiles",
    author="Abhin Chhabra",
    author_email="chhabra.abhin@gmail.com",
    description="My dotfiles as a Python package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chhabrakadabra/dotfiles',
    use_scm_version=True,
    license="BSD",
    python_requires='>=3.7.*',
    packages=[],
    setup_requires=[
        'setuptools_scm',
        'ansible',
    ],
    install_requires=[
        'ansible',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    cmdclass={'install': CustomInstall},
)
