with open('sample.txt','r+') as f:
    text=f.read()
    print("Old",text)
    f.seek(0)
    f.write("Hi \n")