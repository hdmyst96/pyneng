#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

""" 

result = []
#Ho aperto il file/ ho estratto gli elementi che mi servono/ gli ho aggiutno in una lista 
with open('CAM_table.txt') as file:
    for line in file:
        if line.startswith(' '):
            vlan  =   line.lstrip(' ').split()[0]
            mac =  line.lstrip(' ').split()[1]
            port =  line.lstrip(' ').split()[-1]
            if not vlan == 'Mac' and not mac == 'Address' and not port == 'Table':
                y ='{:6} {:17} {:5}'.format(vlan,mac,port)
                y =''.join(y).split()
                result.append(y)
#ho transformato primo elemento di ogni lista in integer per poter sortare in seguito, poi ho  
result1 = []
for line in result:
    tmp = []
    for element in line:
        if element.isdigit():
            tmp.append(int(element))
        else:
            tmp.append(element)
    result1.append(tmp)

result1 = sorted(result1) 

#Chiedre al utente di scegliere vlan e mostrare solo intf con vlan corrispondente 

vl = input("Inserisci Vlan: ")
for line in result1:
    if int(vl) in line:
        print('{} {} {}'.format(line[0],line[1],line[2]))



