import csv
import os
import requests
from pprint import pprint

'''
Gets data of (verse/ayah, translation) pair for each verse in sura, given the sura number
Puts data into dictionary, which is converted into a pandas dataframe
'''

if not os.path.exists('quran'):
   os.makedirs('quran')

for chapter in range(1,115):
  with open(f'quran/{chapter}.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['surah_num', 'verse_num', 'verse', 'translation'])

    sura_api_link = f'https://quranenc.com/api/v1/translation/sura/english_saheeh/{chapter}'
    sura_api = requests.get(sura_api_link)
    sura_json = sura_api.json()
    total_ayas = len(sura_json['result'])

    for aya in range(1, total_ayas+1):
      apiLinkForAya = f'https://quranenc.com/api/v1/translation/aya/english_saheeh/{chapter}/{aya}'
      ayaAPI = requests.get(apiLinkForAya)
      json = ayaAPI.json()

      quote = json["result"]["arabic_text"]
      quoteTranslation = json["result"]["translation"]

      # Verse number | Verse | Translation
      writer.writerow([chapter, aya, quote, quoteTranslation])



