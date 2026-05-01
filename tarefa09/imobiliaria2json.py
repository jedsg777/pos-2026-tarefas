import json
from xml.dom.minidom import parse

def get_data(element, tag):
    
    nodes = element.getElementsByTagName(tag)
    if nodes and nodes[0].firstChild:
        return nodes[0].firstChild.nodeValue.strip()
    return None

def xml_to_json():
    try:
        
        dom = parse('imobiliaria.xml')
        root = dom.documentElement
        imoveis_xml = root.getElementsByTagName('imovel')
        
        lista_imoveis = []

        for imovel in imoveis_xml:
            # Captura o ID do atributo
            id_imovel = imovel.getAttribute('id')

            # Processa Proprietario
            prop_node = imovel.getElementsByTagName('proprietario')[0]
            prop_nome = get_data(prop_node, 'nome')
            
            # Pega multiplos e-mails e telefones
            emails = [e.firstChild.nodeValue.strip() for e in prop_node.getElementsByTagName('email')]
            telefones = [t.firstChild.nodeValue.strip() for t in prop_node.getElementsByTagName('telefone')]

            # Processa Endereco
            end_node = imovel.getElementsByTagName('endereco')[0]
            num = get_data(end_node, 'numero')

            # Processa Caracteristicas
            carac_node = imovel.getElementsByTagName('caracteristicas')[0]
            
            # Monta o dicionario do imovel seguindo o seu modelo JSON
            dados_imovel = {
                "id": id_imovel,
                "descricao": get_data(imovel, 'descricao'),
                "proprietario": {
                    "nome": prop_nome,
                    "email": emails,
                    "telefone": telefones
                },
                "endereco": {
                    "rua": get_data(end_node, 'rua'),
                    "bairro": get_data(end_node, 'bairro'),
                    "cidade": get_data(end_node, 'cidade'),
                    "numero": int(num) if num and num.isdigit() else num
                },
                "caracteristicas": {
                    "tamanho": int(get_data(carac_node, 'tamanho')),
                    "numQuartos": int(get_data(carac_node, 'numQuartos')),
                    "numBanheiros": int(get_data(carac_node, 'numBanheiros'))
                },
                "valor": get_data(imovel, 'valor')
            }
            lista_imoveis.append(dados_imovel)

        
        estrutura_final = {
            "imobiliaria": {
                "imovel": lista_imoveis
            }
        }

        
        with open('imobiliaria.json', 'w', encoding='utf-8') as f:
            json.dump(estrutura_final, f, indent=4, ensure_ascii=False)
            
        print("Sucesso o arquivo 'imobiliaria.json' foi criado com base no XML.")

    except FileNotFoundError:
        print("Erro: O arquivo 'imobiliaria.xml' nao foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro na conversao: {e}")

if __name__ == "__main__":
    xml_to_json()