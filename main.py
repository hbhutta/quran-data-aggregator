import requests


def getQuote(sura: int, ayaRangeStart: int, ayaRangeEnd: int, includeTranslation: bool) -> str:
  # ayaRangeEnd += 1

  apiLinkForSura = f'https://quranenc.com/api/v1/translation/sura/english_saheeh/{sura}'
  apiLinkForAya = ''

  suraAPI = requests.get(apiLinkForSura)
  
  ayaAPI = ''

  if (1 <= sura and sura <= 114): # Sura number limit is 114
    suraJson = suraAPI.json()
    ayaLimit = len(suraJson["result"])
    print(f"This sura has {ayaLimit} ayat")

    if (1 <= ayaRangeStart and ayaRangeStart <= ayaLimit) and (1 <= ayaRangeEnd and ayaRangeEnd <= ayaLimit):
      if includeTranslation:
        for ayaNumber in range(ayaRangeStart, ayaRangeEnd + 1): # +1 so that ayaRangeEnd aya is included
          apiLinkForAya = f'https://quranenc.com/api/v1/translation/aya/english_saheeh/{sura}/{ayaNumber}'
          ayaAPI = requests.get(apiLinkForAya)
          json = ayaAPI.json()
          quote = json["result"]["arabic_text"]
          quoteTranslation = json["result"]["translation"]
          print(quote + " " + quoteTranslation + " ")
    else:
      print("Aya range(s) out of bounds")
      pass
  else:
    print("Sura range(s) out of bounds")
    pass

getQuote(1, 1, 7, True) # First aya of Al-Fatihah is bismillah
