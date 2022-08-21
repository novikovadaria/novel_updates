import requests
from bs4 import BeautifulSoup
import requests
import csv
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}
for count in range(345, 531):
    url = f"https://www.novelupdates.com/novelslisting/?st=1&pg={count}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    screen = soup.find('div', class_='l-content')
    data = screen.find_all('div', class_='search_main_box_nu')
    for inf in data:
        block = inf.find('div', class_='search_body_nu')
        search_title = inf.find('div', class_='search_title')
        title = inf.find('a').text
        search_status = inf.find('div', class_='search_stats')
        chapters = inf.find('span', class_='ss_desk').text
        f = open('novel.csv', 'a', encoding='utf-8')
        f.write(f"'{title} ' ,\n")
f.close()
