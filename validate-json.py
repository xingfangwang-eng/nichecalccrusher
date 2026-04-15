import json

# 读取keywords-data.json文件并验证语法
try:
    with open('keywords-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("JSON file is valid!")
    print(f"Total root keys: {len(data)}")
    if 'niches' in data:
        print(f"Niches count: {len(data['niches'])}")
    if 'long_tail_solutions' in data:
        print(f"Long tail solutions count: {len(data['long_tail_solutions'])}")
except json.JSONDecodeError as e:
    print(f"JSON syntax error: {e}")
    # 尝试定位错误位置
    with open('keywords-data.json', 'r', encoding='utf-8') as f:
        content = f.read()
        error_pos = e.pos
        # 打印错误位置前后的内容
        start = max(0, error_pos - 100)
        end = min(len(content), error_pos + 100)
        print(f"Error context:\n{content[start:end]}")
