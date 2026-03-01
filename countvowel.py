# Create a Python script that counts the number of vowels in a given string. Demonstrate the use of
#basic string operations like iteration and conditional checks

n=input("ENter a String:")
vowel="aeiou"
count=0
for ele in n:
    if ele in vowel:
        count=count+1


print("Total Voewl",count)