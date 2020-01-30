import mechanicalsoup
import base64
import random
import sys

def ptsd(enc,k):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = k[i % len(k)]
        dec_c = chr((256 + enc[i] - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

data = [('4srmzeHYytvXzdPQmqE=', 'u7amnaa5'), ('ytfox9rD3w==', 'y9HU19PW0uLU'), ('19Lbxt6Tnw==', '29jW0OXWytusnqs='), ('ysrexuXKmqA=', 'yuGilqmRmZuilqubog=='), ('3Mrh0NfWmqE=', 'wsrklaiWoZk='), ('ytDhyuWToQ==', 'z9vU09XLmpum'), ('2NfdxuvD192k', 'vtzY0dbD2Zuzlqk='), ('ytTmzdPbmqA=', 'ytTmzdPbmqA='), ('1N7g1NaToQ==', '1N7g1NbEysvUlqSVnQ==')]

u,p = random.choice(data)
k = sys.argv[1]
br= mechanicalsoup.StatefulBrowser()
br.open('http://detectportal.firefox.com/success.txt')
br.select_form('form[action="/"]')
br["username"]=ptsd(u,k)
br["password"]=ptsd(p,k)
print(br.submit_selected())

