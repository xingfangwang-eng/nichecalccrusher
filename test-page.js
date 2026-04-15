// 测试脚本，模拟浏览器环境
const fs = require('fs');
const path = require('path');

// 读取JSON数据
const jsonData = JSON.parse(fs.readFileSync('keywords-data.json', 'utf-8'));

// 模拟getUrlParameter函数
function getUrlParameter(name) {
    return ''; // 模拟URL中没有id参数的情况
}

// 模拟window.location
const window = {
    location: {
        pathname: '/pages/real-estate-london.html'
    }
};

// 测试ID提取逻辑
let id = getUrlParameter('id');

// 如果URL中没有id参数，尝试从文件名中提取
if (!id) {
    const pathname = window.location.pathname;
    const filename = pathname.split('/').pop();
    if (filename) {
        id = filename.replace('.html', '');
    }
}

console.log(`Extracted ID: ${id}`);

// 测试数据加载逻辑
let keywordData = null;

// 检查niches
if (jsonData.niches && jsonData.niches[id]) {
    keywordData = jsonData.niches[id];
}

// 检查long_tail_solutions
if (!keywordData && jsonData.long_tail_solutions && jsonData.long_tail_solutions[id]) {
    keywordData = jsonData.long_tail_solutions[id];
}

// 检查根级数据
if (!keywordData && jsonData[id]) {
    keywordData = jsonData[id];
}

if (keywordData) {
    console.log('Data found:');
    console.log(`Title: ${keywordData.title}`);
    console.log(`Local Insight: ${keywordData.local_insight.substring(0, 100)}...`);
    console.log(`Step by Step Guide: ${keywordData.step_by_step_guide.length} steps`);
} else {
    console.log('No data found for ID:', id);
}
