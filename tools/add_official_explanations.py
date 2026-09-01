from pathlib import Path
import json,re
p=Path('index.html'); s=p.read_text(encoding='utf-8')
E=[
('呼量（アーラン）','1台あたり1時間20呼、180台で3,600呼。80秒×3,600÷3,600秒=80アーラン。','時間単位をそろえる。'),
('Ethernetフレーム長','データ1,400に宛先MAC6、送信元MAC6、タイプ/長さ2、FCS4を加え、1,418オクテット。','何をフレーム長に含めるか確認。'),
('ビット誤り率','200,000バイト=1,600,000ビット。10^-5を掛けると平均16ビットの誤り。','バイト→ビットは×8。'),
('10GBASE-T / Cat6A','Cat6Aを用いる10GBASE-Tは最大100m。Cat6では条件により55m程度。','-Tはツイストペア。'),
('CoAP','IoTなど制約の大きい機器向けの軽量REST型プロトコルで、一般にUDPを利用。','CoAP=IoT・軽量・UDP。'),
('HTTP GET / POST','GETは主に取得、POSTはデータ送信や処理開始。GETは安全・べき等として扱われる。','GET=取得、POST=登録/処理。'),
('IPヘッダとICMP','IPv4ではProtocolフィールドで上位プロトコルを識別し、ICMPは番号1。','TCP/UDPのポート番号と混同しない。'),
('サブネットアドレス','IPアドレスとサブネットマスクのAND演算でネットワークアドレスを求める。','ホスト部を0にする。'),
('PPP','ポイントツーポイント向け。LCPでリンク確立、NCPでネットワーク層設定、PAP/CHAPで認証。','PPP=LCP/NCP/PAP/CHAP。'),
('UDPを使うルーティング','RIPはUDP 520。BGPはTCP 179、OSPFはIPプロトコル89。','RIP=UDP520、BGP=TCP179。'),
('TCP 3ウェイハンドシェイク','接続確立はSYN→SYN/ACK→ACK。双方の初期シーケンス番号を確認する。','切断時のFINも関連。'),
('ICMPv6近隣探索','IPv6ではARPの代わりにNDPを利用。NS/NAで近隣ノード情報を確認する。','IPv6ではARPではなくNDP。'),
('OpenFlow','フロー未登録時はPacket-Inでコントローラへ通知し、Flow-Modなどでルールを追加する。','SDN=制御と転送の分離。'),
('FTPコマンド','RETRは取得、STORは送信、LISTは一覧取得。制御用とデータ用で別コネクションを使う。','アクティブ/パッシブも頻出。'),
('無線LAN周波数帯','2.4GHzは到達性が高いが干渉が多く、5GHzは利用可能チャネルが多い。Wi-Fi 6Eは6GHzも利用。','規格と周波数帯を表で整理。'),
('TLS','通信の機密性・完全性・相手認証を提供。ハンドシェイク後にアプリデータを保護する。','HTTPS=HTTP over TLS。'),
('テンペスト攻撃','機器から漏れる電磁波などを観測して情報を推測する。対策は電磁シールドなど。','電磁的漏えいがキーワード。'),
('DRDoS','第三者のリフレクタへ送信元IPを被害者に偽装して要求し、増幅応答を集中させる。','反射+増幅。'),
('無線LANセキュリティ','WPA2/WPA3や802.1X/EAPを利用し、WEPやSSID非公開だけに依存しない。','WEPは脆弱。'),
('DNSSEC','DNS応答の真正性・完全性を電子署名で検証する。通信経路の暗号化ではない。','DNSSEC=署名、DoH/DoT=暗号化。'),
('OP25B','外向きTCP/25を制限して迷惑メール送信を抑止。正規投稿は587などを使う。','25=SMTPサーバ間、587=投稿。'),
('キャッシュメモリ','ライトスルーは主記憶へ同時書込み、ライトバックは後で主記憶へ反映。','整合性と性能の違いを整理。'),
('MTTR','平均修復時間。監視、ログ、交換容易な構成、手順標準化などで短縮できる。','MTTR短縮で可用性向上。'),
('ブローカー','要求側と提供側の間でサービスを仲介し、疎結合化や位置透過を実現する。','仲介・疎結合。'),
('ステージング環境','本番公開前に本番に近い条件で最終確認する環境。リリース手順や設定差異も確認する。','開発→テスト→ステージング→本番。')]
arr=[{'topic':a,'body':b,'tip':c} for a,b,c in E]
marker='// ORIVECTOR_OFFICIAL_EXPLANATIONS_V1'
if marker not in s:
    s=s.replace('const officialPastAnswers=',marker+'\nconst officialPastExplanations='+json.dumps({'r7':arr},ensure_ascii=False)+';\nconst officialPastAnswers=',1)
