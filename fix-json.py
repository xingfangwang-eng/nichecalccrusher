import json
import re

# 读取文件内容
with open('keywords-data.json', 'r', encoding='utf-8') as f:
    content = f.read()

# 清理文件内容，移除可能的多余字符
content = content.strip()

# 尝试修复JSON文件
try:
    # 尝试解析JSON
    data = json.loads(content)
    print("JSON is already valid!")
except json.JSONDecodeError as e:
    print(f"JSON error: {e}")
    
    # 尝试修复常见问题
    # 1. 检查是否有多余的逗号
    content = re.sub(r',\s*}', '}', content)
    content = re.sub(r',\s*\]', ']', content)
    
    # 2. 检查是否有未闭合的大括号
    open_braces = content.count('{')
    close_braces = content.count('}')
    print(f"Open braces: {open_braces}, Close braces: {close_braces}")
    
    if open_braces > close_braces:
        content += '}' * (open_braces - close_braces)
    elif close_braces > open_braces:
        content = content[:content.rindex('}')] * (close_braces - open_braces)
    
    # 3. 尝试再次解析
    try:
        data = json.loads(content)
        print("JSON fixed successfully!")
        # 保存修复后的文件
        with open('keywords-data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Fixed JSON saved to keywords-data.json")
    except json.JSONDecodeError as e2:
        print(f"Could not fix JSON: {e2}")
