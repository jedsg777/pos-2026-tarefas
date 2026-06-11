import zeep

# define a URL do WSDL
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# define o código do país para BR
num_input = input("escolha o numero: ")

# faz a chamada do serviço
result = client.service.NumberToWords(
	ubiNum=num_input
)
# imprime o resultado
print(f"O código de telefone do {num_input} é {result}")

