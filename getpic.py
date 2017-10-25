#!/usr/bin/env python3

# A function to get a url from user and if it's url of a picture ,
# then download it in the current directory
import requests
import os
def download_pic ( url ) :
    if url.split('.')[-1] not in ('png','jpg','svg') :
        print('Not an image url ')
        exit()
    req = requests.get(url)
    if req.status_code != 200 : 
        print('Error getting the page ! ')
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


