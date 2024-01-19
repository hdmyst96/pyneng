#!/usr/bin/env python3

import sqlite3 
import os 
import re
import yaml
dhcp_snooping = ['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt','sw3_dhcp_snooping.txt']
switches = 'switches.yml'

#Controllare se il database esiste
db_exists = os.path.exists('dhcp_snooping.db')


#parsing switches data
switches_parsed = []
with open('switches.yml') as file:
    result = yaml.load(file)
    for key,value in result.items():
        for int_key,int_value in  value.items():
            switches_parsed.append((int_key,int_value))

#parsing dhcp snooping database
dhcp_snooping_parsed = []
regex = r'(\S+) +(\S+) +\d+.*?(\d+) +(\S+)'
for element in dhcp_snooping:
    intf = []
    with open(element) as file2:
        intf.append(element.split('_')[0])
        intf = tuple(intf)
        for line in file2:
            match =  re.match(regex, line)
            if match:
                dhcp_snooping_parsed.append(match.groups() + intf)

connect = sqlite3.connect('dhcp_snooping.db')

#Insert switches data in database
switch_query = 'INSERT INTO switches values (?, ?)'
print('Add data to table switches')
for row in switches_parsed:
    try:
        connect.execute(switch_query,row)
        connect.commit()
    except sqlite3.IntegrityError as error:
        print('Adding data: {} found an error: '.format(row),error)

#Insert dhcp snooping  data in database
dhcp_snooping_query = 'INSERT INTO dhcp VALUES(?, ?, ?, ?, ?)'
print('Add data to table dhcp')
for row in dhcp_snooping_parsed :
    try:
        connect.execute(dhcp_snooping_query,row)
        connect.commit()
    except sqlite3.IntegrityError as err:
        print('Adding data: {} found an error: '.format(row),err)

connect.close()
