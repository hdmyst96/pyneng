#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
from pprint import pprint

def parse_sh_cdp_neighbors(output_cdp):
    result = {}
    for line in output_cdp.split('\n'):
         match = re.search(r'(?P<device>\w+)>',line)
         match2 = re.search(r'(?P<device2>\S+) +(?P<intf1>\S+ \S+) +\d+ +(?:\w+ )+ +\S+ +(?P<intf2>\S+ \S+)',line)
         if match:
             device =(match.group('device'))
             result[device] = {}
         elif match2:
             device2,intf1,intf2 =  match2.groups()
             result[device][intf1] = {device2:intf2}
    return result


if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt') as file:
        pprint(parse_sh_cdp_neighbors(file.read()))
