# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
from concurrent.futures import  ThreadPoolExecutor, as_completed
import subprocess


def ping_ip(ip):
    p = subprocess.run(["ping","-c","3","-n",ip],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,)
    return p


def ping_ip_addresses(ip_lists, limit=3):
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        futures = [executor.submit(ping_ip,ipv4)
                   for ipv4 in ip_lists]
        for f in as_completed(futures):
            result = f.result()
            ip = result.args[-1]
            if result.returncode == 0:
                reachable.append(ip)
            else:
                unreachable.append(ip)
    return reachable,unreachable


if __name__ == "__main__":
    list_of_ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "2.2.2.2"]
    print(ping_ip_addresses(list_of_ips))
