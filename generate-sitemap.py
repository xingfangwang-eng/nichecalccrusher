import json
import os

# 读取 keywords-data.json 文件
with open('keywords-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取所有 id
ids = []

# 从 niches 中提取 id
if 'niches' in data:
    for niche_id in data['niches']:
        ids.append(niche_id)

# 从 geo_niches 中提取 id
if 'geo_niches' in data:
    for niche in data['geo_niches']:
        if 'id' in niche:
            ids.append(niche['id'])

# 从 long tail keywords 中提取 id
if 'long tail keywords' in data:
    for keyword_id in data['long tail keywords']:
        ids.append(keyword_id)

# 去重
ids = list(set(ids))

# 生成 sitemap.xml
xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

# 添加首页
xml_content += '''  <url>
    <loc>https://yourdomain.com/</loc>
    <lastmod>2026-04-15</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
'''

# 添加 solutions 页面
for niche_id in ids:
    xml_content += f'''
  <url>
    <loc>https://yourdomain.com/solutions.html?id={niche_id}</loc>
    <lastmod>2026-04-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
'''

xml_content += '''</urlset>'''

# 写入 sitemap.xml 文件
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(xml_content)

print(f'Generated sitemap.xml with {len(ids) + 1} URLs')
print('Sitemap generated successfully!')

# 生成索引列表 HTML
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NicheCalcCrusher | All Solutions</title>
    <meta name="description" content="Browse all custom calculator solutions for various niches and industries. Find the perfect calculator for your blog or website." />
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 24 24' fill='%2339FF14'%3E%3Cpath d='M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z'/%3E%3C/svg%3E" type="image/svg+xml">
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: #000000;
            color: #39FF14;
            font-family: 'JetBrains Mono', monospace;
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }

        /* 网格背景 */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(to right, rgba(57, 255, 20, 0.1) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(57, 255, 20, 0.1) 1px, transparent 1px);
            background-size: 20px 20px;
            pointer-events: none;
            z-index: 0;
        }

        .container {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 60px 20px;
            min-height: 100vh;
        }

        /* 标题样式 */
        .title {
            font-family: 'Press Start 2P', cursive;
            font-size: clamp(20px, 5vw, 30px);
            text-align: center;
            margin-bottom: 60px;
            color: #39FF14;
            text-shadow: 0 0 10px #39FF14, 0 0 20px #39FF14;
            animation: shake 0.5s ease-in-out infinite alternate;
            line-height: 1.5;
        }

        @keyframes shake {
            0% {
                transform: translateX(0);
            }
            100% {
                transform: translateX(2px) translateY(1px);
            }
        }

        /* 解决方案列表 */
        .solutions-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }

        .solution-card {
            background-color: rgba(0, 0, 0, 0.8);
            border: 1px solid #39FF14;
            border-radius: 5px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(57, 255, 20, 0.3);
            transition: all 0.3s ease;
        }

        .solution-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 0 25px rgba(57, 255, 20, 0.5);
        }

        .solution-card h3 {
            font-family: 'Press Start 2P', cursive;
            font-size: 14px;
            margin-bottom: 10px;
            color: #39FF14;
        }

        .solution-card p {
            font-size: 14px;
            line-height: 1.5;
            margin-bottom: 15px;
        }

        .solution-card a {
            color: #39FF14;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease;
        }

        .solution-card a:hover {
            color: #8A2BE2;
            text-decoration: underline;
        }

        /* 回到首页链接 */
        .back-link {
            display: block;
            text-align: center;
            margin-top: 40px;
            color: #39FF14;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease;
        }

        .back-link:hover {
            color: #8A2BE2;
        }

        /* 响应式设计 */
        @media (max-width: 768px) {
            .container {
                padding: 40px 15px;
            }

            .title {
                font-size: 18px;
                margin-bottom: 40px;
            }

            .solutions-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">ALL SOLUTIONS</h1>
        
        <div class="solutions-grid">
'''

# 添加解决方案卡片
for niche_id in ids:
    # 尝试从不同部分获取数据
    niche_data = None
    if 'niches' in data and niche_id in data['niches']:
        niche_data = data['niches'][niche_id]
    elif 'geo_niches' in data:
        for niche in data['geo_niches']:
            if niche.get('id') == niche_id:
                niche_data = niche
                break
    elif 'long tail keywords' in data and niche_id in data['long tail keywords']:
        niche_data = data['long tail keywords'][niche_id]
    
    if niche_data:
        title = niche_data.get('title', 'Custom Calculator')
        description = niche_data.get('seo_description', 'Create your custom calculator')
        index_html += f'''
            <div class="solution-card">
                <h3>{title}</h3>
                <p>{description[:100]}...</p>
                <a href="solutions.html?id={niche_id}">View Solution</a>
            </div>
'''

index_html += '''
        </div>
        
        <a href="index.html" class="back-link">← Back to Home</a>
    </div>
</body>
</html>'''

# 写入 index-all.html 文件
with open('index-all.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print('Generated index-all.html with all solutions')
print('Index file generated successfully!')
