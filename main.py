import wikipediaapi


def read_titles(filename):
  with open(filename, 'r') as file:
    for line in file:
      yield line.strip()


def get_article(title,lang="en"):
  w_api = wikipediaapi.Wikipedia(lang)
  page = w_api.page(title)
  if page.exists():
    return page.text
  else:
    return ""

def srednia_ilosc():
  wszytstkieLitery=0
  iloscArtykulow=0

  for title in read_titles():
    artykul=get_article(title)
    if artykul:
        wszytstkieLitery+=len(artykul)
        iloscArtykulow +=1

  if iloscArtykulow>0:
    sredniaLiter= wszytstkieLitery /iloscArtykulow
    return sredniaLiter
  else:
    print("Nie ma artykulow ")
    return 0

print("Srednia liczba liter w artykule= "+sredniaLiter)


title =  next(titles_gen)
print(title)
title =  next(titles_gen)
print(title)
