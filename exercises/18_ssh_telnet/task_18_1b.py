# -*- coding: utf-8 -*-
"""
Задание 18.1b

Скопировать функцию send_show_command из задания 18.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется при ошибке
аутентификации на устройстве, но и исключение, которое генерируется, когда IP-адрес
устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться
сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
"""
def send_show_command(device,command):
    print( "Connect to {}".format(device['host']) )
    try:
        with  netmiko.ConnectHandler(**device) as ssh:
            ssh.enable()
            return ssh.send_command(command)
    except (netmiko.NetmikoAuthenticationException,netmiko.NetmikoTimeoutException) as err:
        print(err)

if __name__ == "__main__":
    command = "sh ip int br"

    dev = {'device_type': 'cisco_ios',
           'host': '192.168.100.9',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco',
            'timeout': 10}

    send_show_command(dev,command)
