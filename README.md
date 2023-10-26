# Youdao Dictionary Exporter 

## Introduction

This project is a Python script that can export all the word entries from your Youdao dictionary. It helps you backup the dictionary data or export the data to other formats for further processing. Currently it only supports exporting to TXT format.

## Dependencies

```bash
pip install -r requirements.txt
```


## Usage 

1. Make sure you have logged in to your Youdao dictionary account in the browser, and copy the [cookie](./screens/cookie.png)

2. Run the script: `python export_youdao.py --cookie="your cookie"` 

3. The script will export all words to the `words.txt` file


Please follow the above instructions to use this script. If you have any issues during usage, feel free to submit an issue.