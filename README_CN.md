# WordsOut

## 介绍

这个项目是一个用 Python 写的脚本,可以导出词典中的单词本的所有词条。它可以帮助你备份词典数据,或者将数据导出到其他格式进行进一步处理，目前仅支持 TXT 格式

## 计划

- [x] 有道词典
- [x] 扇贝单词
- [ ] 欧陆词典

## 用法

1. 确保你已经在浏览器中登录了有道词典/扇贝账号,然后获取 [cookie](./screens/cookie.png) 复制下来

2. 运行脚本:`python app.py --cookie="你的cookie" --platform="对应的平台"`

3. 脚本会导出所有单词到 `words.txt` 文件


## 依赖

```bash
pip install -r requirements.txt
```

请根据上面的说明使用这个脚本。如果在使用过程中遇到任何问题,欢迎提交 issue。


## 使用 GUI

从 release 页面下载

<image src="./screens/app-screen-shot.png" width="300"/><image src="./screens/app-screen-shot1.png" width="300"/>
