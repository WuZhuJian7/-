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

# 目标：我上一轮重写、带 meta 的章（均非 1-23 锁定区）
names = ['第一百三十六章','第一百三十七章','第一百三十八章','第一百三十九章','第一百四十章',
         '第一百四十一章','第一百四十二章','第一百四十三章','第一百四十四章','第一百四十五章',
         '第一百四十六章','第一百四十七章','第一百四十八章','第一百四十九章','第一百五十章','第一百七十五章']

for name in names:
    f = os.path.join(base, name + '.txt')
    if not os.path.exists(f):
        print('MISS', name); continue
    lines = open(f, encoding='utf-8').read().splitlines()
    out = []
    deleted_hook = 0
    for l in lines:
        # 1) 删除独立成行的钩子标签
        if re.match(r'\s*钩子[:：]', l):
            deleted_hook += 1
            continue
        out.append(l)
    text = '\n'.join(out)
    # 2) 清除"上一章...，这章"回顾旁白（保留推进部分的实质信息）
    text = re.sub(r'上一章[^。]*?，这章', '', text)
    # 3) 清除"下一章起/下一章，/下一章"引导词（保留后续叙述）
    text = re.sub(r'下一章[起，]?', '', text)
    open(f, 'w', encoding='utf-8').write(text)
    print(f"{name}: 删钩子行={deleted_hook}")
print("DONE")
