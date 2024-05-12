
# ███╗░░░███╗██████╗░  ░█████╗░░█████╗░██████╗░██╗███████╗  ██╗██╗░░
# ████╗░████║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝  ╚═╝╚██╗░
# ██╔████╔██║██████╔╝  ██║░░╚═╝██║░░██║██║░░██║██║█████╗░░  ░░░░╚██╗
# ██║╚██╔╝██║██╔══██╗  ██║░░██╗██║░░██║██║░░██║██║██╔══╝░░  ░░░░██╔╝
# ██║░╚═╝░██║██║░░██║  ╚█████╔╝╚█████╔╝██████╔╝██║███████╗  ██╗██╔╝░
# ╚═╝░░░░░╚═╝╚═╝░░╚═╝  ░╚════╝░░╚════╝░╚═════╝░╚═╝╚══════╝  ╚═╝╚═╝░░



# 𝔡𝔬 𝔰𝔲𝔟𝔰𝔠𝔯𝔦𝔟𝔢 𝔱𝔬 𝔪𝔶 𝔠𝔥𝔞𝔫𝔫𝔢𝔩


















# ===========================================> Subscibe To Mr Codie <=====================================================

import requests
import json
from time import time as t
import dotenv ;dotenv.load_dotenv()
import os
from colorama import Fore
import colorama
colorama.init(autoreset=True)


session = os.environ['Session']
Cookie = os.environ['cookie']


Rs = requests.Session()



def Text_Generation_Pi(Promt:str):
    c= t()
    API = 'https://pi.ai/api/chat'



    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/event-stream',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Cookie': Cookie,
    }


   
    payload = {
        'text': f'{Promt}',
        'conversation': session
    }

    response = Rs.post(url=API, data=json.dumps(payload), headers=headers, stream=True)

    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                try:
                    line_str = line.decode('utf-8')
                    if 'data' in line_str:
                        data_json = json.loads(line_str.split('data: ')[1])
                        if 'text' in data_json:
                            yield data_json['text']
                except Exception as e:
                    print(e)
        print(f"\n{Fore.MAGENTA+str(t()-c)}")
        
    else:
        print(f"Error {response.status_code}")




if __name__=="__main__":
    while 1:
        for i in Text_Generation_Pi(str(input("\n>>> "))):
            print(Fore.GREEN+i, end="",flush=True)
        print("\n")
