import requests
import os
import re
from colorama import Fore

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def title(args):
    if args == None:
        os.system("title Email Splicer") if os.name == "nt" else None
    else:
        os.system(f"title Email Splicer [~] {args}") if os.name == "nt" else None



email = ""

while email != "EXIT":
    title(None)
    clear()

    email = input(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Email: ")
    title_1= f"Splicing - {email}"
    title(title_1)
    email_spliced = email.split('@')

    start = email_spliced[0]

    end = email_spliced[1]

    company = end.split('.')

    print(f"""
{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET}========================={Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET}

       - Email splicer -

{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET}========================={Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET}
    """)

    print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Original:", email)
    print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Length:", len(email))
    print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Start:", start)
    print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} End:", end)

    emaillist = [
    'outlook$c$Microsoft', 
    'gmail$c$Google', 
    'protonmail$c$Proton', 
    'yahoo$c$Microsoft', 
    'hotmail$c$Microsoft', 
    'aol$c$Aol', 
    'yandex$c$Yandex', 
    'yandexmail$c$Yandex'
    ]

    thing = False
    for email_start in emaillist:
        email_prov = email_start.split('$c$')

        if email_prov[0] == company[0]:
            thing = True
            print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Email type: {email_prov[0]}")
            print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Company: {email_prov[1]}")
    if thing != True:
            print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Email type: None found")
            print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Company: None found")        



    bad_requests = [400, 404, 999]

    sites = [
        f'https://www.youtube.com/@{start}',
        f'https://github.com/{start}',
        f'https://replit.com/@{start}',
        f'https://www.pornhub.com/users/{start}',
        f'https://www.pornhub.com/model/{start}',
        f'https://www.xvideos.com/channels/{start}',
        f'https://www.redtube.com/channels/{start}',
        f'https://www.redtube.com/pornstar/{start}',
        f'https://www.roblox.com/user.aspx?username={start}',
        f'https://m.twitch.tv/{start}',
        f'https://www.tiktok.com/@{start}',
        f'https://www.linkedin.com/in/{start}?trk=people-guest_people_search-card',
        f'https://www.tumblr.com/{start}',
    ]


    #This will attempt to get the user from a 
    #list of sites, sites typically return a    
    #200 when valid so I filter out other codes.


    print("\n+--<*>--+ Sites +--<*>--+\n")


    for site in sites:

        
        response = requests.get(site)
        if response.status_code not in bad_requests:
            print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Start of email found on | {site} | {response.status_code}")



    input(f"\n{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Press enter to exit...")

