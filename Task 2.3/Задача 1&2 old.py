import json
from xml.etree import ElementTree as et

origin = []


def nor(p):
    return p.lower().strip().split()


def text(u):
    if u[-1] == 'n':
        with open(u, encoding='utf-8') as f:
            inf = json.load(f)
            inf = inf['rss']['channel']
            origin.append(nor(inf['title']))
            origin.append(nor(inf['description']))
            for i in inf['items']:
                origin.append(nor(i["description"]))
                origin.append(nor(i["title"]))
    elif u[-1] == 'l':
        media = et.parse('newsit.xml')
        tv = media.find('channel')
        origin.append(nor(tv.find('title').text))
        origin.append(nor(tv.find('description').text))
        news = tv.findall('item')
        for n in news:
            origin.append(nor(n.find('title').text))
            origin.append(nor(n.find('description').text))
    else:
        print("Такого файла нет")


te = input("Введите название файла ")
text(te)

fix = lambda l: sum(l, [])
origin = fix(origin)

seven = list(filter(lambda s: len(s) > 6, origin))

half_final = sorted(seven, key=seven.count)
half_final.reverse()

final = [half_final[0]]

p = 1
while len(final) < 10:
    if half_final[p] not in final:
        final.append(half_final[p])
    p += 1


def razz(o):
    o = str(o)
    if (o[len(o) - 1] == '2') or (o[len(o) - 1] == '3') or (o[len(o) - 1] == '4'):
        return "раза"
    else:
        return "раз"


print('')
for i in range(10):
    f1 = i + 1
    f2 = final[i]
    f3 = half_final.count(final[i])
    f4 = razz(half_final.count(final[i]))
    print("{} место - \"{}\", упоминается {} {}".format(f1, f2, f3, f4))
