capitais = {
    "Acre":"Rio branco",
    "Alagoas":"Maceio",
    "Amapa":"Macapa",
    "Amazonas":"Manaus",
    "Bahia":"Salvador",
    "Ceara":"Fortaleza",
    "Espirito Santo":"Vitoria",
    "Goias":"Goiania",
    "Maranhao":"Sao luiz",
    "Mato Grosso":"Cuiaba",
    "Mato Grosso do Sul":"Campo Grande",
    "Minas Gerais":"Belo Horizonte",
    "Para":"Belem",
    "Pernambuco":"Recife",
    "Piaui":"Terezinha",
    "Rio de Janeiro":"Rio de Janeiro",
    "Rio grande do sul":"Porto Alegre",
    "Rio grande do norte":"Natal",
    "Rondonia":"Porto velho",
    "Roraima":"Boa vista",
    "Santa Catarina":"Florianopolis",
    "Sao Paulo":"Sao Paulo",
    "Sergipe":"Aracaju",
    "tocantins":"palmas",
    "Distrito Federal":"Brasilia",

}

# for i in capitais:
#     print(i)

# print(capitais[0:6])
# print(capitais["Acre"])
# Pegar os 6 primiros itens
ps = 1 
for i in capitais:
    if ps < 6:
        print(i+": A capital é "+capitais[i])
    else:
        break
    ps+=1