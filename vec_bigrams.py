from b import *

languages = []
mean = []
all_bigrams = []
all_trigrams = []
all_monograms = []
all_fourgrams = []
all_grams = [all_monograms, all_bigrams, all_trigrams, all_fourgrams]
vec_of_all_grams = []


f = open("bigrams.txt", 'r', encoding="utf8")    # open file with smth need to train
for line in f:
    languages.append(line.split()[0])
f.close()


#for ff in range(len(a)):  # get all languages using in file
#    if not languages.count(a[ff]):
#        languages.append(a[ff])

bigrams = open('bigrams.txt', 'r')
for line in bigrams:
    all_bigrams.append(line[3:].split())
bigrams.close()



f.close()

print("grams ready \n")
number_of_grams(all_grams, [0, 200, 0, 0])
get_vec(vec_of_all_grams, all_bigrams, len(languages))
print("vector of grams ready ", len(vec_of_all_grams))

data_train = []
data_answer = []


f = open('out.txt', 'r', encoding="utf8")
w = open('vec_bigrams_tr.txt', 'w', encoding="utf8")
for line in f:
    w.write(''.join(str(languages.index(line.split()[0])+1)) + ' ' + ' '.join(str(line[3:].count(q)) for q in vec_of_all_grams) + '\n')
f.close()
w.close()


f = open('out2.txt', 'r', encoding="utf8")
w = open('vec_bigrams_ts.txt', 'w', encoding="utf8")
for line in f:
    w.write(' '.join(str(line.count(q)) for q in vec_of_all_grams) + '\n')
f.close()
w.close()
