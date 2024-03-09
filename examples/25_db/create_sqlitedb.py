import os
import sqlite3 
import re
import sys

data_filename = 'dhcp_snooping.txt'
db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'

regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

result = []

#parsing dei dati necessari per poter dopo inserirli nel database
with open('dhcp_snooping.txt') as data:
    for line in data:
        match = regex.search(line)
        if match:
            result.append(match.groups())

db_exists = os.path.exists(db_filename)

conn = sqlite3.connect(db_filename)

#Creare tabella inserendo dentro le colonne 
if not db_exists:
    print('Creating schema')
    with open ('dhcp_snooping_schema.sql') as f:
        schema  = f.read()
        conn.executescript(schema)
        print("Done")
else:
    print('Database already exists')

#Scrivere i dati nella tabella
print('Inserting data in database')
for row in result:
    try:
        with conn:
            query = '''insert into dhcp (mac, ip, vlan, interface)
                       values (?, ?, ?, ?)'''
            conn.execute(query,row)
    except sqlite3.IntegrityError as error:
        print('Error occured: ',error)

conn.close()
