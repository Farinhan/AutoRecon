#!/usr/bin/env python
# By : Farinha
# ----

# Libs
import os.path
from importlib.metadata import requires
import os
from re import S
import re
import time
import requests
import subprocess
import argparse
import bs4
from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
import urllib
import urllib3
from urllib.request import urlparse
# Ricing
from rich import print
from rich.prompt import Prompt
from rich.progress import track
from rich.console import Console
from time import sleep
from pathlib import Path
from urllib import request,error,parse
import sys

# --------------------

os.system('clear')

banner = (''' 
[sea_green3]---------------[/]
[sea_green3]-[/] [bold]By: Farinha[/] [sea_green3]-[/]
[sea_green3]---------------[/]        
          ''')

print(banner)
time.sleep(1)

console = Console()
prompt = Prompt()

# --------------------

parser = argparse.ArgumentParser(description="Run to code = python3 farinito.py FileToUrls ")

parser.add_argument("-d", "--domain", type=str, help='Target', required=False)
parser.add_argument("-s", "--scraping", help="Scraping", required=False,
                    action="store_true")
parser.add_argument("-e", "--enum", help="Auto-Enum", required=False,
                    action="store_true")
parser.add_argument("-p", "--port", help="Port Scan", required=False,
                    action="store_true")
parser.add_argument("-g", "--git", help="Procura por Git-Exposed", required=False,
                    action="store_true")
parser.add_argument("-c", "--checkurl", help="Info da URL", required=False,
                    action="store_true")
parser.add_argument("-bd", "--brute", help="Brute-Force Diretórios", required=False,
                    action="store_true")
parser.add_argument("-f", "--findcve", help="Procura por coisas interessantes :)", required=False,
                    action="store_true")

args = parser.parse_args()

# --------------------

def check_url():
    if 'https://' in args.domain:
        print('[red][bold]Sem[/][/] HTTPS')
        exit()
    elif 'http://' in args.domain:
       print('[red][bold]Sem[/][/] HTTP')
       exit()

# --------------------

def check_url_scraping():
    if not 'https://' in args.domain:
        print('[red][bold]Precisa[/][/] HTTPS')
        exit()
        
# --------------------
   
def path():
    arq = Path(args.domain)
    
    if arq.is_dir():
        print('')
    else:
        print('[steel_blue1][bold]> Criando diretório de output[/][/]')
        print('[magenta][bold]>>> Diretório criado com sucesso![/][/]')
        time.sleep(1.2)
        print()
        os.system('mkdir '+args.domain)
        
# --------------------

def path_txt():
    if(os.path.isfile('alive.txt')):
        print('')
    else:
        print('[red]>> Vc precisa de um arquivo alive.txt com seus hosts dentro.')
        time.sleep(3)
        exit()

# --------------------

