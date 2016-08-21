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
The first line of the function creates an empty dictionary. The for loop traverses the string. Each time through the loop,
if the character c is not in the dictionary, we create a new item with key c and the initial value 1 (since we have seen this letter once).
If c is already in the dictionary we increment d[c]
'''


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

'''
Dictionaries have a method called get that takes a key and a default value. If the key appears in the dictionary, get returns the corresponding
value; otherwise it returns the default value. For example:
>>> h = histogram('a')
>>> print h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0
'''

def histogram(word):
    dictionary = dict()
    for character in word:
        dictionary[character] = 1 + dictionary.get(character, 0)
    return dictionary

print histogram('antidisestablishmentarianism').sort()

'''
Given a dictionary d and a key k, it is easy to find the corresponding value v = d[k].
This operation is called a lookup.
'''

#reverse lookup:

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    # raise can take a detailed error message
    raise ValueError ('value not found in dictionary')


h = histogram('parrot'); print h
k = reverse_lookup(h,3); print k

for i in h.values():
    results = []
    for k in h:
        if h[k] == i:
            results.append(list(i,h[k]))
        else:
            continue
print results


def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv


##Exercise 9
'''
If you did Exercise 8, you already have a function named has_duplicates that takes a list as a parameter and
returns True if there is any object that appears more than once in the list.
'''

l = ['red', 'yellow', 'green']

def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print has_duplicates(t)
    t.append(1)
    print has_duplicates(t)

    t = [1, 2, 3]
    print has_duplicates2(t)
    t.append(1)
    print has_duplicates2(t)



def has_duplicates3(l):
    return len(set(l)) < len(l)

