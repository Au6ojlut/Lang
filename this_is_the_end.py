from b import *

train = []
test = []
counter = 0
languages = []
langs = []
last = open('vec_normize_ts_tr.txt', 'r', encoding='utf8')
for line in last:
    if counter < 15000:
        test.append(line.split())
    else:
        train.append(line.split())
    counter += 1
last.close()
lang = open('monograms.txt', 'r', encoding='utf8')
for line in lang:
    langs.append(line.split()[0])
lang.close()

lang2 = open('vec_monograms.txt', 'r', encoding='utf8')

for line in lang2:
    languages.append(line.split()[0])
lang2.close()
NB = GaussianNB()
NB.fit(train, languages)
print("Start predicting")
predicted_m = NB.predict(test)

f3 = open('answering.txt', 'w', encoding="utf8")

for item in predicted_m:
    f3.write(langs[item-1].upper() + '\n')
f3.close()