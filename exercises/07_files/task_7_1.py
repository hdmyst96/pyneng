#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

""" 
ospft_template = '''
Prefix {:>30}
AD/Metric {:>21}
Next-Hop {:>25}
Last update {:>18} 
Outbound Interface {:>21}
'''

with open('ospf.txt') as f:
    for line in f:
        line_split = line.split()
        line_split[4] = line_split[4].removesuffix(',')
        line_split[5] = line_split[5].removesuffix(',')
        line_split[2] = line_split[2].strip('[]')
        print(ospft_template.format(line_split[1],line_split[2],line_split[4],line_split[5],line_split[6]))
