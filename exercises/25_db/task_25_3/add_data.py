#!/usr/bin/env python3

import sqlite3
import re
import os
import yaml

def control_db_exists(dbfilename):
    '''
    La funzione richiede un argomento con
    il nome del database, poi controlla se 
    il db esiste, ritorna TRUE, in caso contrario
    FALSE
    '''
    db_exists = os.path.exists(dbfilename)
    return db_exists

def insert_data_db(query, data):
    for row in data:
        try:
            connect.execute(query,row)
            connect.commit()
        except sqlite3.IntegrityError as error:
            print('Adding data: {} found an error: '.format(row),error)


#parsing switches data
switches_parsed = []
with open('switches.yml') as file:
    result = yaml.load(file)
    for key,value in result.items():
        for int_key,int_value in  value.items():
            switches_parsed.append((int_key,int_value))

dhcp_snooping = ['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt','sw3_dhcp_snooping.txt']


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

switch_query = 'INSERT INTO switches values (?, ?)'
dhcp_snooping_query = 'INSERT INTO dhcp VALUES(?, ?, ?, ?, ?)'

db_exists = control_db_exists('dhcp_snooping.db')
if db_exists:
    connect = sqlite3.connect('dhcp_snooping.db')
    print('Sto aggiungendo swith data in database')
    insert_data_db(switch_query,switches_parsed)
    print('Sto aggiungendo dhcp data in database')
    insert_data_db(dhcp_snooping_query,dhcp_snooping_parsed)
else: 
    print('Il database non esiste. Deve essere prima creato!')
