import bs4
import time

from urllib import request

ROOT='https://ffxiv.consolegameswiki.com'
START_PAGE=ROOT + '/wiki/Category:NPCs'
USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'
ACCEPT='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'

with open('npcs.csv', 'w') as npc_fp:
    url = START_PAGE
    headers = {'User-Agent': USER_AGENT, 'Accept': ACCEPT}
    while True:
        print('Scraping {} ...'.format(url))
        url_req = request.Request(url, headers=headers)
        with request.urlopen(url_req) as req:
            body = req.read().decode('utf-8')
        
        soup = bs4.BeautifulSoup(body, features='html.parser')
        divs = soup.find_all(name='div', attrs={'id': 'mw-pages'})
        if len(divs) != 1:
            break
        
        npc_div = divs[0]
        for list_item in npc_div.find_all(name='li'):
            link = list_item.find_all('a')[0]
            npc_fp.write('{},{}{}\n'.format(link.text, ROOT, link.attrs['href']))
        
        next_link = npc_div.find_all('a', text='next page')
        if len(next_link) < 1:
            break
        url = ROOT + next_link[0].attrs['href']
        time.sleep(2)
