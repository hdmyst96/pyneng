#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
result  = ()
access_intf = {}
trunk_intf = {} 
with open('config_sw1.txt') as file:
    for line in file:
       if "FastEthernet" in line:
           intf = line.split()[-1]
           access_intf[intf] = {}
           trunk_intf[intf] = {}
       elif "access vlan" in line:
               vlan = line.split()[-1]
               access_intf[intf] = int(vlan)
       elif "allowed vlan" in line:
              list_vlan = line.split()[-1].split(',') 
              trunk_intf[intf] = [int(numb) for numb in list_vlan]

access_intf = {key:value for key, value in access_intf.items() if not value == {}}
trunk_intf  = {key:value for key, value in trunk_intf.items() if not value == {}}
result = (access_intf,trunk_intf)  
