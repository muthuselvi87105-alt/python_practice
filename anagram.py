def anagram(s1,s2):
    if len(s1) != len(s2):
       return False
    count=[0] * 26
    for i in s1:
        count[ord(i) - ord('a')] +=1
    for j in s2:
        count[ord(j) - ord('a')] -= 1
    
    for k in count:
       if k !=0:
           return False
    return True 
k=anagram("state","taste")
if k:
    print("anagram")
else:
    print("not anagram")
