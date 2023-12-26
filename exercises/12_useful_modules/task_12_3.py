#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate 

def print_ip_table(reachips,unreachips):
    ips_dict = {"Reachable": reachips,
                "Unreachable": unreachips }
    return print(tabulate(ips_dict,headers="keys"))



if __name__ == "__main__":
    reach_ip = ['10.10.1.7', '10.10.1.8', '10.10.1.9', '10.10.1.15']
    unreach_ip = ['10.10.2.1', '10.10.1.2']
    print_ip_table(reach_ip,unreach_ip)
