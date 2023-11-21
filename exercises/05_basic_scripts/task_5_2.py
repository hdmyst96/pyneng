#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
#chiedere al utente di inserire il ip ed il mask
ipmask = input('insert ip and mask: ')

#dividere ip dal mask
ipmask = ipmask.split('/')
ip = ipmask[0:1]
ip = '.'.join(ip)
ip = ip.split('.')

#convertire il ip in nr binario 
network_template = '''
     Network:
     {0:<8} {1:<8} {2:<8} {3:<8}
     {0:08b} {1:08b} {2:08b} {3:08b}
     '''
#mostrare ip in nr binario e normale
print(network_template.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))

#incapsulre il mask in una variabile 
maskd = ipmask[1:2]
mask = ipmask[1:2]

mask = ''.join(mask)
#convertire il mask in numero binario 
mask = "1" * int(mask) + "0" * 4  

#controllare se il mask ha 32 bit, nel caso aggiungere i 0 mancanti
mask =  mask.ljust(32, "0")

#aggiungere i punti tra i otteti
mask = mask[0:8] + "." + mask[8:16] + "." +  mask[16:24] + "." + mask[24
:32]
mask =  mask.split('.')

# usare la mask nel template 
mask_template = '''
     Mask:
     {0:}
     {5:<8} {6:<8} {7:<8} {8:<8}
     {1:08} {2:08} {3:08} {4:08}
                '''


print(mask_template.format(int(maskd[0]), int(mask[0]), int(mask[1]), int
(mask[2]), int(mask[3]), int(mask[0],2), int(mask[1],2), int(mask[2],2)
, int(mask[3],2)))




