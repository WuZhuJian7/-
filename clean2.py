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

# 变体点评句（带逗号/破折号，前一轮漏删）
LABELS2 = [
    r'大爽点，落在陈默自己身上——',
    r'大爽点，落在陈默自己身上。',
    r'大爽点，落在陈默——',
]
pat = re.compile('|'.join(LABELS2))

total = 0
for f in sorted(glob.glob(base + '/第*章.txt')):
    ch = cn2int(re.match(r'第(.+?)章', os.path.basename(f)).group(1))
    if ch <= 23: continue
    lines = open(f, encoding='utf-8').read().splitlines()
    new = []; cnt = 0
    for l in lines:
        b = l
        l = pat.sub('', l)
        if l != b: cnt += 1
        new.append(l)
    if cnt:
        total += cnt
        open(f, 'w', encoding='utf-8').write('\n'.join(new))
        print(f"第{ch}章：删变体点评 {cnt} 处")
print(f"\n合计删除 {total} 处")
