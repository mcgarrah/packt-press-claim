#!/usr/bin/env python

"""packt.py: Grab the daily free book claim from Packt Press.

 This will run under Python 2.7 and 3.4 with minimum dependencies.
 The goals was the most simplistic code that will function. The
 script can be run from cron.

 Replace the two lines with username/email and password with your
 credentials.

 Depends on:
   requests
   beautifulsoup

 The code is heavily influenced by:
   https://github.com/movb/packt-grabber
   https://github.com/igbt6/Packt-Publishing-Free-Learning
   https://github.com/niqdev/packtpub-crawler

"""

__author__  = "Michael McGarrah"
__email__   = "mcgarrah@mcgarrah.org"
__version__ = "0.1.0"

import sys
import requests
from bs4 import BeautifulSoup

email    = 'CHANGE_ME@google.com'
password = 'CHANGE_ME_TOO'


base_url = 'https://www.packtpub.com'
free_url = 'https://www.packtpub.com/packt/offers/free-learning'

headers = {'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

if __name__ == "__main__":

    s = requests.Session()
    r = s.get(free_url, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text)

    form = soup.find('form', {'id': 'packt-user-login-form'})
    if form is None:
        print 'Cannot find login form'
        sys.exit()

    form_build_id = form.find('input', attrs={'name': 'form_build_id'})['value']
    if form_build_id is None:
        print 'Cannot find build_id'
        sys.exit()

    form_id = form.find('input', attrs={'name': 'form_id'})['value']
    if form_id is None:
        print 'Cannot find form_id'
        sys.exit()

    post_payload = {
        'email': email,
        'password': password,
        'op': 'Login',
        'form_build_id': form_build_id,
        'form_id': form_id
    }

    r = s.post(free_url, headers=headers, data=post_payload)
    soup = BeautifulSoup(r.text)

    login_error = soup.find('div', {'class': 'messages error'})
    if login_error is not None:
        print 'Login failed'
        sys.exit()

    print 'Logged into Packt'

    deal_of_day = soup.find('div', {'id': 'deal-of-the-day'})
    if deal_of_day is None:
        print 'No deal of day found'
        sys.exit()

    claim_url = soup.find('a', class_='twelve-days-claim')['href']
    if claim_url is None:
       print 'Cannot find claim url'
       sys.exit()

    r = s.get(base_url + claim_url, headers=headers)
    if r.status_code != 200:
       print 'Claim failed for book. Likely bad credentials'
       sys.exit()
    soup = BeautifulSoup(r.text)

    account_list = soup.find('div', {'id': 'product-account-list'})
    if account_list is None:
       print 'Cannot access claim page. Probably bad credentials'
       sys.exit()

    print 'Claim processed'
