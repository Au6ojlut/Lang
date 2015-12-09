from b import *

test = []
counter = 0
languages = []
langs = []
lang2 = open('vec_monograms_tr.txt', 'r', encoding='utf8')

for line in lang2:
    languages.append(line.split()[0])
lang2.close()
NB = GaussianNB()
last = open('vec_normize_ts_tr.txt', 'r', encoding='utf8')
for line in last:
    if counter < 15000:
        test.append(line.split())
    else:
        train = line.split()
        train = [float(x) for x in train]
        a = languages[counter - 15000]
        NB.fit(np.array(train).reshape(1, -1), [a])
    counter += 1
last.close()
lang = open('monograms.txt', 'r', encoding='utf8')
for line in lang:
    langs.append(line.split()[0])
lang.close()


print("Start predicting")

f3 = open('answering.txt', 'w', encoding="utf8")
getcounter = 0
for item in test:
    f3.write(langs[NB.predict(np.array(item).reshape(1, -1))-1].upper() + '\n')
    getcounter += 1
    print(getcounter)
f3.close()