from flask import flask
import requests


topic = 'pizza'

r = requests.get('https://newsdata.io/api/1/latest?apikey=pub_544064f4ed63ce81c7478f27000f5d3celcaf&q={topic}')


