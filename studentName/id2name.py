import requests
from bs4 import BeautifulSoup
URL = "http://icdoor.nctu.edu.tw/enitorweb/EmpReg.aspx"
r = requests.get(URL)
soup = BeautifulSoup(r.text)
viewstate = soup.findAll("input", {"type": "hidden", "name": "__VIEWSTATE"})
eventvalidation = soup.findAll("input", {"type": "hidden", "name": "__EVENTVALIDATION"})
data = {'__EVENTVALIDATION': eventvalidation[0]['value'],
        '__VIEWSTATE': viewstate[0]['value'],
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        'txtID': '0316316',
        'btn_CheckPerson': '%E6%AA%A2%E6%9F%A5%E5%80%8B%E4%BA%BA%E8%B3%87%E6%96%99'}
r = requests.post(URL, data=data)
soup = BeautifulSoup(r.text)
name = soup.find(id="lbl_NameShow")
print(name.string)