import csv
import time
from termcolor import colored
import requests

def download_files(url, path, file_error):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    time.sleep(2)
    try:
        response = requests.get(url, headers=user_agent, timeout=4)
        if response.status_code == requests.codes.OK:
            with open(path, 'wb') as new_file:
                new_file.write(response.content)
                print(colored(url, 'green'))
        else:
            with open(file_error, "a", newline='', encoding='latin1', errors='ignore') as e:
                data_error = csv.writer(e)
                data_error.writerow(url.split())
                print(colored("[+] Erro {}".format(url), 'red'))
    except:
        print("servidor frescando")
        print("tirando um cochilo pra despistar")
        print("ZZzzzz...")
        time.sleep(6)
        print("pse")