#!/usr/bin/env python3
import shodan,time,requests,re

SHODAN_API_KEY = ''
api = shodan.Shodan(SHODAN_API_KEY)

#QUERY = 'ssl:”Covenant” http.component:”Blazor”'
QUERY = 'title:dvwa'

#usernames = ['admin', 'administrator', 'covenant', 'c2admin']
#passwords = ['admin', 'administrator', 'password', '123456', '123456789', 'qwerty']



def request_page_from_shodan(query, page=1):
    while True:
        try:
            instances = api.search(query, page=page)
            return instances
        except shodan.APIError as e:
            print(f"Error: {e}")
            time.sleep(5)


def query_shodan(query):
    print("[*] querying the first page")
    first_page = request_page_from_shodan(query)
    total = first_page['total']
    already_processed = len(first_page['matches'])
    result = process_page(first_page)
    page = 2
    while already_processed < total:
        # break just in your testing, API queries have monthly limits
        break
        print("querying page {page}")
        page = request_page_from_shodan(query, page=page)
        already_processed += len(page['matches'])
        result += process_page(page)
        page += 1
    return result


res = query_shodan(QUERY)
print(res)
