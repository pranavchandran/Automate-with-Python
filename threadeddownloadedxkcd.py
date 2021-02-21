# Downloads XKCD comics using multiple threads.
# pip3 install BeautifulSoup4
# pip3 install requests

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True) #store comics in ./xkcd

def downloadxkcd(startComic, endComic):
    for urlnumber in range(startComic, endComic):
        # download the page
        print('Downloading page https://xkcd.com/%s...'%(urlnumber))
        res = requests.get('https://xkcd.com/%s'%(urlnumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # Find url of the comic page
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('could not find comic image')
        else:
            comicurl = comic_elem[0].get('src')
            # download the image
            print('Downloading image %s...'%comicurl)
            res = requests.get('https:' + comicurl)
            res.raise_for_status()
            # save the image to ./xkcd
            imagefile = open(os.path.join('xkcd', os.path.basename(comicurl)),'wb')
            for chunk in res.iter_content(100000):
                imagefile.write(chunk)
            imagefile.close()

# create and start thread objects
# wait for all threads to end
downloadxkcd(1,10)

# Downloads XKCD comics using multiple threads
downloadthreads = []
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1 #there is no comic 0, so set it to 1
    downloadthread = threading.Thread(target=downloadxkcd, args=(start, end))
    downloadthreads.append(downloadthread)
    downloadthread.start()

# wait for all threads to end
for downloadthread in downloadthreads:
    downloadthread.join()
print('Done')

