import requests
from audio import *

# globals

sources = {"elcorreo" : "https://www.elcorreo.com/", "elmundo": "https://www.elmundo.es/"}
source_key_list = []

# globals

def getNews(paper_name):
    global sources
    r = requests.get(sources[paper_name])
    content = r.text.split()
    for i in content:
        if i.startswith("<"):
            i = ""
            while not i.endswith(">"):
                i = ""
    print(content)




def menu():
    global sources
    global source_key_list
    count = 0
    #say("Señor, estos son los periódicos que posee actualmente")
    for i in sources:
        source_key_list.append(i)
    for i in source_key_list:
        count += 1
        print(f"   {[count]} {source_key_list[count - 1]}")
    while True:
        #say("¿Qué periódico desea leer?")
        cmd = input("Número > ")
        num = int(cmd)
        getNews(source_key_list[num])

        

if __name__ == "__main__":
    menu()
