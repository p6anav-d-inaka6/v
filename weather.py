import requests

def get_weather(city, api_key, units):
    url = f"http://api,openweahermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    request = requests.get(url)
    content = request.json()
    print(content)
 get_weather("kannur","1e19040ecfdfbde24f0fa97e63ebeb8e",'standard')