import requests
from bs4 import BeautifulSoup
import csv

source=requests.get('https://coreyms.com/').text
#print(source.status_code)

soup=BeautifulSoup(source,'lxml')
#print(soup.prettify())
csv_file=open('output.csv','w')
csv_writter=csv.writter(csv_file)
csv_writter.writerow(['Headline','Summary','Youtube Link'])

for article in soup.find_all('article'):
#print(article.prettify())
    headline=article.a.text
    print(headline)

    summary=article.find('div',class_='entry-content').p.text
    print(summary)
    try:
        video_src=article.find('iframe',class_='youtube-player')['src']
        video_id=video_src.split('/')[4]
        video_id=video_id.split('?')[0]
        # print(video_id)
        youtube_link = f'https://youtube.com/watch?v={video_id}'

    except Exception as e:
        youtube_link='NONE'
    print(youtube_link)
    print()
    csv_writter.writerow([headline,summary,youtube_link])
csv_file.close()