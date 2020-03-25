#body-content > div.newest-list > div > table > tbody > tr:nth-child(3) > td.number

#body-content > div.newest-list > div > table > tbody > td
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
musics = soup.select("#body-content > div.newest-list > div > table > tbody > tr")

rank = 0
for music in musics:
    title = music.select_one("td.info > a.title.ellipsis")

    title = title.text

    new_title = " ".join(title.split())

    singer = music.select_one("td.info > a.artist.ellipsis")

    if new_title is not None:
        rank += 1

        print(rank, new_title, "by",  singer.text)

    # body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number



