from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


dormURL = [ 'http://mailsys.nctu.edu.tw/MailNotify/main.asp?dorm=' + '{0:03}'.format(i) for i in range(86,103)]
mailData = []
formatOfData = ['id','name','date','type']

for url in dormURL:
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page.read().decode('hkscs'))
	tables = None
	try:
		tables = soup.body.table.find_all('tr')
	except:
		continue
	if tables:
		tables = tables[1:]
		for t in tables:
			lines = t.find_all('font')
			tmpData = {'exist':True}
			for index in range(0,4):
				tmpData[formatOfData[index]] = lines[index].contents[0]
			mailData.append(tmpData)
		
# mailData = [{'id','name','date','type',exist}...]


	






