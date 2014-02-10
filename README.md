Xenu Analyzer (python)
=============

Although [Xenu's Link Sleuth](http://home.snafu.de/tilman/xenulink.html) is a very cool link checker, understanding their output .html is not.  This tool will help you extract the data you need for checking link errors.

## Requirements
- Python 2.7

## Usage

Run 
```
python xenu-analyzer.py input.html
```

It will generate three files you'll probably need:

- valid_urls_for_searchengines.txt  
- broken_links.txt
- redirected_urls.txt

