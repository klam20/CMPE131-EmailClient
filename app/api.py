import requests

#FROM API-NINJA
#Generates a 16 character password
def generatePassword():
    length = '16'
    api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
    response = requests.get(api_url, headers={'X-Api-Key': 'bdPWsaINX/n3R+hrCS3wtw==Y6dj8yHSwpljaAXh'})
    if response.status_code == requests.codes.ok:
        return response.text[21:-2] #Need to substring in order to get actual PW and not other information
    else:
        print("Error:", response.status_code, response.text)