#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

def firstUniqChar(s):
    count = collections.Counter(s)

    for index, letter in enumerate(s):
        if count[letter]==1:
            return index
    return -1
