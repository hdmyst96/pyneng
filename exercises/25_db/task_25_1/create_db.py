#!/usr/bin/env python3 

import sqlite3

def create_dhcp_snooping_db(dbfilename):
    '''
    La funzione crea  la tabella dhcp_snooping.db;
    dentro la schema gia completata;
    come argomento prende il nome del file, 
    di solito dhcp_snooping.db
    '''
    connection = sqlite3.connect(dbfilename)
    try:
        with open('dhcp_snooping_schema.sql') as file:
            schema = file.read()
            connection.executescript(schema)
            print('Sto creando la tabella...')
    except sqlite3.OperationalError:
        print('La tabella e gia creata')


if __name__ == "__main__":
    create_dhcp_snooping_db('dhcp_snooping.db')