def enum():

    # ----- AMASS ----- #
    
    def amasss():
        console.log('[sea_green3][bold]!> AMASS Enum[/][/]')
        os.system('amass enum -passive -norecursive -nolocaldb -noalts -d '+args.domain+' >> '+args.domain+'/amass.txtls')
        print()
    with console.status('[sea_green3]!>[/] [bold]Realizando Amass...[/]') as farinha:
        amasss()
        print('[magenta][bold]>> AMASS Terminado')
        print()
    
    # ----- WayBackEngine ----- #
        
    def waybackenginee():
        print()
        console.log('[steel_blue1][bold]> WayBackEngine Enum[/][/]')
        os.system('curl -sk "http://web.archive.org/cdx/search/cdx?url=*.'+args.domain+'&output=txt&fl=original&collapse=urlkey&page=" | awk -F / \'{gsub(/:.*/, \"\", $3); print $3}\' | anew | sort -u >> '+args.domain+'/wayback.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via WAYBACKENGINE[/]') as lindo:
        waybackenginee()
        print()
        print('[magenta][bold]>> WayBackEngine Terminado')
        print()
        print()
        
    # ----- JLDC ----- #
    
    def jldcc():
        console.log('[sea_green3][bold]> JLDC Enum[/][/]')
        os.system('curl -s \"https://jldc.me/anubis/subdomains/'+args.domain+'\" | grep -Po \"((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+\" | sort -u | anew >> '+args.domain+'/jldc.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via JLDC[/]') as muito:
        jldcc()
        print()
        print('[magenta][bold]>> JLDC Terminado')
        print()
        print()
    
    # ----- CRT ----- #
    
    def crtt():
        time.sleep(2)
        console.log('[steel_blue1][bold]> Enumerando via CRT[/][/]')
        time.sleep(2)
        os.system('curl -s \"https://crt.sh/?q=%25.'+args.domain+'&output=json\" | jq -r \'.[].name_value\' | sed \'s/\*\.//g\' | sort -u >> '+args.domain+'/crt.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via CRT[/]') as lindinho:
        crtt()
        print()
        print('[magenta][bold]>> CRT Terminado')
        print()
        print()
        
    # ----- RIDDLER ----- #
    
    def riddlerr():
        console.log('[sea_green3][bold]> Enumerando via RIDDLER[/][/]')
        os.system('curl -s \"https://riddler.io/search/exportcsv?q=pld:'+args.domain+'\" | grep -Po \"(([\w.-]*)\.([\w]*)\.([A-z]))\w+\" | sort -u >> '+args.domain+'/riddler.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via RIDDLER[/]') as mesmoo:
        riddlerr()
        print()
        print('[magenta][bold]>> RIDDLER Terminado')
        print()
        print()
    
    # ----- FINDOMAIN ----- #
    
    def findomainn():
        time.sleep(2)
        console.log('[steel_blue1][bold]> Enumerando via FINDOMAIN[/][/]')
        time.sleep(2)
        os.system('findomain -t '+args.domain+' -q >> '+args.domain+'/findomain.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via FINDOMAIN[/]') as oobaa:
        findomainn()
        print()
        print('[magenta][bold]>> FINDOMAIN Terminado')
        print()
        print()
        
    # ----- SUBFINDER ----- #
    
    def subfinderr():
        console.log('[sea_green3][bold]> Enumerando via SUBFINDER[/][/]')
        os.system('echo '+args.domain+' | subfinder -all -silent | anew >> '+args.domain+'/subfinder.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via SUBFINDER[/]') as escolachata:
        subfinderr()
        print()
        print('[magenta][bold]>> SUBFINDER Terminado')
        print()
        print()
        
    # ----- GOSPIDER ----- #
    
    def gospiderr():
        console.log('[steel_blue1][bold]> Enumerando via GOSPIDER[/][/]')
        os.system('gospider -d 0 -s \"https://'+args.domain+'\" -c 5 -t 100 -d 5 --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt | grep -Eo \'(http|https)://[^/"]+\' | grep '+args.domain+' | anew >> '+args.domain+'/gospider.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via GOSPIDER[/]') as englishh:
        gospiderr()
        print()
        print('[magenta][bold]>> GOSPIDER Terminado')
        print()
        print()
    
    # ----- SCILLA ----- #
    
    def scillaa():
        console.log('[sea_green3][bold]> Enumerando via SCILLA[/][/]')
        os.system('scilla subdomain -plain -target '+args.domain+' | anew >> '+args.domain+'/scilla.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via SCILLA[/]') as concordo:
        scillaa()
        print()
        print('[magenta][bold]>> SCILLA Terminado')
        print()
        print()
        
    # ----- ASSETFINDER ----- #
    
    def assetfinderr():
        console.log('[sea_green3][bold]> Enumerando via ASSETFINDER[/][/]')
        os.system('assetfinder --subs-only '+args.domain+' | anew >> '+args.domain+'/assetfinder.txtls')
    with console.status('[sea_green3]!>[/] [bold]Enumerando via ASSETFINDER[/]') as yepp:
        assetfinderr()
        print()
        print('[magenta][bold]>> ASSETFINDER Terminado')
        print()
        print()
        
    # ----- TASKS ----- #
    
    def tarefitas():
        console.log('[steel_blue1][bold]> Realizando Tarefas[/][/]')
        os.system('cat '+args.domain+'/* | anew >> all_'+args.domain+'.txt')
    with console.status('[sea_green3]!>[/] [bold]Realizando Tarefas[/]') as suuu:
        tarefitas()
        print()
        print('[magenta][bold]>> Tarefas Terminadas')
        print()
        print()

# -----------------------------
    
