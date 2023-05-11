import requests

quranenc_r = requests.get('https://quranenc.com/api/v1/translations/list')
if quranenc_r.status_code == 200:
   print(quranenc_r.json())
