import math

def calculate(s="circle",r=0,len=0,wid=0,base=0,hei=0):
    if s=='circle':
        return math.pi*r*r
    elif s=='rectangle':
        return len*wid
    elif s=='tri':
        return 0.5*base*hei
    else:
        return "invalid Shape"
    

print("circle",calculate(r=5))

print("rectsngle",calculate(s="rectangle",len=10,wid=5))
print("Triangle",calculate(s="tri",base=20,hei=10))


