with open("sample.txt","r") as f:

    content=f.read()

    char=len(content)

    word=content.split()
    words=len(word)


    line=content.splitlines()
    linec=len(line)



with open("output.txt","w") as r:
    r.write(f" Number of Character {char} \n")
    r.write(f" Number of Lines {linec}")
    r.write(f" Number of words {words} \n")


