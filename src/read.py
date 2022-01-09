import csv
import os
from urllib.parse import urlparse
from src.verification import check

def read_csv(csv_name, path_download):

    with open(csv_name) as csv_file:
        reader = csv.reader(csv_file)
        for url in reader:
            name_file = urlparse(url[0]).path.split('/')[-1]
            path_full = os.path.join(path_download, name_file)
            lines_file = reader.line_num
            check(url[0], name_file, path_full, lines_file, csv_name+'-error.txt')
