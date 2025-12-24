with open("sample.txt",'r+') as f:
    text=f.read() #read existing fileno
    print("old",text)
    f.seek(0) #go back top start
    f.write("HI\n") #overwrite from begining