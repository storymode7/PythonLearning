#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
def extract_url(url,option=2) :
    req=requests.get(url)
    if req.status_code == 404 :
        print("Cannot find the page requested")
        exit()
    soup = BeautifulSoup(req.content, 'html.parser')
    all_links=[]
    for link in soup.find_all('a') :
        if option == 1 :
            all_links.append(url+link.get('href'))
        else :
            all_links.append(link.get('href'))
    return all_links


if __name__ == '__main__' :
    url=input('Enter the url to extract links from : ')
    option = 0
    while option == 0  :
        try :
            option=(int(input('Do you want \n1)Absolute links ,or\n2)Relative links \nEnter choice number : ')) ) 
        except ValueError :
            print('Please enter any one from 1 or 2 ')
        
    links=extract_url(url,option)
    for link in links :
        print(link)
