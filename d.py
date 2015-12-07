from b import *

languages = []
mean = []
all_bigrams = []
all_trigrams = []
all_monograms = []
all_fourgrams = []
all_grams = [all_monograms, all_bigrams, all_trigrams, all_fourgrams]
vec_of_all_grams = []


f = open("monograms.txt", 'r', encoding="utf8")    # open file with smth need to train
for line in f:
    languages.append(line.split()[0])
f.close()


#for ff in range(len(a)):  # get all languages using in file
#    if not languages.count(a[ff]):
#        languages.append(a[ff])

monograms = open('monograms.txt', 'r')
for line in monograms:
    all_monograms.append(line[3:].split())
monograms.close()


bigrams = open('bigrams.txt', 'r')
for line in bigrams:
    all_bigrams.append(line[3:].split())
bigrams.close()


trigrams = open('trigrams.txt', 'r')
for line in trigrams:
    all_trigrams.append(line[3:].split())
trigrams.close()


fourgrams = open('fourgrams.txt', 'r')
for line in fourgrams:
    all_fourgrams.append(line[3:].split())
fourgrams.close()


f.close()

print("grams ready \n")
number_of_grams(all_grams, [32, 100, 100, 100])
get_vec(vec_of_all_grams, all_grams, len(languages))
print("vector of grams ready ", len(vec_of_all_grams))

data_train = []
data_answer = []


f = open('out.txt', 'r', encoding="utf8")
w = open('tr_vec.txt', 'w', encoding="utf8")
for line in f:
    w.write(''.join(str(languages.index(line.split()[0])+1)) + ' ' + ' '.join(str(line[3:].count(q)) for q in vec_of_all_grams) + '\n')
f.close()


print("have data from file")

"""

data_predict = []
f = open('out2.txt', 'r', encoding="utf8")
counter = 1
for line in f:
    data_predict.append([line.count(j) for j in vec_of_all_grams])
    #print([line.count(j) for j in vec_of_all_grams])

#print((data_predict[1]))
answer = []

# maybe add priority
'''
for line in data_predict:
    tmp = []
    for q in range(1, len(languages)+1):
        tmp.append([sum(line[(q-1)*135:135*q]), languages[q-1]])
    answer.append(get_max_element(tmp)[1])
#answer
w = open('answering.txt', 'w')
for q in answer:
    w.write(q.upper() + '\n')
w.close()
'''
for line in f:
    data_predict.append([line[3:].count(q) for q in vec_of_all_grams])
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
    f3.write(languages[item-1].upper() + '\n')
f3.close()
"""