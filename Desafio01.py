import requests

rqst = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL")
rqst_json = rqst.json()
#print(rqst_json)
cotacao_euro = float(rqst_json["EURBRL"]["bid"]) #5.19
#print(rqst_dolar_json)
cotacao_dolar = float(rqst_json["USDBRL"]["bid"]) #5.17

#print(cotacao_dolar)
#print(cotacao_euro)

#Programa conversao reais em dolar e euro

reais_converter = float(input("Digite a quantidade em reais para converter em dolar: "))

convert_reais_dolar = reais_converter / cotacao_dolar
convert_euro_dolar = reais_converter / cotacao_euro

print(f"{reais_converter} Reais equivalem a: {convert_reais_dolar:.4f} Dolares.\n")
print(f"{reais_converter} Reais equivalem a: {convert_euro_dolar:.4f} Euros.")









