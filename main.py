import SilverBotFN
intro = Fore.LIGHTGREEN_EX + """
██╗░░██╗ ██╗░░░░░██╗░░░░░██████╗
██║░██╔╝ ██║░░░░░██║░░░░░██╔══██╗
█████═╝  ██║░░░░░██║░░░░░██║░░██║
██╔═██╗  ██║░░░░░██║░░░░░██║░░██║
██║░╚██╗ ██║░░░░░██║░░░░░██████╔╝
╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝
"""

print(intro)

response = requests.get("https://cdn2.klld.tk/api/v1/status")
patch = response.json()["currentFortniteVersion"]

response = requests.get("https://cdn2.klld.tk/api/v1/status")
LOAD = response.json()["LOAD"]



print(f'{LOAD}.\n')
print(f'{patch}.\n')
