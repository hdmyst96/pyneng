import sqlite3 
import sys

db_filename = 'dhcp_snooping.db'

key,value = 'ip', '10.1.10.2'
keys = ['mac', 'vlan', 'interface']


conn = sqlite3.connect(db_filename)

#Permette di communicare con i dati delle colonne
conn.row_factory = sqlite3.Row

print('\nDetailed information for host with', key,value)
print('-' * 40)

query = 'select * from dhcp where {} = ?'.format(key)
result = conn.execute(query, (value,  ))

for row in result:
    for k in keys:
        print('{:12}: {}'.format(k,row[k]))
    print('-' * 40)

