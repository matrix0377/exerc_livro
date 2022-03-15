'''
Código para testar a função find_details
Lê o arquivo surfing_data.csv
Aprimorei com o while
Para sair digite 999 
'''


def find_details(id2find):
    surfers_f = open("F:\\vsProjetos2022\exerc_livro\surfing_data.csv", "r")
    for each_line in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'],
         s['board'], s['age']) = each_line.split(';')
        if id2find == int(s['id']):
            surfers_f.close()
            return(s)
    surfers_f.close()
    return({})


lookup_id = 0
while lookup_id != 999:
    lookup_id = int(input("Enter the id of the surfer: "))
    surfer = find_details(lookup_id)
    if surfer:
        print("  ")
        print("===*===" * 7)
        print("  ")
        print("ID:         " + surfer['id'])
        print("Name:       " + surfer['name'])
        print("Country:    " + surfer['country'])
        print("Average:    " + surfer['average'])
        print("Board type: " + surfer['board'])
        print("Age:        " + surfer['age'])
        print("===*===" * 7)
        print("======>>>> para Sair, digite 999")

