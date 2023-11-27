#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
""" 
ip = input('Inserisci IP: ')
ip_list = ip.split('.')

#Verification programm
for octet in ip_list:
    if len(ip_list) == 4 and not octet.isnumeric():
        print('ip address sbagliato')
        break
    elif octet >= '255':
        print('ip address sbagliato')
        break

for int in ip_list:
    if '1' <= octet  <= '223':
        print('unicast')
        break
    elif '224'<= octet<= '239':
        print('multicast')
        break
    if ip_list == ['255', '255', '255', '255']:
        print('local broadcast')
        break
    elif ip_list == ['0','0','0','0']:
        print('unassigned')
        break
    else:
        print('unused')
        break
