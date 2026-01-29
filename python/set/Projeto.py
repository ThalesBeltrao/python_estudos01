# valores duplicados
from collections import Counter

lista_emails = ("a@gmail", "b@gmail", "c@gmail", "a@gmail", "b@gmail")


# list comprehesion
#duplicado = [email for email in lista_emails if lista_emails.count(email) > 1]
#print(set(duplicado))

# sem lista comprehesion

#lista = []

#for email in lista_emails:
    #if lista_emails.count(email) > 1:
        #lista.append(email)



duplicado = Counter(lista_emails)
print(duplicado)

