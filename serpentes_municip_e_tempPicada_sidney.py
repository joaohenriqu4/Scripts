from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

output = []
num_de_municip = 186 +2 #O for comeca do 2, entao coloquei mais dois para seguir a quantidade do site
num_de_serpentes = 6 +2#O comeca do 2, entao coloquei mais dois para seguir a quantidade do site
num_de_temp_picadas = 6 +2


municip_cont = 1 #municip vai de 1 até 12 e a 13 é muni ignorado
serpente_cont = 1 #serpente 1 é em branco e o 6 é o laquético
temp_picadas_cont = 1

for g in range(2,num_de_municip):
	for s in range(2,num_de_serpentes):
		for tp in range(2,num_de_temp_picadas):
			browser = webdriver.Chrome() # inicia uma instancia
			try:
				browser.get('http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinanwin/cnv/animaispe.def')
			except:
				browser.close()
				browser.get('http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinanwin/cnv/animaispe.def')
			
			browser.maximize_window()
			time.sleep(3)
			
			#2006 é marcado automaticamente
			ano = browser.find_element_by_xpath(r'//*[@id="A"]/option[2]') #escolhe o ano 2005
			ano.click()
			ano = browser.find_element_by_xpath(r'//*[@id="A"]/option[3]') #escolhe o ano 2004
			ano.click()
			ano = browser.find_element_by_xpath(r'//*[@id="A"]/option[4]') #escolhe o ano 2003
			ano.click()
			ano = browser.find_element_by_xpath(r'//*[@id="A"]/option[5]') #escolhe o ano 2002
			ano.click()
			ano = browser.find_element_by_xpath(r'//*[@id="A"]/option[6]') #escolhe o ano 2001
			ano.click()
			
			municips = browser.find_element_by_xpath('//*[@id="fig9"]') #pega municip
			municips.click()
			
			municip = browser.find_element_by_xpath('//*[@id="S9"]/option[1]')#escolhe municip 1
			municip.click()
			
			municippath = '//*[@id="S9"]/option['+str(g)+']'
			municip = browser.find_element_by_xpath(municippath)#escolhe municip 1
			municip.click()
			time.sleep(3)
			
			
			temp_picadas = browser.find_element_by_xpath('//*[@id="fig20"]') #pega temp_picadaes
			temp_picadas.click()
			
			temp_picada = browser.find_element_by_xpath('//*[@id="S20"]/option[1]')#escolhe temp_picada 1
			temp_picada.click()
			
			temp_picadapath = '//*[@id="S20"]/option['+str(tp)+']'
			temp_picada = browser.find_element_by_xpath(temp_picadapath)#escolhe temp_picada 2
			temp_picada.click()
			
			
			serpentes = browser.find_element_by_xpath('//*[@id="fig22"]')#escolhe tipo de serpente 1
			serpentes.click()
			
			serpente = browser.find_element_by_xpath('//*[@id="S22"]/option[1]')#escolhe tipo de serpente 1
			serpente.click()
			serpentepath = '//*[@id="S22"]/option['+str(s)+']'
			serpente = browser.find_element_by_xpath(serpentepath)#escolhe tipo de serpente 1
			serpente.click()
			time.sleep(3)
			
			mostrar = browser.find_element_by_xpath('/html/body/div/div/center/div/form/div[4]/div[2]/div[2]/input[1]')# clica em mostrar
			mostrar.click()
			time.sleep(3)
			
			try:
				total_valor = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[1]/td[2]').text# pega o valor
			except:
				total_valor = 0
			try:
				valor_2001 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[2]/td[2]').text# pega o valor
			except:
				valor_2001 = 0
			try:
				valor_2002 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[3]/td[2]').text# pega o valor
			except:
				valor_2002 = 0
			try:
				valor_2003 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[4]/td[2]').text# pega o valor
			except:
				valor_2003 = 0
			try:
				valor_2004 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[5]/td[2]').text# pega o valor
			except:
				valor_2004 = 0
			try:
				valor_2005 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[6]/td[2]').text# pega o valor
			except:
				valor_2005 = 0
			try:
				valor_2006 = browser.find_element_by_xpath('/html/body/div/div/table/tbody/tr[7]/td[2]').text# pega o valor
			except:
				valor_2006 = 0
			output.append(f'municip: {municip_cont} -- Serpente: {serpente_cont} -- Tempo_Picadas: {temp_picadas_cont} -- 2001: {valor_2001}, 2002: {valor_2002}, 2003: {valor_2003}, 2004: {valor_2004}, 2005: {valor_2005}, 2006: {valor_2006}, Total: {total_valor}\n')
			temp_picadas_cont = temp_picadas_cont +1	
			browser.close()
			print(output)
			
		serpente_cont = serpente_cont +1
		temp_picadas_cont = 1
		
		arq = open('output_municip_temp_picadas.txt','a')
		arq.writelines(output)
		arq.close()
		output = []
		
	municip_cont = municip_cont +1
	serpente_cont = 1
