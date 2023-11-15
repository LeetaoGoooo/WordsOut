# WordsOut

## Introduction

This project is a Python script that can export all the word entries from your dictionary. It helps you backup the dictionary data or export the data to other formats for further processing. Currently it only supports exporting to TXT format

## Plan

- [x] Youdao
- [x] Shanbay
- [ ] Eudic

## Dependencies

```bash
pip install -r requirements.txt
```

## Usage 

### Run source code

1. Make sure you have logged in to your Youdao/Shanbay dictionary account in the browser, and copy the [cookie](./screens/cookie.png)

2. Run the script: `python app.py --cookie="your cookie" --platform="corresponding platform"` 

3. The script will export all words to the `words.txt` file

Please follow the above instructions to use this script. If you have any issues during usage, feel free to submit an issue.

## Use GUI

download from release page

<image src="./screens/app-screen-shot.png" width="300"/><image src="./screens/app-screen-shot1.png" width="300"/>
