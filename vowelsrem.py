def remove_vo(text):
    result=""
    vowel="aeiou"
    for ch in text:
        if ch not in vowel:
            result=result+ch
    return result
    

tx="Hello Devuo"
res=remove_vo(tx)
print(res)