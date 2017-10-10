#!/usr/bin/env python3

import argparse
import os
import sys
from subprocess import call

parser = argparse.ArgumentParser(description='Deploy Panda Ansible roles easily', epilog='Example: ./wrapper.py -t 172.28.128.26 -k private_key -u vagrant')

parser.add_argument('-t', '--target', help = 'Target Hostname/s or IP/s',
                    action = "store", dest = "targets",
                    required=True, nargs = '+')
parser.add_argument('-k', '-key', help = 'SSH key',
                    action = "store", dest = "sshKey",
                    required=True)
parser.add_argument('-u', '-user', help = 'SSH user',
                    action = "store", dest = "sshUser",
                    required=True)

args = parser.parse_args()

inventoryFile = 'inventory'
playbook = 'base.yml'

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

def generateInventoryFile(file):
    with open(file, 'w') as f:
        f.write('[base]\n')
        for host in args.targets:
            f.write(host+'\n')
    f.close()

def gitUpdate():
    print(' -> Fetching latest version from Github...')
    call(['git', 'pull'])

def AnsibleDeploy(inventory, key, user):
    print(' -> Deploying the services...')
    call(['ansible-playbook', '-i', inventory, '--key-file', key, '-u', user, playbook])

gitUpdate()
generateInventoryFile(inventoryFile)
try:
    AnsibleDeploy(inventoryFile, args.sshKey, args.sshUser)
except FileNotFoundError:
    print("Error - Seems like Ansible is not installed, try 'pip2 install ansible' and try again")
    exit()
