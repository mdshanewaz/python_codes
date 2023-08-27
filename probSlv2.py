def stringAnagram(dictionary, query):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    
    result = []

    count = 0

    for q in query:
        for p in dictionary:
            if is_anagram(q, p):
                count = count + 1;
            
        result.append(count)
    
    print(result)

hello = stringAnagram(['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stair', 'raits'], ['a', 'nark', 'bs', 'hack', 'stair'])


