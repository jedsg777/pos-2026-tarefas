from xml.dom.minidom import parse

# Carrega o documento
dom = parse('cardapio.xml')
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')

print("Pratos disponíveis:")
for prato in pratos:
    id_prato = prato.getAttribute('id')
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue.strip()
    print(f"{id_prato} - {nome}")

escolha = input('--------------------------------------------------\nDigite o ID do prato para mais informações: ')

for prato in pratos:
    id_prato = prato.getAttribute('id')

    if escolha == id_prato:
        nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue.strip()
        descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue.strip()
        preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue.strip()
        calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue.strip()
        tempoPreparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue.strip()
        
        ingredientes_nodes = prato.getElementsByTagName('ingrediente')
        lista_ingredientes = [ingrediente.firstChild.nodeValue.strip() for ingrediente in ingredientes_nodes]

        print('--------------------------------------------------')
        print(f'Prato: {nome}')
        print(f'Descrição: {descricao}')
        print(f'Preço: {preco}')
        print(f'Ingredientes: {", ".join(lista_ingredientes)}')
        print(f'Calorias: {calorias}')
        print(f'Tempo de Preparo: {tempoPreparo}') 
        break
else:
    print('Prato não encontrado.')