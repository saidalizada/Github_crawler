# Github_crawler
Github_crawler is a crawler for Github search <br />

Input values are hardcoded in json file in the [`src/config`](https://github.com/saidalizada/Github_crawler/tree/main/src/config) folder. There are 4 different json file 3 of them for 3 different type and one for unicode keyword.<br />
## Installation

Main libraries used for crawler
```bash
pip3 install -r requirements.txt
```

## Usage

If you want to run the code;
### for type repositories

```bash
python3 github_crawler.py
```

### for type issues

```bash
python3 github_crawler.py -i
```

### for type wiki

```bash
python3 github_crawler.py -w
```

### for unicode Keywords ('Россия') with type repositories
```bash
python3 github_crawler.py -u
```

## Output

### You can see [output.json](/src/config/output.json) After running these commands whatever you want to try above.
