# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
#chiedere al utente di inserire il ip ed il mask
ipmask = input('insert ip and mask: ')

#dividere ip dal mask
ipmask = ipmask.split('/')
ip = ipmask[0:1]
ip = '.'.join(ip)
ip = ip.split('.')
ip_template = '''{:08}.{:08}.{:08}.{:08} '''
ip_bin =  ip_template.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))

#convertire gli ultimi bit nel ip address per arrivare ad network mask !
replace_ip =  ip_bin[0:-4]
replace_ip1 = ip_bin[31:]
replace_ip1 = replace_ip1.replace("1", "0")
ip_bin = replace_ip + replace_ip1 



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
