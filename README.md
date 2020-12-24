# Github_crawler
Github_crawler is a crawler for Github search <br />

Input values are hardcoded in json file in the src/config folder. There are 4 different json file 3 of them for 3 different type and one for unicode keyword.<br />

## Usage

Main libraries used for crawler
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

to run the code for unicode Keywords ('Россия') with type repositories
```bash
python github_crawler.py -u
```
