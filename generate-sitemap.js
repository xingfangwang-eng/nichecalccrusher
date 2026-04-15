const fs = require('fs');

// 读取 keywords-data.json 文件
fs.readFile('keywords-data.json', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading keywords-data.json:', err);
        return;
    }

    try {
        // 解析 JSON 数据
        const keywordData = JSON.parse(data);
        
        // 收集所有 ID
        const ids = [];
        
        // 从 niches 中提取 ID
        if (keywordData.niches) {
            for (const nicheId in keywordData.niches) {
                ids.push(nicheId);
            }
        }
        
        // 从 long_tail_solutions 中提取 ID
        if (keywordData.long_tail_solutions) {
            for (const solutionId in keywordData.long_tail_solutions) {
                ids.push(solutionId);
            }
        }
        
        // 去重
        const uniqueIds = [...new Set(ids)];
        
        // 生成 sitemap.xml 内容
        let sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
`;
        
        // 添加首页
        sitemapContent += `  <url>
    <loc>https://yourdomain.com/</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
`;
        
        // 添加 directory.html
        sitemapContent += `  <url>
    <loc>https://yourdomain.com/directory.html</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
`;
        
        // 添加所有解决方案页面
        uniqueIds.forEach(id => {
            sitemapContent += `  <url>
    <loc>https://yourdomain.com/solutions.html?id=${id}</loc>
    <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
`;
        });
        
        sitemapContent += `</urlset>`;
        
        // 写入 sitemap.xml 文件
        fs.writeFile('sitemap.xml', sitemapContent, (err) => {
            if (err) {
                console.error('Error writing sitemap.xml:', err);
                return;
            }
            console.log('sitemap.xml generated successfully!');
            console.log(`Added ${uniqueIds.length} solution pages to sitemap.`);
        });
        
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});
