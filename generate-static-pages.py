import os

# 创建pages目录（如果不存在）
if not os.path.exists('pages'):
    os.makedirs('pages')

# 读取solutions.html模板
with open('solutions.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 手动定义关键词列表，基于之前的分析
keywords = [
    'real-estate-london', 'solar-texas', 'tax-california', 'wedding-nyc', 'mortgage-sydney',
    'airbnb-florida', 'fitness-la', 'business-toronto', 'crypto-miami', 'solar-queensland',
    'real-estate-manchester', 'tax-singapore', 'wedding-paris', 'solar-phoenix', 'crypto-dubai',
    'real-estate-austin', 'tax-portugal-nomad', 'real-estate-chicago', 'wedding-santorini', 'business-seattle',
    'real-estate-atlanta', 'solar-adelaide', 'wedding-maui', 'fitness-miami', 'business-berlin',
    'tax-houston-nomad', 'crypto-london-hmrc', 'real-estate-boston', 'solar-denver', 'wedding-rome',
    'real-estate-vancouver', 'solar-sydney', 'tax-london-freelance', 'wedding-bali', 'pet-health-sf',
    'amazon-fba-global', 'vanlife-oregon', 'dividend-investing-us', 'gaming-tokyo', 'golf-scotland',
    'tax-singapore-iras', 'business-berlin-esop', 'childcare-london-cost', 'tax-seattle-rsu', 'crypto-germany-hold',
    'real-estate-dallas-tax', 'solar-brisbane-roi', 'wedding-bali-villa', 'vanlife-australia-budget', 'rooftop-garden-nyc',
    'tax-toronto-dividend', 'baby-houston-pediatric', 'vaping-california-mix', 'gardening-atlanta-soil', 'sustainability-london-carbon',
    'dividend-uk-isa', 'backpacking-colorado-ultralight', 'rental-yield-dublin-rtb', 'mortgage-auckland-lvr', 'fitness-sydney-hydration',
    'keto', 'airbnb', 'saas', 'real-estate-london', 'tax-singapore',
    'business-berlin-esop', 'vanlife-australia-budget', 'solar-texas', 'tax-california', 'wedding-nyc',
    'airbnb-florida', 'wedding-santorini', 'crypto-dubai', 'tax-portugal-nomad', 'real-estate-austin',
    'tax-uk-cgt-crypto', 'solar-barcelona-grants', 'fitness-nyc-hiit', 'real-estate-calgary-ab', 'wedding-bali-uluwatu',
    'tax-seattle-amazon', 'real-estate-nashville-str', 'fitness-sydney-bondi', 'real-estate-perth-solar', 'tax-canada-ontario',
    'wedding-lasvegas-chapel', 'real-estate-brisbane-fhog', 'vanlife-portland-blm', 'garden-atlanta-clay', 'solar-phoenix-battery',
    'baby-houston-heat', 'wedding-santorini-curfew', 'real-estate-london-sdlt', 'tax-portugal-nhr', 'business-toronto-mars',
    'fitness-la-biohack', 'crypto-miami-305', 'real-estate-philly-abatement', 'tax-uk-isa-dividend', 'solar-barcelona-nextgen',
    'wedding-bali-banjar', 'tax-seattle-capitalgains', 'real-estate-brisbane-olympics', 'business-dublin-mnctax', 'coffee-barista-ratio',
    'golf-handicap-whs', 'backpacking-weight-calc', 'vape-juice-mixer', 'garden-soil-volume', 'tax-nomad-portugal',
    'real-estate-berlin-yield', 'solar-london-efficiency', 'wedding-bali-permit', 'tax-california-llc', 'baby-care-formula'
]

# 去重
unique_keywords = list(set(keywords))
print(f"Total unique keywords: {len(unique_keywords)}")

# 为每个关键词生成静态页面
for keyword in unique_keywords:
    # 构建页面内容
    page_content = template
    
    # 保存页面
    page_path = os.path.join('pages', f'{keyword}.html')
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(page_content)
    
    print(f"Generated: {page_path}")

print("All static pages generated successfully!")
