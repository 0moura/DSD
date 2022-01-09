import os
from src.dir import check_dir
from src.google import g_search
from src.read import read_csv

key = 'chave aqui'

url = input('Informe a url:')
path_dir = input('nome do diretorio ou sub:')
name_file = input('nome do arquivo:')
page = input('paginas a serem buscadas:')
pagination = [*range(0, int(page) * 100 + 100, 100)]
pagination.pop(-1)
path_file = os.path.join(check_dir(path_dir), name_file)

g_search(url, pagination, path_file, key)
read_csv(path_file, path_dir)
