#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
src = argv[1]
dest = argv[2] 
ignore = ["duplex", "alias", "configuration"]

with open('config_sw1.txt')  as src, open('result.txt', 'w') as dest:
    for line in src:
        if line.startswith('!'):
            pass
        elif ignore[0] in line:
            pass
        elif ignore[1] in line:
            pass
        elif ignore[2] in line:
            pass
        else:
            dest.write(line)

