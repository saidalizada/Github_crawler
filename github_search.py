import requests
import bs4
from random import randint

class Github:

    def __init__(self, keywords, proxies, type):
        self.keywords = keywords
        self.type = type
        random_n = randint(0,len(proxies)-1)
        proxy = proxies[random_n]
        self.proxy = proxy
        self._root_url = 'https://github.com'

    def get_githup_search_url(self):
        _root_url = self._root_url
        keywords = self.keywords
        type = self.type
        query = "+".join(keywords)
        url = f'{_root_url}/search?q={query}&type={type}'
        return url
    
    def soup(self, url):
        proxy = self.proxy
        proxy_dict = {"http": f"http://{proxy}",}
        r = requests.get(url, proxies=proxy_dict)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        return soup

    def get_extra_info_repo(self, url):
        language_stats_list = []
        soup = self.soup(url)
        owner = soup.find('span', attrs={"class": "author"}).text
        languages = soup.find_all(name='div', attrs={"class": "BorderGrid-cell"})[-1].find_all('li')
        for language in languages:
            language_info = language.find_all('span')
            language_name = language_info[0].text
            language_percentage = language_info[1].text
            language_stats_list.append((language_name, language_percentage))
        language_stats = dict(language_stats_list)
        return owner, language_stats

    def compute(self):
        l = []
        _root_url = self._root_url
        type = self.type
        githup_url = self.get_githup_search_url()
        githup_search = self.soup(githup_url)
        url_list = githup_search.find_all(name="div", attrs={"class": "f4"})
        for url in url_list:
            get_url = url.find('a').get('href')
            _url = _root_url + get_url
            if type == 'repositories':
                owner, language_stats = self.get_extra_info_repo(_url)
                url_dict =  {"url": _url, "extra": {"owner": owner,\
                    "language_stats":language_stats}}
                l.append(url_dict)   
            else:
                url_dict = {"url": _url}
                l.append(url_dict)
            
        print(l)
        return l
    