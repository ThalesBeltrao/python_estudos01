"""
#Dicionarios em python (tipo dict)
#Dicionarios seçao estruturas de dados do tipo
#par de usuario e valor
#chaves podem ser consideredas como indice
#que vimos na lista podem ser de tipos imutáveis
#como: str, int, float, bool, tuple
#mutavel: dic, list


pessoa = {
        'nome': "thales".capitalize(),
        "sobrenome": "willian".capitalize(),
        "idade": 15,
        "Altura": 1.80,
        "Endereco":[
            {"rua":"joaquim de oliveira silva", "Numero":1000}
        ]
}

#print(pessoa["idade"])


for usuario in pessoa:
       ... #print(usuario,pessoa[usuario])

pessoa2 = {}


pessoa2["nome"] = "luiz otavio" # nesse caso ja tem uma variavel declarada acima ele fez a substituição

print(pessoa2)
print(pessoa2["nome"])

print()
# usuario dinamica
pessoa3 = {}
usuario = "nome_completo"
pessoa3[usuario] = "lucas junior"
pessoa3[usuario] = "maria".capitalize()
pessoa3["sobrenome"] = "miranda".capitalize()
print(pessoa3[usuario])

del pessoa3["sobrenome"] #delete a usuario

#print(pessoa3["sobrenome"]) # nesse caso vai gerar um erro porque a usuario não esta especificada

print(pessoa3)

if pessoa3.get("sobrenome") is None: #para saber de a usuario existi no dicionário
        print("Não Existi")
else:
        print(pessoa3["sobrenome"])


#Métodos Uteis dos dicionarios em python
#len - quantas chaves
#keys - iterável com as chaves
#values -iteraveis com os valores
#itens -iteravel com chaves e valores
#setdefault -adicionar valor se a usuario não existir
#copy - retorna um copia rasa(shallow copy)
#popitem =- Apaga  ultimo item adicionado
#update - Atualiza um dicionário com outro



dados = {
        "nome": "Joarez",
        "sobrenome": "Junior",
        "idade": 15,
        #"Altura": 1.80
}


#print(len(dados)) # quantidade de usuario
#print(dados.keys())#chaves fazendo type coergion para tuupla, ou lista ou desempacotar
#print(list(dados.values())) apenas os valores
#print(dados.items()) usuario e valor

dados.setdefault("Altura",1.80) # voce adiciona um valor com uma usuario não existente no dicionario
print(dados["Altura"])
#for valor in dados.values():
        #print(valor)
print(dados.items())





import copy
# Shallow Copy vs Deep Copy em dados mutáveis Python
d1 = {
        "c1": 1,
        "c2": 2,
        "l1": [0,1,2] # shallow copi ele não entra dentro da lista para guardar o valor dentro de outra mem´ria ele apenas aponta para o valor que esta salvo em d1
}
d2 = d1.copy() # nesse caso usando um metodo copy ele faz uma copya do valor tendo seu proprio valor na memória isso faz com que ele modifique d2 e não altere d1 apenas valores imutáveis
#d2 = d1 # indica por see mutavel ele apenas aponda para a usuario primaria se mudar a usuario de d1 o d2 muda tambem e vise e versa
d2["c1"] = 1000 # por ser valores mutáveis ele não faz uma copia ele apenas aponda o valor para o mesmo lugar em que se encontra a primeira variavel que due origem ao dicionário
# isso chama shallow copy = copia rasa
d2["l1"][1]= 99 # por ser um elemento mutavel ele faz a alteração nas duas listar tanto em d1 como em d2
print(d1)
print(d2)


# depp copy fazer uma copia profunda
a1 = {
        "b1":10,
        "b2":15,
        "b3":20,
        "l2":[23,10,50]
}

a2 = copy.deepcopy(a1) # nesse caso voce vai estar fazendo uma copia profunda essa valor mesmo com os mutavies vão ser guardados em um lugar diferente da primeira variavel que foi copiada
a2["l2"][0]=200

print(a1)
print(a2)


#metodos uteis dos dicionários em Python
# len - quantas chaves
#keys - iteráveis com usuario
# values - iteráveis com os valores
# items - iteráveis com chaves e valores
#setdefault - adiciona vvalor se a usuario não existe
#copy retorna uma copia rasa (shallow copi)
#get - obtem uma usuario
#pop exclui o elemento específicado(del)
#popitem - apaga o ultimo item adicionado
#update - atualiza o dicionário


person1 = {
        "nome":"thales".capitalize(),
        "sobrenome": "willian".capitalize(),
        "altura": 1.80,
        "idade": 32,
        "peso":73
}

#print(person1.get("nome","usuario não existi")) # caso essa usuario não existisse retornaria um none(não valor)
#print(person1["nome"])
#nome = person1.pop("nome") # apaga uma usuario especificada
#person1.popitem() # exclui o ultimo elemento do dicionário
person1.update({
        "nome":"julia",
        "telefone":999999 # ele pode tantp modificar um elemento da usuario que ja esta especificada como criar uma usuario nova
})
# outro modo de usar o update
print(person1)
person1.update(nome="gabriel".capitalize(),idade= "23")
print(person1)
print()

# terceiro modo de usar o update
person2= {}
lista = [["nome","thales"],["idade",32]]
person2.update(lista)
print(person2)

questions = [
        {
                "pergunta": "Quanto é 2+2?",
                "Opções":["1","2","3","4"],
                "Resposta":4
        }
]

for question in questions:
        print(question["pergunta"])
        #print(*question["Opções"],sep="\n")

        for i, opcao  in enumerate(question["Opções"]):
                print(f"{i})",opcao)

        choose_value = int(input("Escolha seu valor: "))

        if choose_value == 4:
                print("Parabéns você acertou")
        else:
                print("Não foi dessa vez, tente novamente")



#desempacotamento e empacotamento em dicionários
#args e Kwargs
#kwargs -keyword argumentes (argumentos nomeados)

pessoa= {

        "nome":"Aline",
        "sobrenome":"julia"

}

#a, b = pessoa
#print(a, b) # nesse caso só pega as keys

#a, b = pessoa.values() #nesse caso desempacota apenas os values
#print(a, b)

#a, b = pessoa.items() # desempacota key e values
#print(a, b)

(a1, a2), (b1, b2) = pessoa.items()
print(a1 , a2)
print(b1, b2)

# mesma coisa de fazer um for
print()
for valor in pessoa.items():
        print(*valor) # nesse caso aqui eu desempacoto

# segunda maneira passando  key e values para o for
print()
for usuario , valor in pessoa.items():
        print(usuario , valor)"""


# unir dicionários
pessoa = {

        "nome":"Aline",
        "sobrenome":"julia"

}

dados_pessoa = {
        "idade":16,
        "Altura":1.80
}

#print(pessoa, dados_pessoa)
# primeira maneira de unir os dicionarios
pessoa.update(dados_pessoa)

print(pessoa)


#segunda maneira é fazer uma 3 variavel
#desempatocar os valores dentro de uma variavel abrindo as chaves e passando os **
complet_person = {**pessoa, **dados_pessoa, "telefone": 12991487061}
print(complet_person)


def mostrar_argumento_nomeados(*args, **kwargs):
        print(kwargs)
        print(args)


mostrar_argumento_nomeados(13, nome="thales".capitalize()) # aqui por estar com kwargs ele traz a funcao em forma de dicionãrio
