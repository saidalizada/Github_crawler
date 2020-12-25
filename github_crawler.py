"""Github Crawler"""
import sys
from src.github_search import Github
from src.utils.load_json import load_json
from src.utils.write_json import write_json

if __name__ == "__main__":
    try:
        INPUT_VALUE = sys.argv[1]
    except Exception:
        INPUT_VALUE = '-r'

    if INPUT_VALUE == '-i':
        INPUT = load_json('src/config/input_issues.json')
    elif INPUT_VALUE == '-r':
        INPUT = load_json('src/config/input_repositories.json')
    elif INPUT_VALUE == '-w':
        INPUT = load_json('src/config/input_wiki.json')
    elif INPUT_VALUE == '-u':
        INPUT = load_json('src/config/input_unicode.json')
    else:
        INPUT = load_json('src/config/input_repositories.json')

    KEYWORDS = INPUT['keywords']
    PROXIES = INPUT['proxies']
    TYPE_OF_OBJECT = INPUT['type']
    GITHUB = Github(KEYWORDS, PROXIES, TYPE_OF_OBJECT)
    RESULT = GITHUB.compute()
    write_json(RESULT)
    print(RESULT)
