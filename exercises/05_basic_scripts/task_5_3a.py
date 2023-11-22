#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""
inter = input("Inserice la interfaccia(numero/tipo): ")
port = input("Inserisce il porto di accesso(access/trunk): ")

v = {"access": ("Inserice numeri  di VLAN: "), "trunk": ("Inserice Vlan accessibile: ") }
v = input(v[port])   

#aggiungere delimitatore 
print("" * 100)

#Mostrare interfaccia 
print("interface {}".format(inter))

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

#transformare le liste in un dizionario per poter chiamare la sezione(trunk/acc.)
templates = {'access': access_template, 'trunk': trunk_template}

print('\n'.join(templates[port]).format(v))

