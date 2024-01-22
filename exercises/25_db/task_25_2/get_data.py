#!/usr/bin/env python3
import sqlite3
from tabulate import tabulate 
import sys

def get_data_with_argv():
        try: 
            key,value = sys.argv[1:]
            keys = ['mac', 'ip','vlan', 'interface', 'switch']

            connect = sqlite3.connect('dhcp_snooping.db')
            connect.row_factory = sqlite3.Row
            try:
                query = "SELECT * from dhcp where {} = ?".format(key)
                result = connect.execute(query, (value, ))
                if len(sys.argv) == 3:
                    print("Information about device with such a configuration:", key,value)
                    print('-' * 50)
                    for row in result:
                        for k in keys:
                            print('{:12}:{}'.format(k,row[k]))
                        print('-' * 50)
            except sqlite3.OperationalError:
                print("This argument is not supported")
                print("Try one of these: mac, ip, vlan, interface, switch")
        except ValueError as error:
            if len(sys.argv) == 1:
                connect = sqlite3.connect('dhcp_snooping.db')
                connect.row_factory = sqlite3.Row
                all_elements = []
                for row in connect.execute('SELECT * from dhcp'):
                    all_elements.append(row)
                print(tabulate(all_elements))
            elif len(sys.argv) == 2 or len(sys.argv) > 3:
                print('Please, insert zero or two arguments!')


get_data_with_argv()
