from itertools import combinations

comb_words = combinations('abcdefghijklmnopqrstuvwxyz', 9)

for i in comb_words:
    #convert combinations from tuple to string
    s_change= "".join(i) + '\n'
    #print(s_change)
    #appends entries to anagram txt file
    #only needed this program to run once ergo not optimized
    f = open("anagrams.txt",'a')
    f.writelines(s_change)
f.close()
