# Github_crawler
Github_crawler is a crawler for Github search

## Usage
Input values are hardcoded in json file in the src/config folder

### Main libriries used for crawler
```bash
pip install bs4
pip install requests
```
to run the code for type repositories

```bash
python github_crawler.py
```

to run the code for type issues

```bash
python github_crawler.py -i
```

to run the code for type wiki

```bash
python github_crawler.py -w
```

to run the code for unicode Keywords 'Россия' with type repositories
```bash
python github_crawler.py -u
```