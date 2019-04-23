from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


output = []
num_de_municip = 186 +2 


browser = webdriver.Chrome() 
try:
	browser.get('http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinanwin/cnv/animaispe.def')
except:
	browser.close()
	browser.get('http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinanwin/cnv/animaispe.def')

browser.maximize_window()
time.sleep(3)
								
municips = browser.find_element_by_xpath('//*[@id="fig9"]')
municips.click()
time.sleep(3)		
municip = browser.find_element_by_xpath('//*[@id="S9"]/option[1]')

for g in range(2,num_de_municip):				
	municippath = '//*[@id="S9"]/option['+str(g)+']'
	municip = browser.find_element_by_xpath(municippath).text
	time.sleep(3)
	output.append(f'{municip}')
	print(output)
	
browser.close()	
arq = open('muni.txt','w')
arq.writelines(output)
arq.close()