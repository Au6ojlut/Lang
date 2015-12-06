import re


f = open("tr.txt", 'r', encoding="utf8") # open file with smth need to train
w = open('out.txt', 'w', encoding="utf8")    # open output file for writing


for line in f:  # split text for deleting spaces and other symbols
    w.write(" ".join(((re.sub(r"[^\w\s]+|[\d]+", r'', line).strip()).split())).lower() + '\n')

f.close()   # close both files
w.close()

f2 = open('ts.txt', 'r', encoding="utf8")
w2 = open('out2.txt', 'w', encoding="utf8")
for line in f2:
    w2.write(" ".join(((re.sub(r"[^\w\s]+|[\d]+", r'', line).strip()).split())).lower() + '\n')
f2.close()
w2.close()

