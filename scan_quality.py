import os, glob, re

base = "D:/WZJ/摸鱼：他们都以为我只是个写小说的/content"
cn = {'零':0,'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,
      '七':7,'八':8,'九':9,'十':10,'百':100,'千':1000}
def cn2int(s):
    t=0; c=0
    for ch in s:
        if ch in ('十','百','千'):
            u = cn[ch]
            if u == 10:
                c = c if c else 1; t += c*10; c = 0
            elif u == 100:
                t += c*100; c = 0
            elif u == 1000:
                t += c*1000; c = 0
        else:
            c = cn.get(ch, 0)
    return t + c

QUOTES = ('"', '“', '”', '「', '」', "'", '‘', '’')
inner = ['他想','心里','暗想','琢磨','盘算','思忖','默念','心想','脑海中',
         '脑子里','他寻思','思付','内心','在心里','他脑中','默想','他思','寻思',
         '他琢磨','他盘算','他暗想']

rows = []
for f in glob.glob(base + '/第*章.txt'):
    m = re.match(r'第(.+?)章', os.path.basename(f))
    if not m: continue
    ch = cn2int(m.group(1))
    lines = open(f, encoding='utf-8').read().split('\n')
    body = [l for l in lines if l.strip() and not l.strip().startswith('#')
            and '——（第' not in l]
    n = len(body)
    if n == 0: continue
    qline = sum(1 for l in body if any(q in l for q in QUOTES))
    inner_n = sum(l.count(w) for l in body for w in inner)
    qratio = qline / n
    rows.append((ch, n, qline, round(qratio,2), inner_n))

rows.sort(key=lambda r: r[0])

print("=== 闷章（引号行占比<15% 且 内心戏>=4）===")
stale = [r for r in rows if r[3] < 0.15 and r[4] >= 4]
for r in stale:
    print(f"第{r[0]:3d}章 | 行数{r[1]:3d} | 引号行{r[2]:2d}({r[3]*100:.0f}%) | 内心戏{r[4]:2d}")

print("\n=== 引号行占比分布（每10章均值）===")
for lo in range(1, 201, 10):
    seg = [r for r in rows if lo <= r[0] < lo+10]
    if seg:
        avg = sum(r[3] for r in seg)/len(seg)
        print(f"{lo:3d}-{lo+9:3d}: {avg*100:.1f}%")

print("\n=== 引号行占比最低 Top12 ===")
for r in sorted(rows, key=lambda r: r[3])[:12]:
    print(f"第{r[0]:3d}章 | 引号行{r[2]:2d}({r[3]*100:.0f}%) | 内心戏{r[4]:2d}")

print("\n=== 内心戏最多 Top12 ===")
for r in sorted(rows, key=lambda r: -r[4])[:12]:
    print(f"第{r[0]:3d}章 | 引号行{r[3]*100:.0f}% | 内心戏{r[4]:2d}")
