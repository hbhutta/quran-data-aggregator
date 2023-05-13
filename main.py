import requests




def getQuote(sura: int, aya: int, ayaRange: int) -> str:
  # sura = int(input("Enter sura #: "))
  # aya = int(input("Enter aya #: "))

  apiLinkForSura = f'https://quranenc.com/api/v1/translation/sura/english_saheeh/{sura}'
  apiLinkForAya = ''

  suraAPI = requests.get(apiLinkForSura)
  ayaAPI = ''

  if (1 <= sura and sura <= 114): # Sura number limit is 114
    suraJson = suraAPI.json()
    ayaLimit = len(suraJson["result"])

    if (range <= ayaLimit):
      for ayaNumber in range(ayaRange):





    # if (1 <= aya and aya <= ayaLimit): # Aya limit for that specific sura
      apiLinkForAya = f'https://quranenc.com/api/v1/translation/aya/english_saheeh/{sura}/{aya}'
      ayaAPI = requests.get(apiLinkForAya)
      json = ayaAPI.json()
      quote = json["result"]["arabic_text"]
      print(quote)
  else:
    print(-1)
    quit()
  pass


# quranenc = requests.get(api)
# json = ''
# if quranenc.status_code == 200:
#   json = quranenc.json()
#   whatWeWant = json["result"]["arabic_text"]
#   print(whatWeWant)
# else:
#   print("-1")
#   quit()

# '''
# Return: The specified surah verse
# Constraints: 1 <= surah <= 114 && 
# '''
# def getText(surah: int, verse: int) -> str:
#   text = ''
#   if verseInBounds(surah, verse):
#       text = surahJson["result"][verse]["arabic_text"]
#   return text

# def verseInBounds(surah: int, verse: int) -> bool:
#   if (1 <= surah and surah <= 114):
#     surahJson = quranenc.json()
#     surahVerseLimit = len(surahJson["result"])
#     assert type(surahVerseLimit) == int
#     if (1 <= verse and verse <= surahVerseLimit):
#       return True
#   else:
#     return False

# surah = 2
# verse = 1
# print(getText(surah,verse))
