""" Github class to compute search result of the crawler"""
from random import randint
import requests
import bs4

class Github:

    def __init__(self, keywords, proxies, type_of_object):
        self.keywords = keywords
        self.type_of_object = type_of_object
        random_n = randint(0, len(proxies)-1)
        proxy = proxies[random_n]
        self.proxy = proxy
        self._root_url = 'https://github.com'

    def get_githup_search_url(self):
        """ Get url of the search result """
        _root_url = self._root_url
        keywords = self.keywords
        type_of_object = self.type_of_object
        query = "+".join(keywords)
        search_url = f'{_root_url}/search?q={query}&type={type_of_object}'
        return search_url

    def soup(self, url):
        """ Making the Soup"""
        proxy = self.proxy
        proxy_dict = {"http": f"http://{proxy}",}
        _requests = requests.get(url, proxies=proxy_dict)
        soup = bs4.BeautifulSoup(_requests.text, 'lxml')
        return soup

    def get_extra_info_repo(self, url):
        """ Getting owner and languages information(if exist).
            It is for optional task"""
        language_stats_list = []
        soup = self.soup(url)
        owner = soup.find('span', attrs={"class": "author"}).text
        owner = owner.replace('\n', '')
        languages_box = soup.find_all(name='div', attrs={"class": "BorderGrid-cell"})[-1]
        languages_box_header = languages_box.find('h2').text
        if languages_box_header == 'Languages':
            languages = languages_box.find_all('li')
            for language in languages:
                language_info = language.find_all('span')
                language_name = language_info[-2].text
                language_percentage = language_info[-1].text
                language_stats_list.append((language_name, language_percentage))
            language_stats = dict(language_stats_list)
        else:
            language_stats = ""
        return owner, language_stats

    def compute(self):
        """ Return urls of the search result. If type is repository
            Return also owner and languages information"""
        try:
            output_list = []
            _root_url = self._root_url
            type_of_object = self.type_of_object
            githup_url = self.get_githup_search_url()
            githup_search = self.soup(githup_url)
            url_list = githup_search.find_all(name="div", attrs={"class": "f4"})
            for url in url_list:
                get_url = url.find('a').get('href')
                _url = _root_url + get_url
                if type_of_object == 'repositories':
                    owner, language_stats = self.get_extra_info_repo(_url)
                    url_dict = {"url": _url, "extra": {"owner": owner,\
                        "language_stats":language_stats}}
                else:
                    url_dict = {"url": _url}
                output_list.append(url_dict)

            return output_list
        except Exception as error:
            print({"status": "Error", "feedbaxk": str(error)})
