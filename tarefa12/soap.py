import requests
from xml.dom.minidom import parseString
# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

op = input(" coloque o numero, 1 é o numero, 2 é o nome e 3 é o nome da lingua: ")

if op == "1":
    operation = "CountryIntPhoneCode"
elif op == "2":
    operation = "CountryName"
elif op == "3":
    operation = "CapitalCity"
else: 
    print("numero invalido")

country_code = input("digite o codigo do país: " )
# XML estruturado
payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{operation} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{country_code}</sCountryISOCode>
					</{operation}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)
if response.status_code == 200:
    if op == "1":
        response = parseString(response.text).documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue
    elif op == "2":
        response = parseString(response.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue
    elif op == "3":
        response = parseString(response.text).documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue
    print(response)
