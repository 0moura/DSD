import csv

from serpapi import GoogleSearch

def g_search(url, pagination, name_file, key):
    for i in pagination:
        params = {
            "q": url,
            "engine": "google",
            "location": "Austin, Texas, United States",
            "device": "desktop",
            "hl": "pt",
            "gl": "br",
            "num": 100,
            "start": i,
            "api_key": key,
            "async": "false",
            "output": "json"
        }
        search = GoogleSearch(params)
        result = search.get_json()
        for data in result['organic_results']:
            with open(name_file, "a", newline='', encoding='latin1', errors='ignore') as f:
                datax = csv.writer(f)
                datax.writerow(data['link'].split(','))