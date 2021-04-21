# This is a Python program to take a string and print the letters in the drcreasing order of sequence
# (Task1)

W= input('Please enter a string ')

def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print ( most_frequent(W))
