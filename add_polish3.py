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

files = {}
for f in glob.glob(base + '/第*章.txt'):
    m = re.match(r'第(.+?)章', os.path.basename(f))
    if m:
        files[cn2int(m.group(1))] = f

additions = {
199: """夜色里，那根针合上的不只是网眼，还有他一年前那个想摸鱼就摸鱼、不想担就溜的自己。""",

149: """六针之外，陈默还留了一手没命名的——叫'余针'。不是第七枚，是六针用旧了磨出来的手感，像老木匠闭眼也能找准榫头。他没写进底稿，只落在肌肉里。张伟问起，他说：'针会旧，手不能生。'
后来北境再没来敲门，不是怕，是进来也捞不着——网眼针针咬合，想撬一道缝，先得过了六针加那手余针。""",
}

for ch, txt in additions.items():
    p = files[ch]
    s = open(p, encoding='utf-8').read()
    lines = s.split('\n')
    idx = None
    for i in range(len(lines)-1, -1, -1):
        if re.match(r'——（第.+?章 完）——', lines[i].strip()):
            idx = i
            break
    if idx is None:
        print("NO MARKER", ch)
        continue
    lines.insert(idx, '\n' + txt)
    open(p, 'w', encoding='utf-8').write('\n'.join(lines))
    print("added", ch)
