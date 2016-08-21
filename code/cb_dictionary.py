# General notes working with dictionaries from ThinkPython

# create dictionary:

x = dict()
x = {}

print x

# create empty dictionary of eng to spanish words:

eng2sp = dict()

# add elements to the dict()

# eng2sp['one'] =  'uno'
# print eng2sp

# or

x = ('one', 'two', 'three')
y = ('uno', 'dos', 'tres')

for i in range(len(x)):
    eng2sp[x[i]] = y[i]

print eng2sp

'''
#interesting!
The in operator uses different algorithms for lists and dictionaries. For lists, it uses a search algorithm, as in Section 8.6. As the list gets longer, the search time gets longer in direct proportion.
For dictionaries, Python uses an algorithm called a hashtable that has a remarkable property: the in operator takes about the same amount of time no matter how many items there are in a dictionary.
'''

with open('code/words.txt', mode='r') as fd:
    words = fd.read().splitlines()

result = {}


def wordDict():
    for line in words:
        result[line] = words.index(line)
    return result


print wordDict()



import uuid

with open('code/words.txt') as fd:
    words = fd.read().splitlines()

result = dict()


def dictionary():
    for line in words:
        result[line] = uuid.uuid4()
    return result

print dictionary()


#Dictionary as counters:
#very nice!

'''
The first line of the function creates an empty dictionary. The for loop traverses the string. Each time through the loop, if the character c is not in the dictionary, we create a new item with key c and the initial value 1 (since we have seen this letter once). If c is already in the dictionary we increment d[c]
'''

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d