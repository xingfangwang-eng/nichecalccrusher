import json
import re

# 读取keywords-data.json文件
with open('keywords-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 收集所有关键词
keywords = []

# 添加根级别的关键词
for key in data:
    if key not in ['niches', 'long_tail_solutions']:
        keywords.append(key)

# 添加niches中的关键词
if 'niches' in data:
    for key in data['niches']:
        keywords.append(key)

# 添加long_tail_solutions中的关键词
if 'long_tail_solutions' in data:
    for key in data['long_tail_solutions']:
        keywords.append(key)

# 去重
unique_keywords = list(set(keywords))
print(f"Total unique keywords: {len(unique_keywords)}")

# 读取directory.html文件
with open('directory.html', 'r', encoding='utf-8') as f:
    directory_content = f.read()

# 检查每个关键词是否在directory.html中
missing_keywords = []
for keyword in unique_keywords:
    # 检查是否存在指向该关键词的链接
    if f'solutions.html?id={keyword}' not in directory_content and f'pages/{keyword}.html' not in directory_content:
        missing_keywords.append(keyword)

if missing_keywords:
    print(f"Missing keywords in directory.html: {len(missing_keywords)}")
    for keyword in missing_keywords:
        print(f"- {keyword}")
else:
    print("All keywords are already in directory.html")
