"""Github Crawler"""
from src.github_search import Github
from src.utils.load_json import load_json

if __name__ == "__main__":
    _input = load_json('src\config\input_repositories.json')
    keywords = _input['keywords']
    proxies = _input['proxies']
    type_of_object = _input['type']
    github = Github(keywords, proxies, type_of_object)
    result = github.compute()
    print(result)