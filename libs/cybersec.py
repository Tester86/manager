from bs4 import BeautifulSoup
import requests

def getUrls(website):
    urls = []
    r = requests.get(website)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    for i in soup.find_all("a"):
        urls.append(i.get("href"))
    print("\nSearching in " + website + "\n")
    for i in urls:
        try:
            print("   -> " + i)
        except:
            pass
    return list(set(urls))

def getText(url):
    output = ""
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    text = soup.find_all(text=True)
    blacklist = [
        '[document]',
        'noscript',
        'header',
	    'html',
	    'meta',
	    'head', 
	    'input',
	    'script',
        'style',
        'div',
        'class'
    ]
    for i in text:
        if i.parent.name not in blacklist:
            output += i + " "
    print(output)

def autonet(url_list, num_of_tries=2):
    count = 0
    for i in range(num_of_tries):
        try:
            print("\nSearching in " + url_list[count] + "\n")
            getUrls(url_list[count])
            count += 1
        except:
            pass

