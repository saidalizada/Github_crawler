"""Github Crawler"""
from github_search import Github

if __name__ == "__main__":
    keywords = ['test', 'python']
    proxies = ['182.16.255.194:43419', '182.16.255.194:43419']
    type_of_object = 'repositories'
    github = Github(keywords, proxies, type_of_object)
    result = github.compute()
    print(result)