import json

# 读取 keywords-data.json 文件
with open('keywords-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 为 niches 添加 industry_context
niches_context = {
    'keto': 'With the 2026 ketogenic diet guidelines emphasizing personalized macronutrient ratios, health professionals need precise calculation tools that account for individual metabolic variances, activity levels, and body composition metrics to optimize fat-burning efficiency and prevent nutritional deficiencies.',
    'airbnb': 'In 2026, short-term rental operators face complex revenue forecasting challenges due to dynamic pricing algorithms, fluctuating occupancy rates, and evolving local regulatory frameworks, requiring sophisticated ROI calculations that integrate seasonal demand patterns and operational expenses.',
    'saas': 'SaaS businesses in 2026 grapple with increasingly complex unit economics as customer acquisition costs rise and retention becomes paramount, necessitating precise LTV:CAC ratio calculations that factor in multi-year subscription cycles and expansion revenue opportunities.',
    'pet-health': 'Veterinary professionals in 2026 require advanced nutritional calculation tools that account for breed-specific dietary requirements, age-related metabolic changes, and emerging research on canine microbiome health to develop personalized feeding plans that optimize pet wellness.',
    'solar': 'Solar energy professionals in 2026 face the challenge of calculating accurate ROI projections amid evolving utility rate structures, incentive program changes, and battery storage economics, requiring sophisticated tools that model long-term energy production and grid interaction scenarios.',
    'freelance': 'Freelancers in 2026 navigate a complex tax landscape with changing self-employment tax regulations, healthcare costs, and retirement planning options, necessitating precise rate calculation tools that ensure sustainable income while accounting for business expenses and tax liabilities.',
    'wedding': 'Wedding planners in 2026 must manage increasingly complex budget allocations as vendor costs rise and client expectations evolve, requiring sophisticated calculation tools that balance venue expenses, catering costs, and service fees while maintaining event quality and guest experience.',
    'amazon-fba': 'Amazon FBA sellers in 2026 face intricate profit margin calculations due to fluctuating fulfillment fees, advertising costs, and global supply chain disruptions, requiring advanced tools that model product sourcing expenses, shipping logistics, and marketplace competition.',
    'crypto': 'Crypto investors in 2026 need sophisticated calculation tools to navigate volatile market conditions, tax implications of DeFi transactions, and portfolio diversification strategies, requiring real-time ROI analysis that accounts for gas fees, staking rewards, and cross-chain liquidity.',
    'gardening': 'Sustainable gardeners in 2026 require precise soil volume calculations that account for raised bed dimensions, organic matter content, and regional climate conditions, necessitating tools that optimize resource usage and maximize yield while minimizing environmental impact.',
    'baby-care': 'Pediatric professionals in 2026 face the challenge of developing personalized feeding schedules that account for individual growth patterns, digestive sensitivities, and developmental milestones, requiring calculation tools that balance nutritional needs with age-appropriate portion sizes.',
    'van-life': 'Van life enthusiasts in 2026 require sophisticated off-grid power calculations that account for increased energy demands from remote work equipment, climate control systems, and mobile entertainment, necessitating tools that optimize solar panel sizing and battery capacity for extended boondocking.',
    'coffee': 'Specialty coffee professionals in 2026 focus on precision brewing calculations that account for bean origin characteristics, roast profiles, and extraction variables, requiring tools that optimize water-to-coffee ratios and brew times for consistent flavor profiles across different brewing methods.',
    'gaming': 'Gaming enthusiasts in 2026 need accurate power consumption calculations to optimize PC builds for both performance and energy efficiency, accounting for next-gen hardware requirements, cooling systems, and regional electricity pricing to minimize operational costs.',
    'sustainability': 'Environmental professionals in 2026 require comprehensive carbon footprint calculations that account for scope 3 emissions, supply chain impacts, and emerging offset methodologies, necessitating tools that provide actionable insights for organizational decarbonization strategies.',
    'dividend': 'FIRE (Financial Independence Retire Early) enthusiasts in 2026 face complex dividend reinvestment calculations as interest rates fluctuate and market volatility increases, requiring tools that model long-term compounding effects and tax-efficient withdrawal strategies.',
    'golf': 'Golf professionals in 2026 need advanced handicap calculations that account for course difficulty variations, weather conditions, and player performance trends, requiring tools that provide actionable insights for game improvement and tournament preparation.',
    'vaping': 'Vape DIY enthusiasts in 2026 require precise e-liquid mixing calculations that balance nicotine strength, flavor profiles, and PG/VG ratios, necessitating tools that ensure consistent results while adhering to evolving regulatory standards for product safety.',
    'tax-side-hustle': 'Side hustle entrepreneurs in 2026 navigate complex tax calculations as gig economy regulations evolve, requiring tools that accurately estimate self-employment tax liabilities, deductible expenses, and quarterly payment schedules.',
    'backpacking': 'Ultralight backpackers in 2026 need precise pack weight calculations that balance essential gear requirements with weight optimization, accounting for seasonal variations, terrain challenges, and safety considerations for extended backcountry adventures.'
}

# 为 geo_niches 添加 industry_context
geo_niches_context = {
    'real-estate-london': 'London property investors in 2026 face complex rental yield calculations amid Brexit-related market fluctuations, increased stamp duty rates, and evolving tenant regulations, requiring tools that account for London-specific market dynamics and long-term capital growth projections.',
    'solar-texas': 'Texas homeowners in 2026 need sophisticated solar ROI calculations that account for the state\'s deregulated energy market, fluctuating utility rates, and evolving incentive programs, requiring tools that model system performance under Texas\' unique weather conditions and grid interactions.',
    'tax-california': 'California freelancers in 2026 navigate complex tax calculations with the state\'s progressive tax brackets, evolving gig economy regulations, and changing deduction rules, requiring tools that accurately estimate net take-home pay after accounting for federal and state tax liabilities.',
    'wedding-nyc': 'New York City wedding planners in 2026 face escalating venue costs, fluctuating vendor pricing, and complex budget allocations, requiring tools that account for Manhattan\'s premium market rates and seasonal demand variations to create realistic event budgets.',
    'mortgage-sydney': 'Sydney first-time homebuyers in 2026 need precise mortgage repayment calculations that account for Australia\'s variable interest rate environment, NSW stamp duty concessions, and evolving property market conditions, requiring tools that model long-term affordability scenarios.',
    'airbnb-florida': 'Florida vacation rental owners in 2026 navigate complex profitability calculations amid seasonal demand fluctuations, county-level tourist taxes, and evolving short-term rental regulations, requiring tools that account for Florida\'s unique market dynamics and hurricane season considerations.',
    'fitness-los-angeles': 'Los Angeles fitness enthusiasts in 2026 require personalized calorie and body fat calculations that account for the city\'s active lifestyle, diverse fitness trends, and year-round outdoor activity opportunities, necessitating tools that optimize performance while supporting sustainable health goals.',
    'business-toronto': 'Toronto tech startups in 2026 need precise runway calculations that account for Canada\'s payroll tax requirements, GTA office costs, and venture capital funding cycles, requiring tools that model burn rate scenarios and cash flow projections to ensure sustainable growth.',
    'solar-australia-queensland': 'Queensland homeowners in 2026 require sophisticated solar savings calculations that account for Australia\'s changing feed-in tariffs, system size limitations, and regional sun exposure variations, necessitating tools that optimize system design for maximum ROI in the Sunshine State.',
    'real-estate-manchester': 'Manchester property investors in 2026 face unique buy-to-let yield calculations amid the Northern Powerhouse economic initiatives, evolving rental regulations, and regional market growth patterns, requiring tools that model long-term investment performance in the UK\'s second city.',
    'tax-new-york-state': 'New York State residents in 2026 navigate complex tax calculations that combine state and city tax brackets, evolving deduction rules, and changing retirement contribution limits, requiring tools that accurately estimate net take-home pay across different income levels.',
    'wedding-chicago': 'Chicago wedding planners in 2026 need precise budget calculations that account for the Windy City\'s seasonal venue availability, fluctuating catering costs, and downtown premium pricing, requiring tools that optimize expense allocation while maintaining event quality.',
    'crypto-miami': 'Miami crypto traders in 2026 benefit from Florida\'s zero-state-tax environment but face complex profit calculations amid volatile market conditions, evolving regulatory frameworks, and cross-border transaction considerations, requiring tools that maximize tax advantages while ensuring compliance.',
    'real-estate-vancouver': 'Vancouver property investors in 2026 navigate complex ROI calculations that account for Canada\'s Empty Homes Tax, BC luxury tax, and evolving mortgage regulations, requiring tools that model long-term investment performance in one of North America\'s most expensive housing markets.',
    'solar-california-bay-area': 'Bay Area homeowners in 2026 require sophisticated solar ROI calculations that account for California\'s NEM 3.0 rules, battery storage economics, and PG&E rate structures, necessitating tools that optimize system design for maximum savings under the state\'s new net metering framework.',
    'health-denver': 'Denver outdoor enthusiasts in 2026 need altitude-adjusted calorie and hydration calculations that account for Colorado\'s high elevation, varying terrain, and seasonal weather conditions, requiring tools that optimize performance while ensuring safety during mountain activities.',
    'real-estate-austin': 'Austin property investors in 2026 face unique ROI calculations amid the city\'s rapid growth, evolving property tax rates, and competitive rental market, requiring tools that model long-term investment performance in the Silicon Hills tech hub.',
    'business-seattle': 'Seattle tech professionals in 2026 need precise cost-of-living calculations that account for Washington\'s zero-income-tax environment, high housing costs, and evolving benefit packages, requiring tools that compare job offers and optimize financial decisions in the Puget Sound region.',
    'wedding-toronto': 'Toronto wedding planners in 2026 navigate complex budget calculations that account for Ontario\'s 13% HST, fluctuating vendor pricing, and GTA venue availability, requiring tools that optimize expense allocation while ensuring compliance with Canadian tax regulations.',
    'mortgage-melbourne': 'Melbourne property investors in 2026 need precise calculations that account for Victoria\'s land tax changes, stamp duty rates, and evolving mortgage regulations, requiring tools that model long-term investment performance in Australia\'s cultural capital.'
}

# 为 long tail keywords 添加 industry_context
long_tail_context = {
    'real-estate-london': 'London landlords in 2026 require precise rental yield calculations that account for UK Stamp Duty Land Tax (SDLT) changes, evolving tenant regulations, and London\'s unique market dynamics, necessitating tools that model long-term investment performance across different boroughs.',
    'solar-texas': 'Texas solar adopters in 2026 need sophisticated ROI calculations that account for federal tax credits, state-specific incentives, and local utility buy-back rates, requiring tools that optimize system design for maximum savings in the Lone Star State.',
    'tax-california': 'California freelancers in 2026 navigate complex tax calculations with the state\'s progressive tax system, evolving gig economy regulations, and changing deduction rules, requiring tools that accurately estimate net income after accounting for all tax liabilities.',
    'wedding-nyc': 'NYC wedding planners in 2026 face escalating costs and complex budget allocations, requiring tools that account for Manhattan\'s premium venue rates, seasonal demand variations, and vendor pricing fluctuations to create realistic event budgets.',
    'mortgage-sydney': 'Sydney first-home buyers in 2026 need precise mortgage calculations that account for Australia\'s variable interest rates, NSW stamp duty concessions, and evolving property market conditions, requiring tools that model long-term affordability scenarios.',
    'airbnb-florida': 'Florida Airbnb hosts in 2026 navigate complex profitability calculations amid seasonal demand fluctuations, county-level tourist taxes, and evolving short-term rental regulations, requiring tools that optimize pricing strategies for maximum returns.',
    'fitness-la': 'Los Angeles fitness enthusiasts in 2026 require personalized body fat and calorie calculations that account for the city\'s active lifestyle, diverse fitness trends, and year-round outdoor activity opportunities, necessitating tools that support sustainable health goals.',
    'business-toronto': 'Toronto tech startups in 2026 need precise runway calculations that account for Canada\'s payroll tax requirements, GTA office costs, and venture capital funding cycles, requiring tools that model burn rate scenarios to ensure sustainable growth.',
    'crypto-miami': 'Miami crypto traders in 2026 benefit from Florida\'s zero-state-tax environment but face complex profit calculations amid volatile market conditions, requiring tools that maximize tax advantages while ensuring compliance with evolving regulations.',
    'solar-queensland': 'Queensland homeowners in 2026 require sophisticated solar savings calculations that account for Australia\'s changing feed-in tariffs, system size limitations, and regional sun exposure variations, necessitating tools that optimize system design for maximum ROI.',
    'real-estate-manchester': 'Manchester property investors in 2026 face unique buy-to-let yield calculations amid the Northern Powerhouse economic initiatives, evolving rental regulations, and regional market growth patterns, requiring tools that model long-term investment performance.',
    'wedding-chicago': 'Chicago wedding planners in 2026 need precise budget calculations that account for the city\'s seasonal venue availability, fluctuating catering costs, and downtown premium pricing, requiring tools that optimize expense allocation while maintaining event quality.',
    'real-estate-vancouver': 'Vancouver property investors in 2026 navigate complex ROI calculations that account for Canada\'s Empty Homes Tax, BC luxury tax, and evolving mortgage regulations, requiring tools that model long-term investment performance.',
    'business-seattle': 'Seattle tech professionals in 2026 need precise cost-of-living calculations that account for Washington\'s zero-income-tax environment, high housing costs, and evolving benefit packages, requiring tools that compare job offers and optimize financial decisions.',
    'fitness-denver': 'Denver outdoor enthusiasts in 2026 need altitude-adjusted calorie and hydration calculations that account for Colorado\'s high elevation, varying terrain, and seasonal weather conditions, requiring tools that optimize performance while ensuring safety.',
    'real-estate-austin': 'Austin property investors in 2026 face unique ROI calculations amid the city\'s rapid growth, evolving property tax rates, and competitive rental market, requiring tools that model long-term investment performance in the Silicon Hills.',
    'solar-bay-area': 'Bay Area homeowners in 2026 require sophisticated solar ROI calculations that account for California\'s NEM 3.0 rules, battery storage economics, and PG&E rate structures, necessitating tools that optimize system design for maximum savings.',
    'tax-nyc': 'NYC residents in 2026 navigate complex tax calculations that combine state and city tax brackets, evolving deduction rules, and changing retirement contribution limits, requiring tools that accurately estimate net take-home pay.',
    'wedding-toronto': 'Toronto wedding planners in 2026 navigate complex budget calculations that account for Ontario\'s 13% HST, fluctuating vendor pricing, and GTA venue availability, requiring tools that optimize expense allocation while ensuring compliance.',
    'mortgage-melbourne': 'Melbourne property investors in 2026 need precise calculations that account for Victoria\'s land tax changes, stamp duty rates, and evolving mortgage regulations, requiring tools that model long-term investment performance.',
    'crypto-dubai': 'Dubai crypto investors in 2026 benefit from the UAE\'s zero-tax environment but face complex profit calculations amid global market volatility, requiring tools that maximize tax advantages while ensuring compliance with international regulations.',
    'vanlife-portland': 'Pacific Northwest van lifers in 2026 require sophisticated budget and power calculations that account for regional fuel costs, campground fees, and off-grid energy needs, necessitating tools that optimize resources for extended road trips.',
    'freelance-berlin': 'Berlin freelancers in 2026 navigate complex tax calculations that account for Germany\'s KSK (Künstlersozialkasse) contributions, health insurance costs, and evolving freelance regulations, requiring tools that accurately estimate net income.',
    'coffee-seattle': 'Seattle coffee enthusiasts in 2026 require precise brewing calculations that account for bean origin characteristics, roast profiles, and extraction variables, necessitating tools that optimize water-to-coffee ratios for consistent flavor profiles.',
    'dividend-london': 'UK investors in 2026 need sophisticated ISA dividend reinvestment calculations that account for tax-free growth opportunities, evolving yield environments, and long-term compounding effects, requiring tools that maximize retirement savings.',
    'golf-scottsdale': 'Scottsdale golfers in 2026 need advanced handicap calculations that account for desert course conditions, elevation variations, and local rating systems, requiring tools that provide accurate performance metrics for tournament play.',
    'fba-shenzhen': 'Cross-border Amazon sellers in 2026 face complex profit margin calculations that account for international shipping costs, FBA fees, and currency fluctuations, requiring tools that optimize sourcing and pricing strategies for maximum returns.',
    'backpacking-colorado': 'Colorado trail hikers in 2026 need precise pack weight calculations that account for high-altitude conditions, seasonal weather variations, and trail difficulty levels, requiring tools that optimize gear selection for extended backcountry adventures.',
    'garden-atlanta': 'Atlanta gardeners in 2026 require precise soil volume calculations that account for Georgia\'s climate conditions, raised bed dimensions, and organic gardening practices, necessitating tools that optimize resource usage for maximum yield.',
    'baby-houston': 'Houston parents in 2026 need personalized baby formula and feeding calculations that account for the city\'s climate, pediatric guidelines, and individual growth patterns, requiring tools that support healthy infant development.'
}

# 更新 niches
for niche_id, context in niches_context.items():
    if niche_id in data['niches']:
        data['niches'][niche_id]['industry_context'] = context

# 更新 geo_niches
for niche in data['geo_niches']:
    niche_id = niche['id']
    if niche_id in geo_niches_context:
        niche['industry_context'] = geo_niches_context[niche_id]

# 更新 long tail keywords
for keyword_id, context in long_tail_context.items():
    if keyword_id in data['long tail keywords']:
        data['long tail keywords'][keyword_id]['industry_context'] = context

# 保存更新后的文件
with open('keywords-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('Successfully added industry_context to all entries in keywords-data.json')
