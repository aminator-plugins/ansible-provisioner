#!/usr/bin/env python
# Copyright 2013 Answers for AWS LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup, find_packages
setup(
    name = "aminatorplugins_ansible",
    version = "0.3",
    packages = find_packages(),
    namespace_packages = ( 'aminatorplugins', 'aminatorplugins.provisioner'),

    data_files = [
        ('/etc/aminator/plugins', ['default_conf/aminatorplugins.provisioner.ansible.yml']),
    ],

    entry_points = {
       'aminator.plugins.provisioner': [
           'ansible = aminatorplugins.provisioner.ansible:AnsibleProvisionerPlugin',
       ],
    },

    # metadata for upload to PyPI
    author = "Peter Sankauskas",
    author_email='info@answersforaws.com',
    url='https://github.com/aminator-plugins/ansible',
    description = "Ansible provisioner for Netflix's Aminator",
    long_description=open('README.rst').read(),
    license=open("LICENSE.txt").read(),
    keywords = "aminator plugin ansible",
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
    )
)
