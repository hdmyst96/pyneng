#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess


def ping_ip_addresses(ip_list):
    true_ip = []
    false_ip = []
    print('Work in progress...')
    for ip in ip_list:
        ping_ips = subprocess.run('ping -c 2 -n {}'.format(ip),shell=True,stdout=subprocess.PIPE)
        if ping_ips.returncode == 0:
            true_ip.append(ip)
        else:
            false_ip.append(ip)
    return tuple([true_ip] + [false_ip])


if __name__ == "__main__":
    
    list_of_ips = ['1.1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']
    print(ping_ip_addresses(list_of_ips))
