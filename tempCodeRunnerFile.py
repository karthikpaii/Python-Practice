import wikipedia
topic=input("Enter a Keyword To Search:")
print("="*30)
print(f"Search For a {topic}")
print("="*30)
res=wikipedia.summary(topic,sentences=20)
print(res)
print("="*30)