# -*- coding: utf-8 -*-
import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
reload(sys)
sys.setdefaultencoding('utf8')

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
file = open("bankowosc.txt","a")
bank=["ALIOR","BGZBNPP","BZWBK","CDPROJEKT","GETIN","IDEABANK","INGBSK"]
now = datetime.datetime.now()
print "Czas: ",str(now)
file.write("Czas: "+str(now))
start = time.time()
for x in bank:
    driver.get('http://www.bankier.pl/inwestowanie/profile/quote.html?symbol='+x)
    kurs = driver.find_element_by_class_name("profilLast").text
    zmiana = driver.find_element_by_xpath("//span[@class='value']").text
    file.write("\nBank: "+x+"\nKurs: "+kurs+"\nZmiana: "+zmiana+"\n================")

koniec = time.time()
file.write("\nZakonczono, czas: %d sekund\n\n\n" %(koniec-start))
file.close()
print "Done."