old='''  result.innerHTML=choice===correct\n    ? `<b style=\\"color:var(--ok)\\">⭕ 正解！</b><p>正解は「${correct}」です。</p>`\n    : `<b style=\\"color:var(--ng)\\">❌ 不正解</b><p>正解は「${correct}」です。</p>`;'''
new='''  const ex=officialPastExplanations?.[officialPastYear]?.[officialQuestionIndex];\n  const base=choice===correct ? `<b style="color:var(--ok)">⭕ 正解！</b><p>正解は「${correct}」です。</p>` : `<b style="color:var(--ng)">❌ 不正解</b><p>正解は「${correct}」です。</p>`;\n  result.innerHTML=base+(ex ? `<div class="officialDetailExplain"><h4>📘 ORIVECTOR解説：${ex.topic}</h4><p>${ex.body}</p><div class="examtip"><b>試験ポイント：</b> ${ex.tip}</div></div>` : `<div class="officialDetailExplain"><h4>📘 解説</h4><p>この年度の詳細解説は順次追加中です。</p></div>`);'''
if old in s: s=s.replace(old,new,1)
else:
    s=re.sub(r'  result\.innerHTML=choice===correct[\s\S]*?`;',new,s,count=1)
if '.officialDetailExplain{' not in s:
    s=s.replace('</style>','.officialDetailExplain{margin-top:14px;padding-top:12px;border-top:1px solid var(--line)}\n.officialDetailExplain h4{margin:0 0 8px;color:var(--accent)}\n.officialDetailExplain p{line-height:1.75}\n</style>',1)
s=s.replace('Ver 2.7.1','Ver 2.8.0')
p.write_text(s,encoding='utf-8')
# SEO解説ページ
answers=['エ','イ','エ','イ','エ','イ','ア','ウ','エ','エ','ア','ア','ウ','ウ','ウ','ウ','イ','ウ','エ','イ','イ','イ','ア','エ','エ']
out=Path('past-explanations/r7');out.mkdir(parents=True,exist_ok=True)
cards=''.join(f'<section class="card"><h2>問{i}：{e[0]}</h2><p><b>正解：{answers[i-1]}</b></p><p>{e[1]}</p><div class="tip"><b>試験ポイント：</b>{e[2]}</div></section>' for i,e in enumerate(E,1))
html='''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>令和7年度 ネットワークスペシャリスト午前II 過去問25問解説｜ORIVECTOR</title><meta name="description" content="令和7年度春期ネットワークスペシャリスト午前II 25問の要点解説。"><link rel="canonical" href="https://orivector.jp/network-specialist-study/past-explanations/r7/"><meta name="robots" content="index,follow"><style>body{margin:0;background:#08111f;color:#edf4ff;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.wrap{max-width:900px;margin:auto;padding:24px 16px 60px}a{color:#61dafb}.lead{color:#aebed2;line-height:1.8}.card{background:#101b2c;border:1px solid #213651;border-radius:16px;padding:18px;margin:14px 0}.card h2{font-size:19px}.card p{line-height:1.75}.tip{background:#0a1728;border-left:4px solid #61dafb;padding:11px}</style></head><body><main class="wrap"><p><a href="../../">← ネスペ問題集へ</a></p><h1>令和7年度 ネットワークスペシャリスト 午前II 過去問解説</h1><p class="lead">公式問題を解いた後の復習用に、25問の核心をORIVECTOR独自の言葉で整理しています。</p>'''+cards+'''</main></body></html>'''
(out/'index.html').write_text(html,encoding='utf-8')
sm=Path('sitemap.xml')
if sm.exists():
    x=sm.read_text(encoding='utf-8');u='<url><loc>https://orivector.jp/network-specialist-study/past-explanations/r7/</loc></url>'
    if u not in x: sm.write_text(x.replace('</urlset>',u+'\n</urlset>'),encoding='utf-8')
