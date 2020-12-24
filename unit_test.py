from src.github_search import Github
import unittest
from random import randint

class TestMethods(unittest.TestCase):
    
    def test_repositories_type(self):
        keywords = ['test','python']
        proxies = ['182.16.255.194:43419','182.16.255.194:43419'] 
        type_of_object = 'repositories'
        github = Github(keywords, proxies, type_of_object)
        result = github.compute()
        self.assertEqual(list(result[0].keys()), ['url', 'extra'])

    def test_issues_type(self):
        keywords = ['test','python']
        proxies = ['182.16.255.194:43419','182.16.255.194:43419'] 
        type_of_object = 'issues'
        github = Github(keywords, proxies, type_of_object)
        result = github.compute()
        self.assertEqual(list(result[0].keys()), ['url'])

    def test_wikis_type(self):
        keywords = ['test','python']
        proxies = ['182.16.255.194:43419','182.16.255.194:43419'] 
        type_of_object = 'wikis'
        github = Github(keywords, proxies, type_of_object)
        result = github.compute()
        self.assertEqual(list(result[0].keys()), ['url'])

    def test_length(self):
        keywords = ['test','python']
        proxies = ['182.16.255.194:43419','182.16.255.194:43419'] 
        type_of_objects = ['wikis', 'issues', 'repositories']
        rand_n = randint(0,2)
        type_of_object = type_of_objects[rand_n]
        github = Github(keywords, proxies, type_of_object)
        result = github.compute()
        self.assertEqual(len(result), 10)

    def test_get_extra_info_repo(self):
        url = 'https://github.com/geekcomputers/Python'
        keywords = ['test','python']
        proxies = ['182.16.255.194:43419','182.16.255.194:43419'] 
        type_of_object = 'repositories'
        github = Github(keywords, proxies, type_of_object)
        result = github.get_extra_info_repo(url)
        self.assertEqual(result[0], 'geekcomputers')

    

if __name__ == '__main__':
    unittest.main()