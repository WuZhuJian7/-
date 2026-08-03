import os, glob, re

base = "D:/WZJ/摸鱼：他们都以为我只是个写小说的/content"
cn = {'零':0,'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'百':100,'千':1000}
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

# meta / 成稿不纯净信号
META_PATTERNS = {
    '钩子标签': r'钩子[:：]',
    '上一章旁白': r'上一章',
    '下一章旁白': r'下一章',
    '作者注': r'(作者[注按]|:|：|PS|ps|注[:：])',
    '讲解感(说/道堆砌)': None,  # 后面单独算
}
rows = []
files = sorted(glob.glob(base + '/第*章.txt'))
for f in files:
    name = os.path.basename(f)
    m = re.match(r'第(.+?)章', name)
    ch = cn2int(m.group(1)) if m else -1
    txt = open(f, encoding='utf-8').read()
    lines = [l for l in txt.splitlines() if l.strip() and not l.startswith('#')]
    # 去掉章末标记
    body = txt.replace('——（%s 完）——' % name.replace('.txt',''), '')
    body_lines = [l for l in body.splitlines() if l.strip() and not l.startswith('#')]
    meta_hits = {}
    for label, pat in META_PATTERNS.items():
        if pat:
            meta_hits[label] = len(re.findall(pat, body))
    # 讲解感：连续"X说/Y说"对白且含"针法/规则/机制/系统/原理/设定"说明词
    explain_words = ['针法','规则是','机制是','原理','设定是','体系','框架是','逻辑是','也就是说','换言之','简单说','具体来说','所谓']
    ex_cnt = sum(body.count(w) for w in explain_words)
    meta_hits['讲解词数'] = ex_cnt
    rows.append((ch, name, meta_hits))

# 打印有 meta 标签或讲解词偏多的章（讲解词>6 视为偏说明）
print("=== 含 meta 标签 / 偏讲解 的章节 ===")
flagged = False
for ch, name, mh in rows:
    has_meta = any(mh[k] > 0 for k in ['钩子标签','上一章旁白','下一章旁白','作者注'])
    if has_meta or mh['讲解词数'] > 6:
        flagged = True
        print(f"第{ch:3d}章 | 钩子:{mh['钩子标签']} 上章:{mh['上一章旁白']} 下章:{mh['下一章旁白']} 作者注:{mh['作者注']} 讲解词:{mh['讲解词数']} | {name}")
if not flagged:
    print("（无）")
print()
print("=== 讲解词数 TOP15（偏说明风险）===")
for ch, name, mh in sorted(rows, key=lambda r:-r[2]['讲解词数'])[:15]:
    print(f"第{ch:3d}章 | 讲解词:{mh['讲解词数']:2d} | {name}")
