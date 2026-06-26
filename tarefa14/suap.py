import requests
from getpass import getpass

url_suap = "https://suap.ifrn.edu.br/api/"

matricula = input("Matrícula: ")
chave_acesso = getpass()

credenciais = {"username": matricula, "password": chave_acesso}

requisicao = requests.post(url_suap + "token/pair", json=credenciais)
dados_token = requisicao.json()
print(dados_token)

token = dados_token["access"]
autenticacao = {
    "Authorization": f"Bearer {token}"
}

print(autenticacao)
ano_corrente = input("ano: ")
periodo_corrente = input("periodo: ")
resultado = requests.get(url_suap + f"ensino/meu-boletim/{ano_corrente}/{periodo_corrente}", headers=autenticacao)

boletim = resultado.json()["results"]
for materia in boletim:
    print(f"{materia['disciplina']:<70}{materia['nota_etapa_1']['nota']} - {materia['nota_etapa_2']['nota']} - {materia['nota_etapa_3']['nota']} - {materia['nota_etapa_4']['nota']}")