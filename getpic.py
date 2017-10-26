#!/usr/bin/env python3

# A function to get a url from user and if it's url of a picture ,
# then download it in the current directory
import requests
import os
from bs4 import BeautifulSoup
def img_check( req ) :
    magic_dict = {
                'png' : b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' ,
                'jpg' : b'\xFF\xD8' ,
                 }
    if req.content.startswith(magic_dict['png'] )   :
        print('Image type : png')
        return 1

    elif req.content.startswith(magic_dict['jpg'] ) :
        print('Image type : jpg/jpeg')
        return 1
    else:
        try:
            beautified = BeautifulSoup(req.content,'xml') 
            if beautified.format.text.startswith('image/svg') :
                print('Image type : svg')
                return 1
        except:
            print('Sorry! File type not supported . ')
            return 0
                

def download_pic ( url ) :
    if url.split('.')[-1] not in ('png','jpg','svg') :
        print('Not an image url ')
        exit()
    req = requests.get(url)
    if req.status_code != 200 : 
        print('Error getting the page ! ')
        exit()
    if  img_check(req) == 0:
        exit()
    filename=url.split('/')[-1] 
    #Renaming file , if another with same name exists 
    counter=1
    extension = filename.split('.')[1]
    filename = filename.split('.')[0]
    tmpfilename = filename
    while os.path.isfile(os.getcwd() + '/' + tmpfilename + '.' + extension) :
        print('A file with same name already exists \nChanging name')
        tmpfilename = filename + str(counter)
        counter=counter + 1

    filename=tmpfilename + '.' + extension
    
    with open(filename,'wb') as imagef :
        imagef.write(req.content)
    print('Download complete')
    print('File name : %s ' %(filename) )

   

if __name__ == '__main__' :
    url = input("Enter the url to the possible picture : ")
    download_pic ( url )


