## Fitur
- Looping otomatis – akan mengunjungi URL target menggunakan semua proxy di file proxylist.txt, lalu mengulang lagi.
- User-Agent acak – berpura-pura jadi perangkat Android/Windows agar terlihat seperti pengunjung asli
- Referer acak – misalnya Google, Bing, Facebook, supaya kunjungan terlihat datang dari berbagai sumber.

## Instalasi & Menjalankan
1. update paket
```
 pkg update && pkg upgrade -y

```
2. Install Python2 & git
```
 pkg install python2 git -y
```
3. Clone Repo
```
  https://github.com/topibajaa/autovisitor.git
```
4. Run
```
  python2 av.py
```
