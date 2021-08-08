dognames_dic=dict()

with open('dognames.txt') as dogname_file:
    for line in dogname_file.readlines():
        dogname=line.rstrip()
        if dogname not in dognames_dic.keys():
            dognames_dic[dogname]=1
        else: print('dog name already exist in the dog names dict')
dogname_file.close()       
print(dognames_dic)