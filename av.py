#!/system/bin/python
# Autoclicker by Mr.Java404, Improved by ChatGPT

import urllib2
import time
import random
import os
import sys

# Warna Terminal
B = '\033[1m'
R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
BL = '\033[34m'
P = '\033[35m'
W = '\033[37m'
N = '\033[0m'

os.system("clear")

proxy_list = "proxylist.txt"

# Tambahan user-agent Android + lainnya
bacod = [
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-J600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36",
    # Tambahan desktop lama tetap ada juga:
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
]

refferer_list = ['http://google.com','http://bing.com','http://facebook.com','http://twitter.com','http://yahoo.com']

print B+Y+"[+] Masukkan URL Visitor: "+N
ini_url = raw_input("=> ")

def Autoclicker(proxy1):
    try:
        proxy = proxy1.split(":")
        print B+BL+"#-- TARGET --# "+W+proxy1+P+" => Proses..."+N
        proxy_set = urllib2.ProxyHandler({"http": "%s:%d" % (proxy[0], int(proxy[1]))})
        opener = urllib2.build_opener(proxy_set, urllib2.HTTPHandler)
        opener.addheaders = [('User-agent', random.choice(bacod)),
                             ('Referer', random.choice(refferer_list))]
        urllib2.install_opener(opener)
        f = urllib2.urlopen(ini_url, timeout=10)
        if "google.com" in f.read():
            print B+G+"[*] 200 OK"+N
        else:
            print R+"[*] Gagal mengunjungi URL."+N
    except Exception as e:
        print R+"[!] Proxy Error: %s" % e+N
    time.sleep(3)

def loadproxy():
    try:
        with open(proxy_list, "r") as f:
            proxies = [x.strip() for x in f.readlines()]
            return proxies
    except:
        print R+"[!] File proxylist.txt tidak ditemukan!"+N
        sys.exit(1)

def main():
    proxies = loadproxy()
    while True:
        print Y+"[*] Looping ke semua proxy..."+N
        for proxy in proxies:
            Autoclicker(proxy)
        print BL+"[*] Menunggu 10 detik sebelum mengulang..."+N
        time.sleep(10)

if __name__ == '__main__':
    main()
