#!/usr/bin/env python
# -*- coding: utf-8 -*-

#FUTURE - Essa biblioteca torna o código compatível para Python 2 e Python 3
from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()


'''''''''''''''''''''''''''Código Playground''''''''''''''''''''''''''''''
    Esse código apresenta um ambiente planejado para desenvolvimento de bots.

    Desenvolvido pela Banana Digital
    Michael Barney Galindo Júnior

    Este programa é um software livre; você pode redistribuí-lo e/ou 
    modificá-lo sob os termos da Licença Pública Geral GNU como publicada
    pela Fundação do Software Livre (FSF); na versão 3 da Licença,
    ou (a seu critério) qualquer versão posterior.

    Este programa é distribuído na esperança de que possa ser útil, 
    mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
    a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
    Licença Pública Geral GNU para mais detalhes.

    Você deve ter recebido uma cópia da Licença Pública Geral GNU junto
    com este programa. Se não, veja <http://www.gnu.org/licenses/>.
'''

'''IMPORT DAS BIBLIOTECAS QUE USAMOS'''

#Urllib - permite realizar solicitações na internet
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json #permite trabalhar com dados json

import os   #permite trabalhar diretamente com o sistema operacional

#Flask - permite utilizar um programa em python como um servidor
from flask import Flask
from flask import request
from flask import make_response
        
# Aplicativo Flask deve iniciar com layout global
app = Flask(__name__)

'''Função do Webhook, ativada com uma chamada POST'''
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True) #a informação recebida
    res = processRequest(req) #processa a informação
    res = json.dumps(res, indent=4)
    r = make_response(res) #cria uma resposta
    r.headers['Content-Type'] = 'application/json' #prepara a resposta
    return r

'''Função que realiza o processamento do dado recebido pelo API.ai, realizando uma atividade de acordo com cada ação:'''

def processRequest(req):
    action = req.get("result").get("action") #ações
    parameters = req.get("result").get("parameters") #parametros

    if action == "somar":
        numeros = parameters.get("numeros") #armazenamos os numeros em uma variavel
        soma = 0 #iniciamos a soma em 0
        
        for numero in numeros:    #para cada valor dos numeros
            soma = soma + numero  #adicionamos ele na soma

        #preparação do retorno
        retorno = {
            "speech": soma,
            "displayText": soma,
            "source": "app"
        }
        return retorno; #envia para o api.ai
    
    elif action == "chamarAlgumEvento":
        msg = {
            "followupEvent": {
                  "name": "eventoQueQuerChamar",
               }
            }
            
        return msg;

    
    else:
        return {}

'''Apresentar alguma resposta caso receba uma solicitação GET'''
@app.route('/', methods=['GET'])
def verify():
    return "Ativo", 200

'''Inicialização do serivdor'''
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Iniciando app na porta: %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')