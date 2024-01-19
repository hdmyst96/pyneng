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



