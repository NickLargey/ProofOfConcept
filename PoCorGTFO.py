import webbrowser, requests, bs4, os

url = 'https://www.alchemistowl.org/pocorgtfo/'
os.makedirs('PoC||GTFO', exist_ok=True)

# download page
print('downloading page...')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

names = []
linkpdf = []
for i, link in enumerate(soup.findAll('a')):
	fullURL = url + link.get('href')
	if fullURL.endswith('.pdf'):
		linkpdf.append(fullURL)
		names.append(soup.select('a')[i].attrs['href'])

names_urls = zip(linkpdf, names)

for url, name in names_urls:
    print(name)
    res = requests.get(url)
    res.raise_for_status()
    pdf = open(os.path.join('PoC||GTFO', os.path.basename(url)), 'wb')
    for i in res.iter_content(10000000):
    	pdf.write(i)
    pdf.close()


print('done')







