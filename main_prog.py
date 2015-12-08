from b import *





languages = []
data_train = []
answer = []
data_predict = []
f = open("monograms.txt", 'r', encoding="utf8")  # open file with smth need to train
for line in f:
    languages.append(line.split()[0])
f.close()

# for train

vec_monograms_tr = open('vec_monograms_tr.txt')
counter = 0
for line in vec_monograms_tr:
    vec = line.split()[1:]
    for q in range(15):
        if q == 0:
            tmp = vec
            data_train.append(tmp[32 * q:32 * q + 20])
        else:
            tmp = vec
            data_train[counter].extend(tmp[32 * q:32 * q + 20])

    counter += 1
vec_monograms_tr.close()

vec_bigrams_tr = open('vec_bigrams_tr.txt')
counter = 0
for line in vec_bigrams_tr:
    vec = line.split()[1:]
    for q in range(15):
        tmp = vec
        data_train[counter].extend(tmp[200 * q:200 * q + 60])
    counter += 1
vec_bigrams_tr.close()


vec_trigrams_tr = open('vec_trigrams_tr.txt')
counter = 0
for line in vec_trigrams_tr:
    vec = line.split()[1:]
    for q in range(15):
        tmp = vec
        data_train[counter].extend(tmp[300 * q:300 * q + 70])
    counter += 1
vec_trigrams_tr.close()


vec_fourgrams_tr = open('vec_fourgrams_tr.txt')
counter = 0
for line in vec_fourgrams_tr:
    vec = line.split()[1:]
    for q in range(15):
        tmp = vec
        data_train[counter].extend(tmp[400 * q:400 * q + 100])
    counter += 1
vec_fourgrams_tr.close()



w = open('vec_normize_tr.txt', 'w', encoding="utf8")
for q in preprocessing.normalize(data_train):
    w.write(' '.join(str(i) for i in q) + '\n')
w.close()

data_train = [] # too much RAM

# for predict
vec_monograms_tr = open('vec_monograms_ts.txt')
counter = 0
for line in vec_monograms_tr:
    vec = line.split()
    for q in range(15):
        if q == 0:
            tmp = vec
            data_train.append(tmp[32 * q:32 * q + 20])
        else:
            tmp = vec
            data_train[counter].extend(tmp[32 * q:32 * q + 20])

    counter += 1
vec_monograms_tr.close()

vec_bigrams_tr = open('vec_bigrams_ts.txt')
counter = 0
for line in vec_bigrams_tr:
    vec = line.split()
    for q in range(15):
        tmp = vec
        data_train[counter].extend(tmp[200 * q:200 * q + 60])
    counter += 1
vec_bigrams_tr.close()


vec_trigrams_tr = open('vec_trigrams_ts.txt')
counter = 0
for line in vec_trigrams_tr:
    vec = line.split()
    for q in range(15):
        tmp = vec
        data_train[counter].extend(tmp[300 * q:300 * q + 70])
    counter += 1
vec_trigrams_tr.close()


vec_fourgrams_tr = open('vec_fourgrams_ts.txt')
counter = 0
for line in vec_fourgrams_tr:
    vec = line.split()
    for q in range(15):
        tmp = vec
        data_train[counter].extend(tmp[400 * q:400 * q + 100])
    counter += 1
vec_fourgrams_tr.close()


w = open('vec_normize_ts.txt', 'w', encoding="utf8")
for q in preprocessing.normalize(data_predict):
    w.write(' '.join(str(i) for i in q) + '\n')
w.close()


