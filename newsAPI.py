import requests

def get_weather(city, api_key, units):
    url ="https://newsapi.org/v2/everything?qlnTitle=stock20market&from={from_date}&sortBy=popularity&languag=en&apiKey={api_Key}"
    request = requests.get(url)
    content = request.json()
    print(content)
 get_weather("kannur","1e19040ecfdfbde24f0fa97e63ebeb8e",'standard')