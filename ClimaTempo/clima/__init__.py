import requests, json


class Clima:


    def __init__(self, token, city):
        self.token = token
        self.city = city


    ##obten id cidade
    def data_city(self):
        #city = input('Informe o nome da cidade: ')
        url = 'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=' + self.city + '&state=ce&token=' + self.token
        response = requests.get(url)
        date = json.loads(response.text)
        return date[0]['id']



    #registrar cidade para utilizar algumas consultas
    def register_city(self, id_city):
        """'http://apiadvisor.climatempo.com.br/api-manager/user-token/5cca58af8cc349c15c55c1596219c717/locales' \
                -H 'Content-Type: application/x-www-form-urlencoded' \
                -d 'localeId[]='"""
        url = 'http://apiadvisor.climatempo.com.br/api-manager/user-token/5cca58af8cc349c15c55c1596219c717/locales'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        local = 'localeId[]=' + str(id_city)
        response = requests.put(url, headers=headers, data=local)
        print(json.loads(response.text))


    def clima_city(self):
        url = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/8050/current?token=' + self.token
        response = requests.get(url)
        info_city = json.loads(response.text)        
        print(f'Estado: {info_city["state"]}')
        print(f'Cidade: {info_city["name"]}')
        print(f'País: {info_city["country"]}')
        print(f'Temperatura: {info_city["data"]["temperature"]}C graus com sensação termica de {info_city["data"]["sensation"]}C graus')
        print(f'Condição: {info_city["data"]["condition"]}')
