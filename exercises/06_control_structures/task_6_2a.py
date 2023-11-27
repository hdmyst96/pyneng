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
    if len(ip_list) != 4:
        print('ip address sbagliato')
        break
    elif not octet.isnumeric():
        print('ip address sbagliato')
        break
    elif octet >= '255':
        print('ip address sbagliato')
        break        
#Main programm 
oct = ip.split('.')[0]
if '1' <= oct  <= '223':
    print('unicast')
elif '224'<= oct<= '239':
    print('multicast')
elif ip_list == ['255', '255', '255', '255']:
    print('local broadcast')
elif ip_list == ['0','0','0','0']:
    print('unassigned')
else:
    print('unused')
