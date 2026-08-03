import glob, re, os

base = "D:/WZJ/摸鱼：他们都以为我只是个写小说的/content"
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

# 作者大纲旁白标签（必须删，保留其后对话内容）
LABELS = [
    r'大爽点（大高潮）落在这章：',
    r'大爽点落在这章：',
    r'大爽点落在他身上：',
    r'大爽点落在第三天。',
    r'中打脸落在这章：',
    r'小打脸落在这章：',
    r'大高潮落在这章：',
    r'大高潮落在他身上——',
    r'大高潮来了——',
    r'大高潮，来了。',
    r'大高潮来了。',
]
pat = re.compile('|'.join(LABELS))

total = 0
for f in sorted(glob.glob(base + '/第*章.txt')):
    ch = cn2int(re.match(r'第(.+?)章', os.path.basename(f)).group(1))
    if ch <= 23: continue
    lines = open(f, encoding='utf-8').read().splitlines()
    new = []
    cnt = 0
    for l in lines:
        if l.startswith('#'):   # 章名行不动（如 186 章名含"大高潮"）
            new.append(l); continue
        before = l
        l = pat.sub('', l)
        if l != before:
            cnt += 1
        new.append(l)
    if cnt:
        total += cnt
        open(f, 'w', encoding='utf-8').write('\n'.join(new))
        print(f"第{ch}章：删标签 {cnt} 处")
print(f"\n合计删除标签 {total} 处")
