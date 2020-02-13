import mechanicalsoup
import base64
import random
import sys

def ptsd(key, enc):
    dec = []
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

data = [('âÊæÍáØÊÛ×ÍÓÐ\x9a¡', '»¶¦\x9d¦¹'), ('Ê×èÇÚÃß', 'ËÑÔ×ÓÖÒâÔ'), ('×ÒÛÆÞ\x93\x9f', 'ÛØÖÐåÖÊÛ¬\x9e«'), ('ÊÊÞÆåÊ\x9a\xa0', 'Êá¢\x96©\x91\x99\x9b¢\x96«\x9b¢'), ('×Êà×æÃ', 'ÒÖáÆßÔÝÊ×ÆäÑÌÑ¤\x97¥\x96\x9e\x9f'), ('ÜÊáÐ×Ö\x9a¡', 'ÂÊä\x95¨\x96¡\x99'), ('ÊÐáÊå\x93¡', 'ÏÛÔÓÕË\x9a\x9b¦'), ('Ø×ÝÆëÃ×Ý¤', '¾ÜØÑÖÃÙ\x9b³\x96©'), ('ÜÜÕÆåËÖ', 'ËÊæÎß\x94\x9a¢¤\x9e¤'), ('ÊÕØÓâ', 'ÊÕØÓâ¢\x9a¢¬\x9b'), ('ÔÞàÔÖ\x93¡', 'ÔÞàÔÖÄÊËÔ\x96¤\x95\x9d'), ('Ê×ÞÎæÃË\x9a©', 'ÛÝÔØÚÔÎÎ¥\x9e'), ('ÖÒæÙÚË\x9a¡', '¿¿¬\x9a¢±'), ('ÙÛÔÓÓÛ\x9a¢', '¹»´³³»\xa0¡¬'), ('ÔÛÜØÚÐÊÙ¤\x9c', '¸ÝÔÐç\x96®ßØ×\x9c')]
u,p = random.choice(data)
k = sys.argv[1]
br= mechanicalsoup.StatefulBrowser()
br.open('http://detectportal.firefox.com/success.txt')
br.select_form('form[action="/"]')
br["username"]=ptsd(k,u)
br["password"]=ptsd(k,p)
print(br.submit_selected())

