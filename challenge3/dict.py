#!/usr/bin/python
out = ""
def recursive_items(dictionary):
    global out 
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            out = out + '/' + key 
            yield from recursive_items(value)
        else:
            yield (key, value)
            out = out + '/' + key

a = {'a': {'b': {'c': {'d': 'e'}}}}

for key, value in recursive_items(a):
    print(key, value)

print('Key: ',out,' Value: ',value)
