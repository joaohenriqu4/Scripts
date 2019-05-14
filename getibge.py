from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

output = []
arquivo = open('muni.txt','r')
linhas = arquivo.readlines()

for linha in linhas:
	teste = "https://cidades.ibge.gov.br/brasil/pe/{LINHA}/panorama".format(LINHA=linha)
	browser = webdriver.Chrome()
	try: 
		browser.get(teste)
	except:
		browser.close()
		browser.get(teste)
	browser.maximize_window()
	time.sleep(15)

	nome = browser.find_element_by_xpath(r'//*[@id="local"]/ul/li[3]/h1').text
	cod_municip = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/div[1]/div[1]/p').text
	gentilico = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/div[1]/div[2]/p').text
	prefeito = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/div[1]/div[3]/p').text
	time.sleep(5)
	
	#aba populacao
	populacao_estimada_2018 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[2]/td[3]').text
	populacao_no_ultimo_censo_2010 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[4]/td[3]').text
	densidade_demografica_2010 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[6]/td[3]').text
	time.sleep(5)
	
	#aba trabalho e rendimento
	trabalho_rendimento = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[8]/th[2]')
	trabalho_rendimento.click()
	time.sleep(3)
	salario_medio_mensal_dos_trabalhadores_formais_2016 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[9]/td[3]').text
	pessoal_ocupado_2016 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[11]/td[3]').text
	populacao_ocupada_2016 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[13]/td[3]').text
	percentual_da_populacao_per_capita  = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[15]/td[3]').text
	time.sleep(5)
	
	#aba educacao
	educacao = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[17]/th[2]')
	educacao.click()
	time.sleep(3)
	taxa_de_escolarizacao_de_6_14_idade_2010 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[18]/td[3]').text
	IDEB_anos_iniciais_2015 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[20]/td[3]').text
	IDEB_anos_finais_2015 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[22]/td[3]').text
	matriculas_fundamental_2017 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[24]/td[3]').text
	matriculas_medio_2017 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[26]/td[3]').text
	docentes_fundamental_2015 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[28]/td[3]/span').text
	docentes_medio_2017 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[30]/td[3]').text
	numero_estabelecimentos_ensino_fundamental_2017 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[32]/td[3]').text
	numero_estabelecimentos_ensino_medio_2017 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[34]/td[3]').text
	educacao.click()
	time.sleep(5)
	
	#aba economia
	economia = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[36]/th[3]')
	economia.click()
	time.sleep(3)
	pib_per_capita_2016 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[37]/td[3]').text
	receitas_fontes_externas_2015 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[39]/td[3]').text
	idhm_2010 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[41]/td[3]').text
	receitas_realizadas_2017 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[43]/td[3]').text
	despesas_empenhadas_2017 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[45]/td[3]').text
	time.sleep(5)
	
	#aba saude
	saude = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[47]/th[2]')
	saude.click()
	time.sleep(3)
	mortalidade_infantil_2014 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[48]/td[3]').text
	internacoes_diarreia_2016 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[50]/td[3]').text
	estabelecimentos_sus_2009 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[52]/td[3]').text
	
	#aba territorio e ambiente
	territorio_ambiente = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[54]/th[2]')
	territorio_ambiente.click()
	time.sleep(3)
	unidade_territorial_2017 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[55]/td[3]').text
	sanitario_adequado_2010 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[57]/td[3]').text
	vias_publicas_2010 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[59]/td[3]').text
	Urbanização_publicas_2010 = browser.find_element_by_xpath(r'//*[@id="dados"]/panorama-resumo/table/tr[61]/td[3]').text
	
	
	output.append(f'NOME: {nome}; Código do Município: {cod_municip}; Gentílico: {gentilico}; Prefeito: {prefeito}; -- ABA POPULAÇÃO; POPULAÇÃO: {populacao_estimada_2018}; populacao_no_ultimo_censo_2010: {populacao_no_ultimo_censo_2010}; densidade_demografica_2010: {densidade_demografica_2010}; -- aba trabalho e rendimento; salario_medio_mensal_dos_trabalhadores_formais_2016: {salario_medio_mensal_dos_trabalhadores_formais_2016}; pessoal_ocupado_2016: {pessoal_ocupado_2016}; populacao_ocupada_2016: {populacao_ocupada_2016}; percentual_da_populacao_per_capita: {percentual_da_populacao_per_capita}; -- aba educacao educacao; taxa_de_escolarizacao_de_6_14_idade_2010: {taxa_de_escolarizacao_de_6_14_idade_2010}; IDEB_anos_iniciais_2015: {IDEB_anos_iniciais_2015}; IDEB_anos_finais_2015: {IDEB_anos_finais_2015}; matriculas_fundamental_2017: {matriculas_fundamental_2017}; matriculas_medio_2017: {matriculas_medio_2017}; docentes_fundamental_2015: {docentes_fundamental_2015}; docentes_medio_2017: {docentes_medio_2017}; numero_estabelecimentos_ensino_fundamental_2017: {numero_estabelecimentos_ensino_fundamental_2017}; numero_estabelecimentos_ensino_medio_2017: {numero_estabelecimentos_ensino_medio_2017}; -- aba economia; pib_per_capita_2016: {pib_per_capita_2016}; receitas_fontes_externas_2015: {receitas_fontes_externas_2015}; idhm_2010: {idhm_2010}; receitas_realizadas_2017: {receitas_realizadas_2017}; despesas_empenhadas_2017: {despesas_empenhadas_2017}; -- saude saude; mortalidade_infantil_2014: {mortalidade_infantil_2014}; internacoes_diarreia_2016: {internacoes_diarreia_2016}; estabelecimentos_sus_2009: {estabelecimentos_sus_2009}; -- territorio e ambiente; unidade_territorial_2017: {unidade_territorial_2017}; sanitario_adequado_2010: {sanitario_adequado_2010}; vias_publicas_2010: {vias_publicas_2010}; Urbanização_publicas_2010: {Urbanização_publicas_2010}\n')
	
	browser.close()
	print(output)
	
	arq = open('ibgedados.txt','w')
	arq.writelines(output)
	arq.close()
