import requests
import os
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

    email = input("Email: ")
    title_1= f"Splicing - {email}"
    title(title_1)
    email = email.split('@')

    start = email[0]

    end = email[1]

    company = end.split('.')

    print(f"""
{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET}========================={Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET}

       - Email splicer -

{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET}========================={Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET}
    """)


    print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Start:", start)
    print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} End:", end)

    emaillist = [
    'outlook', 
    'gmail', 
    'protonmail', 
    'yahoo', 
    'hotmail', 
    'aol', 
    'yandex', 
    'yandexmail'
    ]



    if company[0] in emaillist:
        print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Email ending found in database")
    else:
        print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Email type not in database")




    bad_requests = [400, 404, 999]

    sites = [
        f'https://www.youtube.com/@{start}',
        f'https://github.com/{start}',
        f'https://replit.com/@{start}',
        f'https://www.pornhub.com/users/{start}',
        f'https://www.roblox.com/user.aspx?username={start}',
        f'https://m.twitch.tv/{start}',
        f'https://www.tiktok.com/@{start}',
        f'https://www.linkedin.com/in/{start}?trk=people-guest_people_search-card',
        f'https://www.tumblr.com/{start}'
    ]


    #This will attempt to get the user from a 
    #list of sites, sites typically return a 
    #200 when valid so I filter out other codes.


    print("\n+--<*>--+ Sites +--<*>--+\n")


    for site in sites:
        response = requests.get(site)
        if response.status_code not in bad_requests:
            print(f"{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Start of email found on | {site} | {response.status_code}")



    input("\n{Fore.RED}[{Fore.RESET}?{Fore.RED}]{Fore.RESET} Press enter to exit...")

