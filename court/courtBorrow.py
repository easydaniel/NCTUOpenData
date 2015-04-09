from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

# {日期:{地點:{時段}}}

sections = ['早上','中午','下午','晚上']
place = ['活動中心:四樓聯誼廳', '活動中心:一樓聯誼廳', '活動中心:二樓聯誼廳', '活動中心:B1 聯誼廳', '活動中心:露天劇場', '活動中心:思源前廊', '活動中心:地下室中庭', '活動中心:一樓中庭', '活動中心:三樓中庭', '活動中心:中正堂聯誼廳', '活動中心:四樓陽台', '活動中心:溜冰場', '活動中心:五樓陽台','韻律教室']
output = {}
pDict = {} 
sDict = {}
listOfFM = ['club','event','telephone']

courtUrl = 'https://sasystem.nctu.edu.tw/place_rent/main.php?tp=showinfo&m='
# 0: this month 1: next 2: next next
month = 1
# date 1 ~ 30 or 31
date = 31

page = urllib.request.urlopen(courtUrl + str(month))
soup = BeautifulSoup(page.read())

table = soup.body.find_all('tr')
# day 1 = 8
if (7+date) < len(table):
    table = table[7+date]

    line = table.find_all('td')

    line = line[1:]
    indexForSec = 0
    indexForPlace = 0

    for l in line:
        text = l.contents[0]
        if text == '\xa0':
            text = 0
        else:
            text = text['alt'].split('-')
            formatData = {}
            i = 0
            for k in listOfFM:
                formatData[k] = text[i]
                i += 1
            text = formatData
        sDict[sections[indexForSec]] = text
        indexForSec += 1
        if indexForSec == 4:
            output[place[indexForPlace]] = sDict
            sDict = {}
            indexForSec = 0
            indexForPlace += 1



    print(output)





