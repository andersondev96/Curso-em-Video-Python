"""
Crie um código em Python que teste se o site pudim
está acessível pelo computador usado.
"""

import requests
try:
    url = "http://pudim.com.br/"
    page = requests.get(url)
except:
    print('\033[1;31mO site pudim não está acessível\033[m')
else:
    print('\033[1;92mO site pudim está acessível\033[m')