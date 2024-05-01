import sqlite3 

data = [
    ('0000.AA1A.CCCC', 'sw5', 'Cisco 3750', 'London, Green Str'),
    ('0000.BB3B.CCCC', 'sw6', 'Cisco 3780', 'London, Green Str'),
    ('0000.ACAA.DDDD', 'sw7', 'Cisco 2960', 'London, Green Str'),
    ('0011.AAAA.CCCC', 'sw8', 'Cisco 3750', 'London, Green Str')]


conn = sqlite3.connect('dhcp_snooping.db')

with open('dhcp_snooping_schema.sql') as f:
    conn.executescript(f.read())

try:
    query = 'INSERT into switch values (?, ?, ?, ?)'
    conn.executemany(query,data)
    conn.commit()
except sqlite3.IntegrityError as err:
    print('Error', err )


for row in conn.execute("select * from switch"):
    print(row)

conn.close()

