import glob, re, os

cn={'零':0,'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'百':100,'千':1000}
def cn2int(s):
    t=0;c=0
    for ch in s:
        if ch in ('十','百','千'):
            u=cn[ch]
            if u==10: c=c if c else 1; t+=c*10;c=0
            elif u==100: t+=c*100;c=0
            elif u==1000: t+=c*1000;c=0
        else: c=cn.get(ch,0)
    return t+c

# 内联 meta / 大纲旁白信号（作者直接对读者点评正文）
PATTERNS = [
    r'大爽点', r'中爽点', r'小爽点', r'爽点落', r'爽点在这', r'爽点打',
    r'这章', r'本章', r'本回', r'大高潮', r'中高潮', r'小高潮',
    r'作者按', r'写作注', r'注[:：]', r'PS[:：]',
]
pat = re.compile('|'.join(PATTERNS))

print("=== 全本内联 meta / 大纲旁白分布（跳过1-23锁定区）===")
hits_total = 0
flagged = []
for f in sorted(glob.glob('第*章.txt')):
    ch = cn2int(re.match(r'第(.+?)章', f).group(1))
    if ch <= 23: continue
    lines = open(f, encoding='utf-8').read().splitlines()
    ch_hits = []
    for i, l in enumerate(lines, 1):
        for m in pat.finditer(l):
            snippet = l.strip()[:60]
            ch_hits.append((i, m.group(0), snippet))
    if ch_hits:
        flagged.append((ch, f, ch_hits))
        hits_total += len(ch_hits)

for ch, f, ch_hits in flagged:
    tags = {}
    for _, kw, _ in ch_hits:
        tags[kw] = tags.get(kw, 0) + 1
    tagstr = ' '.join(f"{k}:{v}" for k, v in tags.items())
    print(f"\n第{ch}章 [{f}]  命中 {len(ch_hits)} 处 | {tagstr}")
    for i, kw, snip in ch_hits:
        print(f"   L{i} [{kw}] {snip}")

print(f"\n=== 合计：{len(flagged)} 章含内联meta，共 {hits_total} 处 ===")
