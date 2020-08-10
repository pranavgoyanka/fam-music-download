import requests
import tqdm
import os
from bs4 import BeautifulSoup
base = input('Enter Album URL code: ')
url = 'https://freeallmusic.top/track/' + base + '/'
i = 1
first = 1
last = int(input('Enter total number of tracks: '))
inf = {'Title': 0}
albumUrl = 'https://freeallmusic.top/album/' + base
a = requests.get(albumUrl)
soup = BeautifulSoup(a.text, features="html.parser")
a = soup.findAll ('meta', {'property': 'og:title'})
print(a)
b = str(a[0])
# b.encode(encoding='UTF-8',errors='strict')
start = b.find('content') + 9
c = b[start:]
end = c.find('property') - 8
album = b[start:start+end+6]
os.makedirs('downloads/' + album + '/', exist_ok=True)

# Download Function

def download(i = first):
    if(i < 10):
        song_url = url + '10' + str(i)
    else:
        song_url = url + '1' + str(i)

    a = requests.get(song_url)
    soup = BeautifulSoup(a.text, features="html.parser")
    a = soup.findAll ('a', {'class': 'text-danger'})
    b = str(a[0])
    # b.encode(encoding='UTF-8',errors='strict')
    start = b.find('href') + 6
    c = b[start:]
    end = c.find('"') - 6
    url_next = b[start:start+end+6]
    # url_next = b[start:end]

    s = requests.Session()
    a = requests.get(url_next)
    soup = BeautifulSoup(a.text, features="html.parser")
    title = soup.findAll ('h4', {'class': 'card-title text-uppercase font-weight-bold'})
    title = str(title[0])
    start = title.find('>') + 1
    c = title[start:]
    end = c.find('<') - 1
    title = title[start:start+end+1]
    a = soup.findAll ('a', {'class': 'btn-outline-success'})
    b = str(a[0])
    b = str(b)
    start = b.find('href') + 6
    c = b[start:]
    end = c.find('"') - 6
    url_dl = b[start:start+end+6]
    s.headers.update({'referer': url_next}) #url_next needs to be passed as the referer header for the get request
    p = s.get(url_dl)
    
    # Sanitize Special Characters while writing file
    set = '<>:"/\|?*'
    for c in set:
        title = title.replace(c, ';')
    

    open('downloads/'+album + '/'+title+'.mp3', 'wb').write(p.content)
    inf[title] = i

# Download Function Ends Here   

print('Downloading...\n')
for i in tqdm.tqdm(range(first, last +1), unit='song'):
    download(i)
    


print('\nVerifying...\n')
i = 0
for filename in tqdm.tqdm(os.listdir('downloads/'+album + '/'), unit='song'):
    
    info = os.stat('./downloads/'+ album + '/'+  filename)
    if info.st_size < 500000:
        print('Fixing ' + filename)
        os.remove('./downloads/' + album + '/'+ filename)
        download(inf[filename[:-4]])


print('Finished Downloading!')


