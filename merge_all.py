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

files = []
for f in glob.glob(base + '/第*章.txt'):
    name = os.path.basename(f)
    m = re.match(r'第(.+?)章', name)
    ch = cn2int(m.group(1)) if m else -1
    files.append((ch, f))
files.sort()

out_path = os.path.join(base, '《摸鱼：我的小说首富成真了》全本.txt')
with open(out_path, 'w', encoding='utf-8') as out:
    for ch, f in files:
        txt = open(f, encoding='utf-8').read().strip()
        if ch != files[0][0]:
            out.write('\n\n')
        out.write(txt)

total = sum(len(open(f, encoding='utf-8').read()) for _, f in files)
print(f"合并完成：{len(files)} 章，输出 {out_path}")
print(f"总字符数（含标点）：{total}")
print(f"首章：{os.path.basename(files[0][1])}  尾章：{os.path.basename(files[-1][1])}")
