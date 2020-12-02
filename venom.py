import requests
from bs4 import BeautifulSoup
from colorama import Fore
import random
import os

os.system('clear')
w = Fore.WHITE
g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
c = Fore.CYAN
y = Fore.YELLOW

colors = (w, g, r, b, c, y)
color = random.choice(colors)
banner = '''

██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗      ███╗   ██╗███████╗██╗    ██╗███████╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ████╗  ██║██╔════╝██║    ██║██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗██╔██╗ ██║█████╗  ██║ █╗ ██║███████╗
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║╚██╗██║██╔══╝  ██║███╗██║╚════██║  Made By Venom
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██║ ╚████║███████╗╚███╔███╔╝███████║  Insta -: i.m.gauravchaudhary
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ ╚══════╝  Whatsapp -: +91 9910332273


'''
print(color + banner + color)
url = 'https://thehackernews.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
headings = soup.findAll('h2', class_="home-title")
print(' ')
x = 0
for i in headings:
    heading = str(i)
    title = heading[23:-5]
    print(w + '     [' + w + color + str(x) + color + w +'] ' + w + color + title +color)
    x += 1
print(' ')
news = int(input(w + '     [+] ' + w + color + 'Enter the number of news You want to read: ' + color))
link = []
for links in soup.findAll('a', class_='story-link'):
    link.append(links.get('href'))
def para(number):
    _new_url = link[number]
    _response = requests.get(_new_url)
    _soup = BeautifulSoup(_response.content, 'html.parser')
    blog = _soup.find('div', id="articlebody")
    print(blog.text)
    
para(news)
