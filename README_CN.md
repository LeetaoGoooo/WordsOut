# 有道词典导出工具

## 介绍

这个项目是一个用 Python 写的脚本,可以导出有道词典中的单词本的所有词条。它可以帮助你备份词典数据,或者将数据导出到其他格式进行进一步处理，目前仅支持 TXT 格式。

## 用法

1. 确保你已经在浏览器中登录了有道词典账号,然后获取 [cookie](./screens/cookie.png) 复制下来

2. 运行脚本:`python export_youdao.py --cookie="你的cookie"`

3. 脚本会导出所有单词到 `words.txt` 文件


## 依赖

```bash
pip install -r requirements.txt
```

请根据上面的说明使用这个脚本。如果在使用过程中遇到任何问题,欢迎提交 issue。