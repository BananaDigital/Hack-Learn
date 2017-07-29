#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Bibliotecas que permitem utilizar e requisitar dados JSON'''
import json
import urllib
import urllib2

def getJSON(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    json_object = json.load(response)
    return json_object
    
#O URL da chamada
url = "http://samples.openweathermap.org/data/2.5/weather?q=Recife&appid=b1b15e88fa797225412429c1c50c122a1"
dados = getJSON(url)

#a aquisição dos dados
print dados['main']['temp']

