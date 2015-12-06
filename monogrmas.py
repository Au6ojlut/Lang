from b import *
a = []
languages = []
all_monograms = []


f = open("tr.txt", 'r', encoding="utf8")    # open file with smth need to train
for line in f:  # split text for deleting spaces and other symbols
    a.append(line.split()[0])


for ff in range(len(a)):  # get all languages using in file
    if not languages.count(a[ff]):
        languages.append(a[ff])
for ii in languages:  # init grams massive
    all_monograms.append([])


f = open('out.txt', 'r', encoding="utf8")    # open output while for reading, because this file is ready for work
for line in f:
    n_gram_vec(line, languages.index(line.split()[0]), all_monograms, 1)
f.close()


massive_sort(all_monograms, languages)
print("grams sorted \n")

delete_second_element(all_monograms)

w = open('monograms.txt', 'w', encoding="utf8")
for i in range(len(all_monograms)): #print all n-grams to file
    for item in range(len(languages)):
        w.write("%s\n" % ' '.join((str(languages[item]), ' '.join([' '.join(q) for q in all_monograms[i][item]]))))
w.close()
