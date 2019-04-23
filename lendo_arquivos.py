arquivo = open('siglas_estados','r')
linhas = arquivo.readlines()

output = []
for linha in linhas:
	teste = "http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinanwin/cnv/animais{LINHA}.def".format(LINHA=linha)
	print (teste)
	output.append(f'{teste}')
print ("\n\t\t fim do arquivo")
arq = open('urldados.txt','w')
arq.writelines(output)
arq.close()
num = input(asww)
arquivo.close()

