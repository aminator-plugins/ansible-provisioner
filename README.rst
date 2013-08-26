Ansible Provisioner for NetflixOSS Aminator
===========================================

Warning: Refactoring of Aminator is going on right now, so this will work
eventually, but probably doesn't just yet.

This Aminator plugin allows you to provision an AMI using an 
`Ansible <https://github.com/ansible/ansible/>`__ playbook. 


Examples
--------

Some example Ansible playbooks can be found in the
`NetflixOSS-Ansible playbooks <https://github.com/Answers4AWS/netflixoss-ansible>`__ 
repository.  

::

    $ sudo aminate -e ec2_ansible_linux -B ami-6637760f asgard-ubuntu.yml



Installation
------------

TODO: Probably something like:

::

    aminate --install ansible


The Easy Way
------------

There has been some work to make this even easier. For more information, please
read: http://answersforaws.com/blog/2013/08/ansible-provisioner-for-aminator/


About Answers for AWS
---------------------

This code was written by `Peter
Sankauskas <https://twitter.com/pas256>`__, founder of `Answers for
AWS <http://answersforaws.com/>`__ - a consulting company focused on
helping business get the most out of AWS. If you are looking for help
with AWS, please `contact us <http://answersforaws.com/contact/>`__.


LICENSE
-------

Copyright 2013 Answers for AWS LLC

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable
law or agreed to in writing, software distributed under the License is
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.
