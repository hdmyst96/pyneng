#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress


def convert_ranges_tp_ip_list(iplist):
    list_of_ips1 = []
    list_of_ips2 = [] 
    for ip in iplist:
        try:
            ipaddress.ip_address(ip)
            list_of_ips1.append(str(ip))
        except ValueError:
            ipsplit = ip.split('-') 
            first_ip, range_ip = ipsplit
            ipobject = ipaddress.ip_address(first_ip)
            try:
               ipaddress.ip_address(range_ip)
               range_ip = range_ip.split('.')[-1]
               last_octet_first_ip = first_ip.split('.')[-1]
               range_ip = int(range_ip)-int(last_octet_first_ip) +1
               list_of_ips2 = [str(ipobject +i) for i in range(int(range_ip))]
            except ValueError:
               list_of_ips2 = [str(ipobject +i) for i in range(int(range_ip))]
    return list_of_ips1 + list_of_ips2


if __name__ == "__main__":
    ipsrange = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_tp_ip_list(ipsrange))
