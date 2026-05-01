import json

with open('imobiliaria.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)


imoveis = dados['imobiliaria']['imovel']

print('IMOVEIS:')
for i in range(len(imoveis)):
    print(i+1, '-', imoveis[i]['descricao'])

escolha = int(input('----------------------------\nDigite o numero do imovel: '))

imovel = imoveis[escolha - 1]

print('Caracteristicas')
caracteristicas = imovel['caracteristicas']
print('Descricao:', imovel['descricao'])
print('Tamanho:', caracteristicas['tamanho'], 'm2')
print('Quartos:', caracteristicas['numQuartos'])
print('Banheiros:', caracteristicas['numBanheiros'])
print('Valor: R$', imovel['valor'])

print('Proprietario ')
proprietario = imovel['proprietario']
print('Nome:', proprietario['nome'])


emails = proprietario.get('email')
if emails:
    print('Email:', ', '.join(emails))
else:
    print('Email: Nao informado')


telefones = proprietario.get('telefone')
if telefones:
    print('Telefones:', ', '.join(telefones))
else:
    print('Telefones: Nao informado')

print('Endereco')
endereco = imovel['endereco']
print('Rua:', endereco['rua'])
print('Bairro:', endereco['bairro'])
print('Cidade:', endereco['cidade'])


numero = endereco.get('numero')
if numero:
    print('Numero:', numero)
else:
    print('Numero: S/N')