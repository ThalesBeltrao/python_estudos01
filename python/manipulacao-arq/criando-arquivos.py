import os

#Criando arquivo com python
#usamos a funcao open para abrir
#close para fechar
#mods:
# r(leitura), w(escrita), x(para criação)
# a (escreve ao final), b(binário)
# t(modo texto) + (leitura e escrita)
#context manager =with(abre e fecha)
#métodos úteis
#white, read (escrever e ler)
#seek(move o cursor)
#readlines(ler linhas)
#vamosfalar mais sobre o módulo os,mas:
#os.remove ou unlink-apaga o arquivo
#os.rename-troca o nome do arquivo
#modulos sobre modulos json, mas:
#json.dump = gera um arquivo json
#json.load





caminho = "C:\\Users\\thale\\pythonProject\\"
caminho += "texto.txt"

#arquivo =open(caminho, "w")
#
#arquivo.close()
"""
with open(caminho, 'a+') as arquivo: # voce consegue escrever no arquivo que esta executando caso queira escrever e rodar ao mesmo tempo precisa passar o + se não pode dar erro
    arquivo.write("linha \n")
    arquivo.write("linha\n")
    arquivo.writelines(["nome:\n", "thales\n".strip()])
    arquivo.seek(0, 0)
    print(arquivo.read())
    print()

with open(caminho, 'r') as arquivo:
    print(arquivo.read())  # read voce consegue rodar ele no seu ide



#modos e tratamento de arquivos"""

with open(caminho, 'w+', encoding="utf8") as arquivo:
    arquivo.write("Atenção \n")
    arquivo.write("linha\n")
    arquivo.writelines(["nome:\n", "thales\n".strip()])
    arquivo.seek(0, 0)
    print(arquivo.read())
    print()


    # w ele não salva o arquivo ele roda o que foi escrito e apaga
    # o A ele salva o arquivo e vai gerando novos
    #modulos os remove unlink


#os.unlink(caminho) remover arquivo



#os.rename renomar ou mover
os.rename(caminho, "../thales.txt")