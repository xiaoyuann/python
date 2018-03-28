def moveZeroes():
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
def isIsomorphic1(s, t):
    d1, d2 = {}, {}
    for i, val in enumerate(s):
        d1[val] = d1.get(val, []) + [i]
    for i, val in enumerate(t):
        d2[val] = d2.get(val, []) + [i]
    print(d1.values(),d2.values())
    return sorted(d1.values()) == sorted(d2.values())
             
pattern='asdfgh'
str='aa bb cc cc cc'

for s in str.split():
        print(s)
        print({}.setdefault(s,range(len(s))))
f = lambda s: list(map({}.setdefault, s, range(len(s))))
print(f(pattern),f(str.split()))
