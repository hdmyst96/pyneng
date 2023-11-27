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


ip = input('Inserisci IP: ')
ip_list = ip.split('.')
ip_correct = False
oct = ip.split('.')[0]
#Verification programm
while not ip_correct:
    if len(ip_list) != 4:
        print('ip address sbagliato')
        ip_correct = True 
        break
    for int in ip_list:
        if not int.isnumeric():
            print('ip address sbagliato')
            ip_correct = True    
            break        
        elif int > '255':
            print('ip address sbagliato')
            ip_correct = True
            break
#Main programm 
    else: 

        if ip_list == ['255', '255', '255', '255']:
            print('local broadcast')
        elif ip_list == ['0','0','0','0']:
            print('unassigned')
        elif '1' <= oct  <= '223':
            print('unicast')
        elif '224'<= oct<= '239':
            print('multicast')
        else:
            print('unused')
    ip_correct = True
