import requests

sura = input("Enter sura #: ")
aya = input("Enter aya #: ")

apiForSura = f'https://quranenc.com/api/v1/translation/sura/english_saheeh/{sura}'
apiForVerse = ''

suraAPI = requests.get(apiForSura)

if (1 <= sura && sura <= 114): # Sura number limit is 114
  ayaLimit = -1
  if (1 <= aya && aya <= ayaLimit):
    api = f'https://quranenc.com/api/v1/translation/aya/english_saheeh/{sura}/{aya}'
quranenc = requests.get(api)
json = ''
if quranenc.status_code == 200:
  json = quranenc.json()
  whatWeWant = json["result"]["arabic_text"]
  print(whatWeWant)
else:
  print("-1")
  quit()

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
