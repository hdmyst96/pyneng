#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Inserisci IP: ')
ip_list = ip.split('.')
ip_correct = False
#Verification programm
while not ip_correct:
    oct = ip.split('.')[0]
    ip_list = ip.split('.')
    if len(ip_list) != 4:
        print('ip address sbagliato')
        ip = input('Inserisci di nuovo IP: ')
        continue
    for int in ip_list:
        if not int.isnumeric() or  int > '255':
            print('ip address sbagliato')
            ip = input('Inserisci di nuovo IP: ')
            break
#Main programm
    else:
        if ip_list == ['255', '255', '255', '255']:
            print('local broadcast')
            ip_correct = True
        elif ip_list == ['0','0','0','0']:
            print('unassigned')
            ip_correct = True
        elif '1' <= oct  <= '223':
            print('unicast')
            ip_correct = True
        elif '224'<= oct<= '239':
            print('multicast')
        else:
            print('unused')
            ip_correct = True
