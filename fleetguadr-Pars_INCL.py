import time
import requests
import csv
def Related_Parts(name):
    cookies = {
        'renderCtx': '%7B%22pageId%22%3A%22ebcd21da-8a79-4eb6-b8fd-5ce014c275f4%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%22ba420390-c555-4ca2-83b8-daa0a923a648%22%2C%22audienceIds%22%3A%22%22%7D',
        'CookieConsentPolicy': '0:1',
        'LSKey-c$CookieConsentPolicy': '0:1',
        '_gcl_au': '1.1.1690850232.1712831388',
        '_ga': 'GA1.1.447288166.1712831389',
        'pctrk': 'e4d245f2-6cbe-4c7d-9f15-35947aab87de',
        'OptanonAlertBoxClosed': '2024-04-11T10:30:27.191Z',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Apr+15+2024+15%3A58%3A36+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0002%3A1%2CC0003%3A1%2CC0001%3A1%2CC0004%3A1&geolocation=RU%3BROS&AwaitingReconsent=false',
    }

    headers = {
        'authority': 'www.fleetguard.com',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'renderCtx=%7B%22pageId%22%3A%22ebcd21da-8a79-4eb6-b8fd-5ce014c275f4%22%2C%22schema%22%3A%22Published%22%2C%22viewType%22%3A%22Published%22%2C%22brandingSetId%22%3A%22ba420390-c555-4ca2-83b8-daa0a923a648%22%2C%22audienceIds%22%3A%22%22%7D; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1; _gcl_au=1.1.1690850232.1712831388; _ga=GA1.1.447288166.1712831389; pctrk=e4d245f2-6cbe-4c7d-9f15-35947aab87de; OptanonAlertBoxClosed=2024-04-11T10:30:27.191Z; _ga_3E46LFE2XH=GS1.1.1713185610.17.1.1713185916.59.0.1120126586; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+15+2024+15%3A58%3A36+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202303.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0002%3A1%2CC0003%3A1%2CC0001%3A1%2CC0004%3A1&geolocation=RU%3BROS&AwaitingReconsent=false; _dd_s=rum=1&id=979825bc-2146-4ce6-a794-0e29dcf73ee2&created=1713185610884&expire=1713186815433',
        'origin': 'https://www.fleetguard.com',
        'referer': f'https://www.fleetguard.com/s/productDetails?propertyVal={name}&propertyField=home&language=en_US',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
        'x-sfdc-lds-endpoints': 'ApexActionController.execute:Replacement_and_Upgrade.replace_and_upgrade',
    }

    params = {
        'r': '10',
        'aura.ApexAction.execute': '1',
    }

    data = {
        'message': f'{{"actions":[{{"id":"82;a","descriptor":"aura://ApexActionController/ACTION$execute","callingDescriptor":"UNKNOWN","params":{{"namespace":"","classname":"Replacement_and_Upgrade","method":"replace_and_upgrade","params":{{"product_value":"{name}","effAccountId":null,"countryCode":"US"}},"cacheable":true,"isContinuation":false}}}}]}}',
        'aura.context': '{"mode":"PROD","fwuid":"ZDROWDdLOGtXcTZqSWZiU19ZaDJFdzk4bkk0bVJhZGJCWE9mUC1IZXZRbmcyNDguMTAuNS01LjAuMTA","app":"siteforce:communityApp","loaded":{"APPLICATION@markup://siteforce:communityApp":"XvLrnsfis-Fl75QQFAqN9A","COMPONENT@markup://instrumentation:o11ySecondaryLoader":"nSN3-Xh18FbrdCVGqsWZnw"},"dn":[],"globals":{},"uad":false}',
        'aura.pageURI': f'/s/productDetails?propertyVal={name}&propertyField=home&language=en_US',
        'aura.token': 'null',
    }

    response = requests.post('https://www.fleetguard.com/s/sfsites/aura', params=params, cookies=cookies,
                             headers=headers, data=data).json()

    return response


def main():
    with open("fleetguard_txt.txt", 'r') as file:
        items = [line.strip() for line in file]

    names = []
    includes_list = []
    companies = []
    k =0

    for name in items:
        k += 1
        Related_Parts = Related_Parts(name)
        try:
            includes = Related_Parts['actions'][0]['returnValue']['returnValue']['Includes'].split(",")
            for inc in includes:
                names.append(name)
                includes_list.append(inc)
                companies.append("FLEETGUARD")

        except:
            print(f"нет includes у детали {name}")
            names.append(name)
            includes_list.append("-")
            companies.append("FLEETGUARD")

        time.sleep(3)

        if k == 500:
            with open('fleetguard.csv', 'a', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                for company, name, include in zip(companies, names, includes_list):
                    # Формируем строку для записи
                    flatten = company,name,include
                    writer.writerow(flatten)
            print(f"Excel файл fleetguard.csv успешно создан.")

            # Сброс счетчика и списков
            k = 0
            companies = []
            names = []
            includes_list = []

    # Если остались данные после завершения цикла, сохраняем их
    if companies:
        with open('fleetguard.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for company, name, include in zip(companies, names, includes_list):
                # Формируем строку для записи
                flatten = company, name, include
                writer.writerow(flatten)
        print(f"Excel файл fleetguard.csv успешно создан.")


if __name__ == '__main__':
    main()