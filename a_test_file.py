dognames_dic = dict()
with open('dognames.txt', 'r') as dognames:
    for line in dognames:
        dognames_dic[line.rstrip()] = 1
    
print(dognames_dic)