import requests
import os


# dictionary with a market from every region
dict = {"NO_HB":540933, "NO_HA":540435, "NO_HH":540528,"NO_OW":531050,"MI_MN":1464050,"MI_MD":240314,"MI":240259,
        "MI_MW":1465200,"OS_BB":4040083,"OS_SH":565268,"OS_TH":4040422,"OS_MP":4040770,"OS_SA":4040423,"SU_FR":440483,
        "SU_BY":440775,"WE_DO":1940491,"WE_KN":1765257,"WE_AC":1940280,"WE_DU":1940104,"WE_WW":1765231,"WE_KB":1931020,
        "SW":840908,"SW_SL":840299,"SW_UU":862008,"CY-OS-OC":4040288,"CY-WE-WC":1940087,"CY-NO-NC":531083,
        "CY-MI-MC":241151,"CY-SW-TC":840344,"CY-SU-SC":431035,"RC-MI-1B":240786,"RC-MI-C1":320525,"RC-MI-CJ":240733,
        "RC-MI-CK":240244,"RC-MI-CL":240738,"RC-MI-CM":1461928,"RC-MI-CN":240737,"RC-MI-CY":1465117,"RC-NO-CB":540184,
        "RC-NO-CH":540350,"RC-NO-CO":541745,"RC-NO-RG":531077,"RC-NO-RW":531076,"RC-NO-S2":531128,"RC-OS-C2":4031022,
        "RC-OS-CE":4031024,"RC-OS-CF":4031003,"RC-OS-CI":4031001,"RC-OS-CQ":1931370,"RC-SU-C5":431033,"RC-SU-C7":431031,
        "RC-SU-C8":431081,"RC-SU-CS":440300,"RC-SW-1C":840956,"RC-SW-2C":831083,"RC-SW-3C":841041,"RC-SW-9C":831057,
        "RC-SW-CP":831084,"RC-WE-5B":1940164,"RC-WE-5M":1940256,"RC-WE-5O":1940158,"RC-WE-5W":1940255,"RC-WE-AA":1940076,
        "RC-WE-DN":1940140,"RC-WE-KL":1940286,"RC-WE-WS":1761496,"PZ-SA":8534516,"PZ-W1":8534505,"PZ-W2":8534545,
        "PZ-W3":8534530,"PZ-W4":8534566,"PZ-W5":8534580,"WE-KB_FF-NF-HM-P063":1761063}


def get_prospekte(dict):
    '''
    downloads Prospekte to a folder in the same directory
    '''
    counter = 0
    for key, value in dict.items():
        counter += 1
        try:
            req1 = requests.get(f'https://www.bonialserviceswidget.de/de/v4/stores/{value}?externalStore=true&publisherId=1062')
            resp1 = req1.json()
            bonialId = resp1["id"]

            req2 = requests.get(f'https://www.bonialserviceswidget.de/de/stores/{bonialId}/brochures')
            resp2 = req2.json()
            # index depending on how many brochures are available
            contentId = resp2["brochures"][0]["contentId"]

            r3 = requests.get(f'https://aws-ops-bonial-biz-production-published-content-pdf.s3-eu-west-1.amazonaws.com/{contentId}/{contentId}.pdf').content

            if not os.path.exists('REWE_Prospekte'):
                os.makedirs('REWE_Prospekte')
            with open(f'REWE_Prospekte\\{key}-{value}.pdf', 'wb') as file:
                file.write(r3)
        except:
            print(f'{key}-{value} does not exist')

        print(counter)

if __name__ == '__main__':
    get_prospekte(dict)