def scraping(): # creditos jaah
    links_intern = set()
    input_url = args.domain
    depth = 100
    
    links_extern = set()
    
    def level_crawler(input_url):
        temp_urls = set()
        current_url_domain = urlparse(input_url).netloc
    
        beautiful_soup_object = BeautifulSoup(
            requests.get(input_url).content, "lxml")

        for anchor in beautiful_soup_object.findAll("a"):
            href = anchor.attrs.get("href")
            if(href != "" or href != None):
                href = urljoin(input_url, href)
                href_parsed = urlparse(href)
                href = href_parsed.scheme
                href += "://"
                href += href_parsed.netloc
                href += href_parsed.path
                final_parsed_href = urlparse(href)
                is_valid = bool(final_parsed_href.scheme) and bool(
                    final_parsed_href.netloc)
                if is_valid:
                    if current_url_domain not in href and href not in links_extern:
                        print("Externo - {}".format(href))
                        links_extern.add(href)
                    if current_url_domain in href and href not in links_intern:
                        print("Interno - {}".format(href))
                        links_intern.add(href)
                        temp_urls.add(href)
        return temp_urls
    

    if(depth == 0):
        print("Interno - {}".format(input_url))
    
    elif(depth == 1):
        try:
            level_crawler(input_url)
        except:
            pass
    
    else:

        queue = []
        queue.append(input_url)
        with open('scraping.txt', 'w') as fp:
            for j in range(depth):
                for count in range(len(queue)):
                    url = queue.pop(0)
                    urls = level_crawler(url)
                    for i in urls:
                        queue.append(i)
                        fp.write(i + '\n')
                        fp.flush()

# -----------------------------

def port():
    console.log('[sea_green3][bold]> Port-Scan[/][/]')
    os.system('xargs -a alive.txt -I@ sh -c \'scilla port -plain -target @ >> portscan.txtls\'')
with console.status('[magenta][bold]!> Realizando Port-Scan...[/][/]') as ll:
    port()
    
# -----------------------------

def gitexposed():
    print('[blue][bold]Git Exposed[/][/]')
    time.sleep(2.2)
    os.system('cat all_'+args.domain+'.txt | xargs -I@ sh -c \'goop @ -f\'')

# -----------------------------

def checkurl():
    print()
    print('[slate_blue3][bold]> Check URL[/][/]')
    print('[slate_blue3][bold]> Seu alvo é http ou https?http/https[/][/]')
    checkurlop = input('> ')
    
    if checkurlop == 'https':
        print()
        time.sleep(2.1)
        print('[salmon1][bold]> Realizando check HTTPS[/][/]')
        os.system('cat alive.txt | parallel -j50 -q curl -w \'Status:%{http_code}\t  Size:%{size_download}\t %{url_effective}\n\' -o /dev/null -sk')
        
    elif checkurlop == 'http':
        print()
        time.sleep(2.1)
        print('[slate_blue3][bold]> Realizando check HTTP[/][/]')
        os.system('cat alive.txt | parallel -j50 -q curl -w \'Status:%{http_code}\t  Size:%{size_download}\t %{url_effective}\n\' -o /dev/null -sk')
    else:
        print('[red]Opcao invalida[/]')
        exit()
        
# -----------------------------

def brute():
    print('[sea_green3]>> Brute-Force Diretórios[/]')
    os.system('scilla dir -plain -target '+args.domain+' >> '+args.domain+'/brute.txtls')
with console.status('[magenta][bold]!> Realizando Brute-Force...[/][/]') as kaka:
    brute()

# -----------------------------

def findcve():
    print('[slate_blue3][bold]> FindCve[/][/]')
    time.sleep(2)
    print('[slate_blue3][bold]> Vc deseja ter uma saída limpa ([red]l[/]) ou uma saída com mais detalhes ([red]d[/]) ?l/d[/][/]')
    findcve_op = input("> ")

    
    if findcve_op == 'l':
        print('[salmon1][bold]> Realizando Ataque...[/][/]')
        os.system('curl -s \"https://otx.alienvault.com/api/v1/indicators/domain/'+args.domain+'/url_list?limit=100&page=1\" | jq -r \'.url_list[].url\' | anew >> '+args.domain+'/alienL.txtls')
        print('[salmon1][bold]> Farinha AL Realizado...[/][/]')
    elif findcve_op == 'd':
        print('[salmon1][bold]> Realizando Ataque...[/][/]')
        os.system('curl -s \"https://otx.alienvault.com/api/v1/indicators/domain/'+args.domain+'/url_list?limit=100&page=1\" | jq | anew >> '+args.domain+'/alienD.txtls')
        print('[salmon1][bold]> Farinha AD Realizado...[/][/]')
    else:
        print('[red]Opcao invalida[/]')
        exit()
        
# -----------------------------
 
if args.enum:
    check_url()
    path()
    enum()
    
elif args.scraping:
    check_url_scraping()
    scraping()

elif args.port:
    path_txt()
    port()
    
elif args.git:
    path_txt()
    gitexposed()

elif args.checkurl:
    path_txt()
    check_url()
    
elif args.brute:
    check_url()
    path()
    brute()
    
elif args.findcve:
    check_url()
    path()
    findcve()
    
