# Remove UTF-8 BOM from JSON file
with open('keywords-data.json', 'r', encoding='utf-8-sig') as f:
    content = f.read()

with open('keywords-data.json', 'w', encoding='utf-8') as f:
    f.write(content)

print('UTF-8 BOM removed successfully')
