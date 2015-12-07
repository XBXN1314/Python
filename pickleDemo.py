# -*- coding: utf-8 -*

# pickle 腌制

import pickle

# 将对象序列化
lista = ["mingyue", "jishi", "you"]
listb = pickle.dumps(lista)
print listb

# 将对象恢复

listc = pickle.loads(listb)
print listc

# 将对象存储到文件里面序列化

group1 = ("bajiu", "wen", "qingtian")
f1 = file('1.pk1', 'wb')
pickle.dump(group1, f1, True)
f1.close()

f2 = file('1.pk1', 'rb')
t = pickle.load(f2)
print t
f2.close()
