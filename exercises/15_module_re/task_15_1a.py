#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re
from pprint import pprint

'''
def get_ip_from_cfg(config_file):
    result = {}
    def_result = {}
    with open(config_file) as f:
        for line in f:
            intf = re.search(r'^interface (\S+)',line)
            ip_masks = re.search(r'ip address (\S+) (\S+)',line)
            if intf:
                intf_match = intf.group(1)
                result[intf_match] = ()
            elif ip_masks:
                result[intf_match] = ip_masks.groups()
        for key,value in result.items():
            if not value == ():
                def_result[key] = value
        return def_result


if __name__ == "__main__":
   result = get_ip_from_cfg('config_r1.txt')
   pprint(result)
'''


#Second variant

def get_ip_from_cfg(config_file):
    regex = r'interface (\S+)\n(?:.*\n)*? ip address (\S+) (\S+)'
    result = {}
    with open(config_file) as f:
        match = re.finditer(regex,f.read())
        for element in match:
            result[element.group(1)] = element.group(2,3)
    return result 

if __name__ == "__main__":
   result = get_ip_from_cfg('config_r2.txt')
   pprint(result)

