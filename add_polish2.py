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
149: """张伟后来又问：'六针够了？'
陈默摇头：'够不够，看网。网要漏，再加；网稳了，就收。'
他没把六针当法宝，当拐杖——人是瘸的才靠拐，人是站着的，针只是鞋底的钉，防滑不代步。
那晚他关灯时想：真正护网的，从来不是针，是肯落针的那只手没抖。""",

175: """林小鹿听完实名针的事，只说了一句：'所以你现在是全网最讲身份的邻居。'
陈默笑：'身份不是枷，是门牌。门牌亮了，想混进来的，先想想自己配不配敲这扇门。'
她没再接，只是把陈默茶杯添满。两人之间，很多话到这份上，就不用说透了。""",

199: """沈砚在群里发来一行：'网眼都补了，早些睡。'
陈默回了个'好'。他想起一年前那个摸鱼的午后，绝不会想到自己有天会守着一张全网织的网入睡。
故事写到这儿，该落笔了。可网还醒着，六针还亮着——所以他只是熄灯，没说结束。""",

142: """后来张伟真学会了'钉指头'——有回有人造他谣，他没找陈默，自己照葫芦画瓢落了笔，虽然针歪了半寸，但谎还是灭了。他给陈默截图，附言：'师傅，出师了。'""",

141: """那枚废签在草稿箱里躺了很久。偶尔陈默翻到，会想起砚翁递笔时的手——稳，却带着将枯的颤。固口针守的，原来是'笔枯之前，先认枯'。""",

143: """林小鹿听完，只说了句：'那你这守门人，守的是桌子，不是门。'陈默点头。门是给人进的，桌子是给人站——他宁可门破，不让桌翻。""",
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

def reduce_freq(p, word, repl, keep=2):
    s = open(p, encoding='utf-8').read()
    count = s.count(word)
    if count <= keep:
        print(os.path.basename(p), "freq", count, "OK")
        return
    idxs = [m.start() for m in re.finditer(word, s)]
    new = s
    for i in range(len(idxs)-1, keep-1, -1):
        st = idxs[i]
        new = new[:st] + repl + new[st+len(word):]
    open(p, 'w', encoding='utf-8').write(new)
    print(os.path.basename(p), "freq", count, "->", keep)

reduce_freq(files[142], '双笔合织', '合织之法', 2)
reduce_freq(files[144], '双笔合织', '合织之法', 2)
