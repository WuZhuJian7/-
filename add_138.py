p = "D:/WZJ/摸鱼：他们都以为我只是个写小说的/content/第一百三十八章.txt"
s = open(p, encoding='utf-8').read()

a = '她笑："网不崩的底，是你俩一枚枚针叠的。"'
b = '\n\n陈默靠回椅背。双笔并立，他从前只当是两人力气大；这一回才咂摸出真味——不是合力，是替手。沈砚的网漏了，他的针补；他的针偏了，沈砚的核兜。一个人落针，总怕写崩；两个人怕的是同一件事，反倒谁都不慌。'
assert a in s, "anchor A not found"
s = s.replace(a, a + b, 1)

c = '他熄灯前想：合织之法拦大稿'
d = '他看了眼时间，离废笔落针才过去几个钟头。几个钟头，北境从“主导框架”的美梦，掉到“换笔救命”的狼狈。\n\n他熄灯前想：合织之法拦大稿'
assert c in s, "anchor C not found"
s = s.replace(c, d, 1)

open(p, 'w', encoding='utf-8').write(s)
print("138 增补完成，字数：", len(s))
