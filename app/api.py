import requests
import shutil

def randomImageAPI():
    category = 'nature'
    api_url = 'https://api.api-ninjas.com/v1/randomimage?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'bdPWsaINX/n3R+hrCS3wtw==Y6dj8yHSwpljaAXh', 'Accept': 'image/jpg'}, stream=True)
    if response.status_code == requests.codes.ok:
        with open('app/static/img.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        print("Error:", response.status_code, response.text)