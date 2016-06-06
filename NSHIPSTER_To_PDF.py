
# Download http://nshipster.com tutorials as PDF file
# @author - Ratan Lal Prasad
# @email - ratan.kgn@gmail.com


import os, sys, shutil
import pdfkit
import urllib3
from bs4 import BeautifulSoup


STORE_DIRECTORY_PATH = '/Users/ratan/Documents/'
FOLDER_NAME = 'NSHIPSTER_TUTORIALS'

# CHECK FOR DIRECTORY
if not os.path.exists(STORE_DIRECTORY_PATH+FOLDER_NAME) :
        os.mkdir(STORE_DIRECTORY_PATH+FOLDER_NAME)

# Parse website
url ='http://nshipster.com'
http_pool = urllib3.connection_from_url(url)
r = http_pool.urlopen('GET', url)

soup = BeautifulSoup(r.data.decode('utf-8'), "html.parser")

DOWNLOAD_FOLDER_PATH = STORE_DIRECTORY_PATH+FOLDER_NAME+'/'

for link in soup.find_all('a'):
    path = link.get('href')
    if path.find("http://") == 0 or path.find("https://") == 0 or path == '/' or path.find("..") == 0:
        print("no need to download this")

    else:
        # print("\n WITHOUT LINK -- ", path)
        try:
            filename = path.replace('/', '') + '.pdf'
            urlToDownload = url + path  # --- use for nshipster
            # urlToDownload = base_url + path # use for python docs
            # print("url to download ", urlToDownload)
            os.chdir(os.path.dirname(__file__))
            # print('Source file ',os.getcwd() + '/' + filename)
            pdfkit.from_url(urlToDownload, filename)
            # print("Destination  ", DOWNLOAD_FOLDER_PATH+filename)
            shutil.move(os.getcwd() + '/' + filename, DOWNLOAD_FOLDER_PATH+filename)
        except:
            print ("Unexpected error:", sys.exc_info()[0])

        # break


