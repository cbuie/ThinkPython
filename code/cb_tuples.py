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