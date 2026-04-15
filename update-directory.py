import json

# 读取keywords-data.json文件
with open('keywords-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 收集所有关键词及其数据
all_keywords = {}

# 添加根级别的关键词
for key in data:
    if key not in ['niches', 'long_tail_solutions']:
        all_keywords[key] = data[key]

# 添加niches中的关键词
if 'niches' in data:
    for key in data['niches']:
        all_keywords[key] = data['niches'][key]

# 添加long_tail_solutions中的关键词
if 'long_tail_solutions' in data:
    for key in data['long_tail_solutions']:
        all_keywords[key] = data['long_tail_solutions'][key]

# 读取directory.html文件
with open('directory.html', 'r', encoding='utf-8') as f:
    directory_content = f.read()

# 检查每个关键词是否在directory.html中
missing_keywords = []
for keyword in all_keywords:
    # 检查是否存在指向该关键词的链接
    if f'solutions.html?id={keyword}' not in directory_content and f'pages/{keyword}.html' not in directory_content:
        missing_keywords.append(keyword)

print(f"Total keywords: {len(all_keywords)}")
print(f"Missing keywords: {len(missing_keywords)}")

# 为每个缺失的关键词生成HTML
for keyword in missing_keywords:
    keyword_data = all_keywords[keyword]
    title = keyword_data.get('title', keyword.replace('-', ' ').title())
    
    # 确定关键词的类别
    category = "Other"
    subcategory = "Other"
    
    # 基于关键词的前缀确定类别
    if 'real-estate' in keyword or 'property' in keyword or 'mortgage' in keyword or 'rental' in keyword:
        category = "Real Estate & Property"
    elif 'tax' in keyword or 'finance' in keyword or 'dividend' in keyword:
        category = "Tax & Finance"
    elif 'solar' in keyword:
        category = "Solar & Energy"
    elif 'wedding' in keyword:
        category = "Wedding & Events"
    elif 'crypto' in keyword:
        category = "Crypto & Blockchain"
    elif 'fitness' in keyword:
        category = "Fitness & Health"
    elif 'business' in keyword:
        category = "Business & Entrepreneurship"
    elif 'vanlife' in keyword or 'backpacking' in keyword:
        category = "Travel & Lifestyle"
    elif 'gaming' in keyword:
        category = "Gaming & Entertainment"
    elif 'vaping' in keyword:
        category = "Vaping & Lifestyle"
    elif 'gardening' in keyword:
        category = "Gardening & Home"
    elif 'rooftop' in keyword:
        category = "Sustainability & Green Living"
    elif 'sustainability' in keyword:
        category = "Sustainability & Green Living"
    elif 'pet' in keyword:
        category = "Pet Care"
    elif 'golf' in keyword:
        category = "Sports & Recreation"
    elif 'childcare' in keyword or 'baby' in keyword:
        category = "Family & Parenting"
    elif 'amazon' in keyword:
        category = "E-Commerce & Retail"
    
    # 生成HTML
    html = f'''            <div class="grid-item">
                <h3>{title}</h3>
                <a href="pages/{keyword}.html">View Calculator</a>
            </div>'''
    
    # 找到类别所在的位置并插入HTML
    # 首先找到对应的类别标题
    category_pattern = f'<h3 class="subcategory-title">{category}</h3>'
    if category_pattern in directory_content:
        # 找到类别标题后的grid-container
        start_idx = directory_content.find(category_pattern)
        grid_start = directory_content.find('<div class="grid-container">', start_idx)
        grid_end = directory_content.find('</div>', grid_start) + 6
        
        # 在grid-container的结束标签前插入HTML
        directory_content = directory_content[:grid_end] + '\n' + html + directory_content[grid_end:]
    else:
        # 如果类别不存在，创建新的类别
        # 找到"BY INDUSTRY"标题
        by_industry_idx = directory_content.find('<!-- 按行业分类 -->')
        industry_title_idx = directory_content.find('<h2 class="category-title">BY INDUSTRY</h2>', by_industry_idx)
        
        # 找到下一个类别标题或"BY GEOGRAPHY"标题
        next_title_idx = directory_content.find('<h3 class="subcategory-title">', industry_title_idx + 1)
        if next_title_idx == -1:
            next_title_idx = directory_content.find('<!-- 按地理位置分类 -->', industry_title_idx)
        
        # 在适当的位置插入新类别
        new_category_html = f'''
        <h3 class="subcategory-title">{category}</h3>
        <div class="grid-container">
{html}
        </div>'''
        
        directory_content = directory_content[:next_title_idx] + new_category_html + directory_content[next_title_idx:]

# 保存更新后的directory.html文件
with open('directory.html', 'w', encoding='utf-8') as f:
    f.write(directory_content)

print("directory.html has been updated with all missing keywords")
