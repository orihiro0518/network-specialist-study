from pathlib import Path
import re, json

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Basic metadata
s=re.sub(r'<title>.*?</title>', '<title>ネットワークスペシャリスト（ネスペ）無料問題集500問｜午後対策・IPA過去問｜ORIVECTOR</title>', s, count=1, flags=re.S)
s=re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="ネットワークスペシャリスト試験（ネスペ）を無料で対策。午前II風500問、午後問題100題、IPA公式過去問150問、基礎12テーマ、苦手復習を1サイトに収録。独学・午後対策・過去問演習に。">', s, count=1)
s=re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="index,follow,max-image-preview:large">', s, count=1)
s=re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="ネットワークスペシャリスト（ネスペ）無料問題集500問｜ORIVECTOR">', s, count=1)
s=re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="午前II風500問・午後100題・IPA公式過去問150問・基礎12テーマでネスペを無料対策。">', s, count=1)
if '<meta property="og:site_name"' not in s:
    s=s.replace('<meta property="og:type" content="website">','<meta property="og:type" content="website">\n<meta property="og:site_name" content="ORIVECTOR">\n<meta property="og:locale" content="ja_JP">',1)
if '<meta name="twitter:title"' not in s:
    s=s.replace('<meta name="twitter:card" content="summary">','<meta name="twitter:card" content="summary">\n<meta name="twitter:title" content="ネットワークスペシャリスト（ネスペ）無料問題集500問｜ORIVECTOR">\n<meta name="twitter:description" content="午前II風500問・午後100題・IPA公式過去問150問でネスペを無料対策。">',1)

schema={
 '@context':'https://schema.org',
 '@graph':[
  {'@type':'Organization','@id':'https://orivector.jp/#organization','name':'ORIVECTOR','url':'https://orivector.jp/'},
  {'@type':'WebSite','@id':'https://orivector.jp/#website','url':'https://orivector.jp/','name':'ORIVECTOR','publisher':{'@id':'https://orivector.jp/#organization'},'inLanguage':'ja'},
  {'@type':['WebApplication','LearningResource'],'@id':'https://orivector.jp/network-specialist-study/#app','name':'ネットワークスペシャリスト（ネスペ）無料問題集500問','url':'https://orivector.jp/network-specialist-study/','description':'ネットワークスペシャリスト試験対策の無料学習サイト。午前II風500問、午後問題100題、IPA公式過去問150問、基礎12テーマ、苦手復習に対応。','applicationCategory':'EducationalApplication','operatingSystem':'Web','isAccessibleForFree':True,'educationalUse':'試験対策','learningResourceType':['問題集','過去問','午後問題対策','学習ガイド'],'inLanguage':'ja','publisher':{'@id':'https://orivector.jp/#organization'}},
  {'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'ORIVECTOR','item':'https://orivector.jp/'},{'@type':'ListItem','position':2,'name':'ネットワークスペシャリスト試験対策','item':'https://orivector.jp/network-specialist-study/'}]},
  {'@type':'FAQPage','mainEntity':[
    {'@type':'Question','name':'ネットワークスペシャリスト試験対策の問題は何問ありますか？','acceptedAnswer':{'@type':'Answer','text':'午前II風500問、午後問題100題、IPA公式午前II過去問150問を収録しています。'}},
    {'@type':'Question','name':'午後問題の対策もできますか？','acceptedAnswer':{'@type':'Answer','text':'構成図、障害原因、設計意図を読み取る午後問題100題で記述対策ができます。'}},
    {'@type':'Question','name':'IPA公式の過去問も解けますか？','acceptedAnswer':{'@type':'Answer','text':'令和元年度から令和7年度までのIPA公式午前II過去問を年度別に演習できます。'}}
  ]}
 ]
}
s=re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False,separators=(',',':'))+'</script>', s, count=1, flags=re.S)

# H1 and hero copy
s=s.replace('<h1>ネットワークスペシャリスト<br>試験対策</h1>','<h1>ネットワークスペシャリスト（ネスペ）<br>無料問題集・試験対策</h1>')
s=s.replace('午前II風500問・午後問題100題・基礎学習を1つに。問題を解くだけでなく、「なぜそうなるか」まで理解してネスペ合格を目指します。','午前II風500問・午後問題100題・IPA公式過去問150問・基礎12テーマを1つに。ネットワークスペシャリスト試験を、問題演習と仕組みの理解の両方から対策できます。')

# Static SEO content visible to crawlers/users
seo='''\n<section class="card" id="seo-guide" style="margin-top:22px">\n  <h2>ネットワークスペシャリスト試験を無料で対策</h2>\n  <p>ORIVECTORでは、ネットワークスペシャリスト試験（ネスペ）の午前II・午後をまとめて学習できます。TCP/IP、VLAN、STP、OSPF、BGP、DNS、VPN、セキュリティなどの基礎を確認したあと、問題演習とIPA公式過去問で知識を定着させます。</p>\n  <div class="topics" style="margin-top:14px">\n    <div class="card"><h3>午前II対策</h3><p>午前II風500問から、苦手カテゴリを選んで10問・20問・全問題を演習できます。</p></div>\n    <div class="card"><h3>午後問題対策</h3><p>構成図・障害原因・設計意図を読み解く100題で、記述式問題に必要な考え方を練習できます。</p></div>\n    <div class="card"><h3>IPA公式過去問</h3><p>令和元年度〜令和7年度の公式午前II過去問を年度別に演習できます。</p></div>\n  </div>\n</section>\n<section class="card" id="faq" style="margin-top:22px">\n  <h2>ネットワークスペシャリスト試験対策 FAQ</h2>\n  <h3>問題は何問収録されていますか？</h3><p>午前II風500問、午後問題100題、IPA公式午前II過去問150問を収録しています。</p>\n  <h3>午後問題も対策できますか？</h3><p>構成図・障害原因・設計意図を読み取る午後問題100題で対策できます。</p>\n  <h3>スマホでも利用できますか？</h3><p>ブラウザで動作するため、スマートフォンからも学習できます。</p>\n</section>\n'''
needle='  <div class="sectionTitle"><h2>今日のおすすめ</h2>'
if 'id="seo-guide"' not in s and needle in s:
    pos=s.find(needle)
    # insert before today's recommendation block, still home view
    s=s[:pos]+seo+s[pos:]

p.write_text(s,encoding='utf-8')

Path('robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://orivector.jp/network-specialist-study/sitemap.xml\n',encoding='utf-8')
Path('sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://orivector.jp/network-specialist-study/</loc></url>\n</urlset>\n',encoding='utf-8')

# self-cleanup files are removed by workflow after running
print('SEO update applied')
