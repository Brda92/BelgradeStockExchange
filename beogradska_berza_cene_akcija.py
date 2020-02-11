from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen as uReq
from datetime import datetime


filename = "bse_akcije.csv"
f = open(filename, 'w')

headers = "Datum, Obim, Promet\n"
f.write(headers)

akcije = ["NIIS", "ENHL", "AERO", "FINT", "KMBN", "MTLC"]



for akcija in akcije:
	f.write(akcija + ',,\n')
	url_akcija = 'https://www.belex.rs/trgovanje/istorijski/'+akcija+'/12m'
	source_akcija = uReq(url_akcija)
	html_akcija = source_akcija.read()
	source_akcija.close()
	soup = BeautifulSoup(html_akcija, 'lxml')


	tabela = soup.find('table', class_ ='tdata')
	tabele = tabela.find_all('tr')
	del tabele[0]
	datumi, obimi, prometi, VWAP = [], [], [], []
	x = 1
	for i in tabele:
		svi_podaci = i.find_all('td')
		try:
			datum = svi_podaci[0].text[:-1]
			obim = svi_podaci[4].text.replace('.', '')
			promet = svi_podaci[5].text.replace('.', '')

			datumi.append(datum)
			obimi.append(int(obim))
			prometi.append(int(promet))
		except:
			print(x)
			x +=1
		f.write(datum + ',' + obim + ',' + promet + '\n')
f.close()


