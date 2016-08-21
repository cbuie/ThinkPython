# General notes working with dictionaries from ThinkPython

#create dictionary:

x = dict()
x = {}

print x

# create empty dictionary of eng to spanish words:

eng2sp = dict()

#add elements to the dict()

# eng2sp['one'] =  'uno'
# print eng2sp

#or

x = ('one', 'two', 'three')
y = ('uno', 'dos', 'tres')

for i in range(len(x)):
    eng2sp[x[i]] = y[i]
print eng2sp