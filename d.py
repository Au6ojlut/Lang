import re
from nltk.util import ngrams
from collections import defaultdict
from math import log
import numpy as np
from sklearn.naive_bayes import GaussianNB


def delete_second_element(my_grams):
    for i in my_grams:
        for q in i:
            for j in q:
                j[1:] = []


def get_vec(all_vec, all_grams):
    for q in all_grams:
        for j in q:
            for i in j:
                all_vec.extend([i])


def list_merge_3(lstlst):   # thanks http://habrahabr.ru/post/63539/ A LOT
    tmp = []
    for lst in lstlst:
      tmp.extend(lst)
    return tmp


def n_gram_vec(line, language, grams_n):  # get all grams from line
    for number in range(1, 4):
        added = []
        line1 = [x.strip(' ') for x in line[3:]]
        line1.pop()
        line1 = [x for x in line1 if x]
        for tmp in ngrams(line1, number):
            tmp1 = ''.join(list_merge_3(tmp))
            count = line[3:].count(tmp1)
            if count:
                place = [same.count(tmp1) for same in grams_n[number-1][language]] or [0]

                if not max(place):
                    grams_n[number-1][language].append([tmp1, count])
                    added.append(tmp1)
                else:
                    if not added.count(tmp1):
                        grams_n[number-1][language][place.index(max(place))][1] += count
                        added.append(tmp1)


def massive_sort(m_my_grams, m_languages):  # sort massive by counts value
    for i in range(len(m_my_grams)):
        for q in range(len(m_languages)):   # thanks to https://wiki.python.org/moin/HowTo/Sorting
            m_my_grams[i][q].sort(key=lambda counter: counter[1], reverse=True)


def number_of_grams(my_grams, vec_of_numbers):
    for i in range(len(my_grams)):
        for j in my_grams[i]:
                j[vec_of_numbers[i]:] = []

# don't use yet
def delete_the_same(unique_gram):  # can be optimized but i am lazy(
    buffer = [[gram[0] for gram in lang] for lang in unique_gram]
    for k in range(len(unique_gram)):
        deleting_bufer = []
        for gram_t in buffer[k]:
            same = False
            for next in range(k+1, len(buffer)):
                if buffer[next].count(gram_t):
                    unique_gram[next].pop(buffer[next].index(gram_t))
                    buffer[next].remove(gram_t)
                same = True
            if same:
                deleting_bufer.append(gram_t)
        for d in deleting_bufer:
            unique_gram[k].pop(buffer[k].index(d))
            buffer[k].remove(d)


a = []
languages = []
ver_monograms = []
ver_bigrams = []
ver_trigrams = []
ver = [ver_monograms, ver_bigrams, ver_trigrams]
mean = []
all_bigrams = []
all_trigrams = []
all_monograms = []
all_grams = [all_monograms, all_bigrams, all_trigrams]
vec_of_all_grams = []
f = open("tr.txt", 'r', encoding="utf8")    # open file with smth need to train


for line in f:
    a.append(line.split()[0].lower())


f.close()


for ff in range(len(a)):  # get all languages using in file
    if not languages.count(a[ff]):
        languages.append(a[ff])

print(all_grams)
f = open('all_grams.txt', 'r', encoding="utf8")    # open output while for reading, because this file is ready for work
ccc = 0
for line in f:
    if ccc < 15:
        all_monograms.append(line[3:].split())
    elif ccc < 30:
        all_bigrams.append(line[3:].split())
    else:
        all_trigrams.append(line[3:].split())
    ccc += 1




f.close()

#massive_sort(all_grams, languages)
print("grams ready \n")
number_of_grams(all_grams, [10, 10, 15])
#delete_second_element(all_grams)

get_vec(vec_of_all_grams, all_grams)
print("vector of grams ready")

data_train = []
data_answer = []
f = open('out.txt', 'r', encoding="utf8")
for line in f:
    data_train.append([line[3:].count(q) for q in vec_of_all_grams])
    data_answer.append(languages.index(line.split()[0])+1)
f.close()
print("have data from file")
data_predict = []
f = open('out2.txt', 'r', encoding="utf8")
for line in f:
    data_predict.append([line.count(q) for q in vec_of_all_grams])
f.close()
data_train = np.array(data_train)
data_answer = np.array(data_answer)
data_predict = np.array(data_predict)

print("start training")
model = GaussianNB()
model.fit(data_train, data_answer)
print("Start predicting")
predicted_m = model.predict(data_predict)
f3 = open('answering.txt', 'w', encoding="utf8")
for item in predicted_m:
    f3.write("%s\n" % languages[item-1].upper())
f3.close()
