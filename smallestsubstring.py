def frequency(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1


    for ele in s:
        if ele in freq:
            

    return freq
    
  


s = "programming"
result = frequency(s)
print(result)