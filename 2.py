import wikipedia
import sys
import requests
import bs4
import urllib.request
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from os import path

file1="F:/Amrita Mtech/Glisten Internship/Work/Media wiki/Saved Documents/Level0/doc1.txt"
wordfile0="F:/Amrita Mtech/Glisten Internship/Work/Media wiki/Saved Documents/Level0/words.txt"
wordfile1="F:/Amrita Mtech/Glisten Internship/Work/Media wiki/Saved Documents/Level0/words.txt"
basepath="F:/Amrita Mtech/Glisten Internship/Work/Media wiki/Saved Documents/Level1"

#level 0 data
res= requests.get('https://en.wikipedia.org/wiki/'+'Sinhagad')
res.raise_for_status()

wiki=bs4.BeautifulSoup(res.text,"html.parser")
with open(file1,'w') as file:    
    for i in wiki.select('p'):
        print(i.getText())
        file.write(i.getText())

#level 1 data
removableList=["Category:Sinhagad"]
sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Sinhagad').read()
soup=bs4.BeautifulSoup(sauce,'lxml')
print(soup.get_text())
links1 = soup.find("div",{"id" : "bodyContent"}).findAll("a" , href=re.compile("(/wiki/)+([A-Za-z0-9_:()])+"))
links=links1[0:50]

beg_link = 'http://www.wikipedia.com'
count=0
for link in links:
    count=count+1
    full_link = beg_link + link['href']
    print(full_link)
    webpage=requests.get(full_link)
    webpage.raise_for_status()
    soup=bs4.BeautifulSoup(webpage.text,"html.parser")
    
    file2="F:/Amrita Mtech/Glisten Internship/Work/Media wiki/Saved Documents/Level1/"+str(count)+".txt"
    f=open(file2,"w")
    f.write(full_link)
    for i in soup.select('p'):
        text=i.getText()
        txt=text.encode('unicode-escape').decode('utf-8')
        print(txt)
        f.write(txt)      
    f.close()

#Removing stop words
stop_words = set(stopwords.words('english'))
file = open(file1) 
line = file.read()# Use this to read file content as a stream: 
words = line.split()
print(words)
for r in words: 
    if not r in stop_words: 
        appendFile = open(wordfile0,'a') 
        appendFile.write(" "+r) 
        appendFile.close()
        #print(r)

#level 1
count=1
for i in range(1,50):
    fileName=path.join(basepath , str(count)+".txt")
    file = open(fileName) 
    line = file.read()# Use this to read file content as a stream: 
    words = line.split()
    print(words)
    count=count+1
    for r in words: 
        if not r in stop_words: 
            appendFile = open(wordfile1,'a') 
            appendFile.write(" "+r) 
            appendFile.close()
            #print(r)



    

    



