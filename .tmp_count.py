import sys, os, re, glob

CN = "七十六 七十七 七十八 七十九 八十 八十一 八十二 八十三 八十四 八十五 八十六 八十七 八十八 八十九 九十 九十一 九十二 九十三 九十四 九十五 九十六 九十七 九十八 九十九 一百".split()

base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

def body_len(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    keep = []
    for ln in lines:
        s = ln.strip()
        if s.startswith("#"):
            continue
        if s.startswith("——（") and s.endswith("）——"):
            continue
        keep.append(s)
    text = "".join(keep)
    text = re.sub(r"\s", "", text)
    return len(text)

args = sys.argv[1:]
names = args if args else [f"第{n}章.txt" for n in CN]
for n in names:
    p = os.path.join(base, n)
    if not os.path.exists(p):
        print(n, "MISSING")
        continue
    L = body_len(p)
    flag = "OK" if 1500 <= L <= 3000 else "!!!"
    print(f"{n}\t{L}\t{flag}")
