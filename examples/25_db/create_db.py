import sqlite3


data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]

#Per connetersi ad un database
conn = sqlite3.connect('dhcp_snooping.db')

#Per iscrivere la schema dentro il database
with open ('dhcp_snooping_schema.sql') as f:
    conn.executescript(f.read())
    print('The table created')

#Per aggiungere i dati nel database
try:
    query = 'INSERT into switch values (?, ?, ?, ?)'
    for line in data:
        with conn:   #start transaction
            conn.execute(query, line)
                     #commit
except sqlite3.IntegrityError as error:
    print('Errore', error)


#Per mostrare i dati
result = conn.execute('select * from switch')
for row in result:
    print(row)

conn.close()

