import re
import numpy as np
from sklearn.naive_bayes import GaussianNB


def delete_second_element(my_grams):
    for i in my_grams:
        for j in i:
            j[1:] = []


def get_vec(all_vec, all_grams):
    for q in all_grams:
        for j in q:
            for i in j:
                all_vec.extend(i)


def list_merge_3(lstlst): #thanks http://habrahabr.ru/post/63539/ A LOT
    tmp = []
    for lst in lstlst:
      tmp.extend(lst)
    return tmp


def n_gram_vec(line, language, grams_n, number):  # get n grams from line
        added = []
        line1 = line[3:len(line)-1].replace(' ', '')
        line1 = [line1[ind:ind+number] for ind in range(len(line1)-number+1)]
        for tmp in line1:
            count = line[3:].count(tmp)
            if count:
                place = [same.count(tmp) for same in grams_n[language]] or [0]

                if not max(place):
                    grams_n[language].append([tmp, count])
                    added.append(tmp)
                else:
                    if not added.count(tmp):
                        grams_n[language][place.index(max(place))][1] += count
                        added.append(tmp)


def massive_sort(m_my_grams, m_languages):
        for q in range(len(m_languages)):   # thanks to https://wiki.python.org/moin/HowTo/Sorting
            m_my_grams[q].sort(key=lambda counter: counter[1], reverse=True)


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
