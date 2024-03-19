'''Crie um código em Pyhton que teste se o site Pudim está 
accessível pelo computador usado'''
import urllib 
import urllib.request
try:
  site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
  print('O site Pudim não está acessível no momento')
else:
  print('Consegui acesar o site Pudim')