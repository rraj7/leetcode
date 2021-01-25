""" def create_unique(array1,array2):
    set1 = set(array1)
    set2 = set(array2)

    list1 = list(set2-set1)
    final = array1+list1

    return final

array1 = ["Alice","Sammy","Olivia","rupert"]
array2 = ["Alice","john","Denver","Olivia"]
#exp output = [Alice, Sammy, Olivia,Rupert,John,Denver]

q = create_unique(array1,array2)
print(q)

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 1, 'for' : 3, 'CS' : 2}

d_input = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

from collections import defaultdict

res = defaultdict(list)
for key, val in sorted(d_input.items()):
    res[val].append(key)


print(str(dict(res)))

i/p = ["test","test1","test2","test2","test1","tset"]
o/p = ["test", "test1","test2"]


def uniqueString(array):
    hash = {}
    for i in range len(array1):

 """


def result(array):
    if (array ==1):
        return 2;
    else :
        return 2* result(array-1)
    

print(result(4))