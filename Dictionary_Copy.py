Dict = {'Boy1': 20, 'Boy2': 25, 'Girl1': 18, 'Girl2': 22, 'Boy3': 30}
print(Dict)
DictBoys = {'Boy1': 20, 'Boy2': 25, 'Boy3': 30}
print(DictBoys)
DictGirls = { 'Girl1': 18, 'Girl2': 22}
print(DictGirls)
CBoys = DictBoys.copy()
CGirls = DictGirls.copy()
print(CBoys)
print(CGirls)

#Update Dictionary
Dict.update({'Boys4':6})
#print updated Dictionary
Z ="Updated Dictionary :"
print(Z)
print(Dict)