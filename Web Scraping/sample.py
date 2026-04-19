import requests
from bs4 import BeautifulSoup

web=requests.get("https://www.tutorialsfreak.com/")
print(web) #<response 200 means web in working condition

print(web.content)
print(web.url)