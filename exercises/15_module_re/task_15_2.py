#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re
from pprint import pprint

def parse_sh_ip_int_br(filename):
    result = []
    regex = (r'(\S+) +((?:\d+.)+(?:\d)).*manual (\S+).+?(?P<port2>\S+)|'
             r'(\S+) +(\S+).*unset +((?:\S+) (?:\S+)) (\S+)')
    with open(filename) as f:
        for line in f:
            match = re.search(regex,line)
            if match:
                if match.lastgroup == 'port2':
                    result.append(match.group(1,2,3,4))
                else:
                    result.append(match.group(5,6,7,8))
        return result     


if __name__ == "__main__":

   pprint(parse_sh_ip_int_br('sh_ip_int_br.txt'))

