'''
Tuples are immutable

A tuple is a sequence of values. The values can be any type, and they are indexed by integers, so in that respect tuples are a lot like lists.
The important difference is that tuples are immutable.
'''
s = 'a'
t = 'a', #a tuple of one needs comma else it is a str
print type(s), type(t)

t = 'a','b','c' #or
t = ('a','b','c') #not necessary
print t, type(t)


# creating multiple tuples at the same time is as easy as:
a, b , c = 'one' , 'two', 3
print a, b, c


def sumIt(x):
    result = 0
    for i in x:
        result =+ i
    return result

def sum_all(*args):
    return sum(args)


def sum_all(*args):
    return sum(args)
print sum_all(1, 2, 3)
print sum_all(1, 2, 3, 4, 5)
print sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


'''
zip is a built-in function that takes two or more sequences and zips them into a list of tuples where each tuple contains one element from each sequence.
In Python 3, zip returns an iterator of tuples, but for most purposes, an iterator behaves like a list.

'''

s = 'abc'
t = [0,1,2]
z = zip(s,t); print z

#If the sequences are not the same length, the result has the length of the shorter one.

print(zip('anne','elk'))

#You can use tuple assignment in a for loop to traverse a list of tuples:

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print number, letter

'''
If you combine zip, for and tuple assignment, you get a useful idiom for traversing two (or more) sequences at the same time. For example, has_match takes two sequences,
t1 and t2, and returns True if there is an index i such that t1[i] == t2[i]:
'''
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


#If you need to traverse the elements of a sequence and their indices, you can use the built-in function enumerate:

for index, element in enumerate('christopher Buie'):
    print index, element
