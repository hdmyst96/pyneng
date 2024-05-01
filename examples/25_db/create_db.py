import sqlite3 

data = [
    ('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
    ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
    ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
    ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]


conn = sqlite3.connect('dhcp_snooping.db')

with open('dhcp_snooping_schema.sql') as f:
    conn.executescript(f.read())

query = 'INSERT into switch values (?, ?, ?, ?)'
for line in data:
    try:
        with conn: # start transaction
            conn.execute(query,line)
                   # commit 
    except sqlite3.IntegrityError as err:
        print('Error', err )


for row in conn.execute("select * from switch"):
    print(row)

conn.close()

