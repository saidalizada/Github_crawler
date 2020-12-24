"""Github Crawler"""
from src.github_search import Github
from src.utils.load_json import load_json
import sys

if __name__ == "__main__":
    try:
        input_value = sys.argv[1]
    except:
        input_value = '-r'

    if input_value == '-i':
        _input = load_json('src/config/input_issues.json')
    elif input_value == '-r':
        _input = load_json('src/config/input_repositories.json')
    elif input_value == '-w':
        _input = load_json('src/config/input_wiki.json')
    elif input_value == '-u':
        _input = load_json('src/config/input_unicode.json')
    else:
        _input = load_json('src/config/input_repositories.json')
        
    keywords = _input['keywords']
    proxies = _input['proxies']
    type_of_object = _input['type']
    github = Github(keywords, proxies, type_of_object)
    result = github.compute()
    print(result)