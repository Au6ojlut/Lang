from b import *

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


f = open("out.txt", 'r', encoding="utf8")    # open file with smth need to train
for line in f:
    a.append(line.split()[0])
f.close()


for ff in range(len(a)):  # get all languages using in file
    if not languages.count(a[ff]):
        languages.append(a[ff])

monograms = open('monograms.txt', 'r')
for line in monograms:
    all_monograms.append([line.split()])
monograms.close()


bigrams = open('bigrams.txt', 'r')
for line in bigrams:
    all_bigrams.append([line.split()])
bigrams.close()


trigrams = open('trigrams.txt', 'r')
for line in trigrams:
    all_trigrams.append([line.split()])
trigrams.close()



f.close()

print("grams ready \n")
number_of_grams(all_grams, [15, 60, 50])
get_vec(vec_of_all_grams, all_grams)
print("vector of grams ready ", len(vec_of_all_grams))

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
