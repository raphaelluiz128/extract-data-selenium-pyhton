# -*- coding: utf-8 -*-

import os
import time
import re
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter as cnt

class newbot:

    def __init__(self, nome_bot):
        self.driver = webdriver.Firefox()

    def climaTempo(self):
        try:

            site  = 'https://www.climatempo.com.br/previsao-do-tempo'
            self.driver.get(site)
            self.driver.implicitly_wait(20)

            i = 0
            while True:
                estado=11
                cidades = [70,217] 

                #11 = Minas Gerais
                #70 = Belo Horizonte, 217 = Contagem

                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div[19]/div[2]/div/div/ul/li[201]/a').click() 

                time.sleep(20)

                localidade = self.driver.find_element_by_xpath('/html/body/div[3]/div[6]/div[4]/div[1]/div[2]/div[1]/div/div[1]/h1').text
                temperatura = self.driver.find_element_by_xpath('/html/body/div[3]/div[6]/div[4]/div[1]/div[2]/div[1]/div/div[2]/span').text
                condicao = self.driver.find_element_by_xpath('/html/body/div[3]/div[6]/div[4]/div[1]/div[2]/div[1]/div/div[3]/span[1]').text

                dat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print("Localidade: " + localidade)
                print("Temperatura: " + temperatura)
                print("Condição: " + condicao)
                
                print("Data da Consulta: " + dat)
                print('-----------------------------')

                time.sleep(10)

                dados = localidade + ';' + temperatura + ';' + condicao + ';' + dat
                self.salvaDados(dados)

                i+=1
                if(i>1):
                    i=0
        except:
            self.driver.close()
            self.erro()


    def erro(self):
         self.climaTempo()

    def salvaDados(self, dados):
        datt = datetime.now().date().strftime("%Y-%m-%d")
        arquivo = open('C:/home/raphael/Área de Trabalho/climatempo/ dados - ' + datt + '.txt', 'a')
        arquivo.write(dados + '\n')
        arquivo.close()