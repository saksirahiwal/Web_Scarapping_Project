## step 0:setup environment foe web scraping
## import libraries
import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com"

## step 1: Get html Content from codewith harry website

r=requests.get(url)
htmlContent=r.content
print(htmlContent)

## step 2:Beautify html content
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)

## spet 3: Html tree traversal
## get html tittle
title=soup.title
print(type(title))

## get html all paragrph
paras=soup.find_all('p')
#print(paras)


##get first element of html page
print(soup.find('p'))

##get classes of any element in html page

print(soup.find('p')['class'])

## find all the element with class mt-2

print(soup.find_all("p",class_="mt-2"))

# get the text from the tags
print(soup.find('p').get_text())

##get all html anchor tags
anchor=soup.find_all('a')
all_link=set()
#get all link on the page
for link in anchor:
    if(link.get('href')!='#'):
        linkText="https://www.codewithharry.com"+link.get('href')
        all_link.add(link)
        print(linkText)
##Get id content
navbarContent=soup.find(id='search-toggle')
for elem in navbarContent.contents:
    print(elem)
    
for item in navbarContent.parents:
    print(item.name)  
    
print(navbarContent.next_sibling.next_sibling)  

    



        

    


