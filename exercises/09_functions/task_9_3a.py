#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_map(config_filename):
    ''' la funzione estrae dal file le interface
    nella modalita access e nella modalita trunk 
    poi le metti in un tuple in cui al interno 
    sara la interfaccia e i numeri dei port,nella
    forma di dizionario '''
    result = ()
    access_intf = {}
    trunk_intf = {}
    with open(config_filename) as file:
        for line in file:
             if "FastEthernet" in line:
                 intf = line.split()[-1]
                 access_intf[intf] = {}
                 trunk_intf[intf] = {}
             if "access vlan" in line:
                 vlan = line.split()[-1]
                 access_intf[intf] = int(vlan)
             if "access vlan"  in line:
                 vlan = line.split()[-1]
                 access_intf[intf] = int(vlan)
             elif "mode access" in line:
                 access_intf[intf] = int(1)
             elif "allowed vlan" in line:
                 list_vlan = line.split()[-1].split(',')
                 trunk_intf[intf] = [int(numb) for numb in list_vlan]

    access_intf = {key:value for key, value in access_intf.items() if not value == {}}
    trunk_intf  = {key:value for key, value in trunk_intf.items() if not value == {}}
    result = (access_intf,trunk_intf) 
    return result

print(get_int_map('config_sw2.txt'))
