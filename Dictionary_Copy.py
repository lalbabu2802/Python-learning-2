Dict = {'Boy1': 20, 'Boy2': 25, 'Girl1': 18, 'Girl2': 22, 'Boy3': 30}
print(Dict)
DictBoys = {'Boy1': 20, 'Boy2': 25, 'Boy3': 30}
# print(DictBoys)
DictGirls = {'Girl1': 18, 'Girl2': 22}
# print(DictGirls)
CBoys = DictBoys.copy()
CGirls = DictGirls.copy()
# print(CBoys)
# print(CGirls)
# Update Dictionary
Dict.update({'Boys4': 6})
# print updated Dictionary
Z = "Updated Dictionary :"
# print(Z)
# print(Dict)

# deleting keys from Dictionary
del Dict['Boys4']
# print(Dict)

# Dictionary items() Method : returns items list of Dictionary
print("list in dictionary: %s" % list(Dict.items()))

# using for loop to print if keys exis in dictionary
print(Dict)
for key in list(Dict.keys()):
    if key in list(DictBoys.keys()):
        print("True")
    else:
        print("False")

# Sorting of Dictionary
Dict2 = {'abhi': 21, 'chatra': 32, 'jitu': 90, 'babu': 54, 'ram': 31}

SortedDict = list(Dict2.keys())
print("unsorted list in dictionary: %s" % SortedDict)
SortedDict.sort()
print("sorted list in dictionary: %s" % SortedDict)
for S in SortedDict:
    print(":".join((S, str(Dict2[S]))))

# Length of Dictionary
print("Length of Dictionary : %d" % len(Dict2))
# Variable types in dictionary
print("Types of variables: %s" % type(Dict2))
# printable string format of dictionary
print("printable string:%s" % str (Dict2))

