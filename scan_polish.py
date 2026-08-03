import os, re, glob

base = r"D:\WZJ\摸鱼：他们都以为我只是个写小说的\content"
files = glob.glob(os.path.join(base, "第*章.txt"))

cn_num = {
    '零':0,'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,
    '十':10,'百':100,'千':1000,'万':10000
}
def cn2int(s):
    total=0
    cur=0
    for ch in s:
        if ch in ('十','百','千','万'):
            unit=cn_num[ch]
            if unit==10:
                cur=cur if cur else 1
                total+=cur*10
                cur=0
            elif unit==100:
                total+=cur*100
                cur=0
            elif unit==1000:
                total+=cur*1000
                cur=0
            elif unit==10000:
                total+=cur*10000
                cur=0
        else:
            cur=cn_num.get(ch,0)
    return total+cur

brands = ['微信','腾讯','阿里','字节','抖音','微博','淘宝','京东','百度','支付宝','微软','苹果','谷歌','亚马逊','facebook','Facebook','微信 ']
# padded cliche phrases often repeated
cliches = ['活针不是孤针','比它先落','稳如磐石','双笔合织','键盘上帝的下一课','他熄灯前把','小打脸落在','中爽点落','连成网的针','浊流全球']

bad_chars=[]   # word count issues
bad_brand=[]
bad_repeat=[]
bad_selfref=[]

for f in sorted(files):
    txt=open(f, encoding='utf-8').read()
    m=re.match(r'.*第(.+?)章', os.path.basename(f))
    ch=cn2int(m.group(1)) if m else -1
    # strip title line and end marker
    body=txt
    body=re.sub(r'^#.*$','',body,flags=re.M)
    body=re.sub(r'——（第.+?完）——','',body)
    n=len(body.strip())
    if ch>=24 and (n<1500 or n>3000):
        bad_chars.append((ch,n))
    # brand
    for b in brands:
        if b in txt:
            bad_brand.append((ch,b))
    # cliche repeat count
    for c in cliches:
        cnt=txt.count(c)
        if cnt>=3:
            bad_repeat.append((ch,c,cnt))
    # self-reference: chapter number appearing in meta narrative
    if ch>0:
        pattern=re.compile(r'第%s章的?(灯熄|落定|的灯|这一章|本章)'%m.group(1))
        if pattern.search(txt):
            bad_selfref.append((ch,'selfref'))

print("=== 字数不达标 (期望1500-3000, 第24章起) ===")
print(bad_chars if bad_chars else "OK")
print("\n=== 真实品牌名 ===")
print(bad_brand if bad_brand else "OK")
print("\n=== 套路句重复>=3次 ===")
print(bad_repeat if bad_repeat else "OK")
print("\n=== 章号自指破次元 ===")
print(bad_selfref if bad_selfref else "OK")
print("\n文件总数:", len(files))
