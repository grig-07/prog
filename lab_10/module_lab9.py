# module_lab9.py 
 
import requests 
 
def fetch_data(url): 
    �ਬ�� �㭪樨 ��� �믮������ �⥢��� �����. 
    print(f"Fetching data from {url}...") 
    response = requests.get(url) 
    response.raise_for_status() 
    return response.json() 
