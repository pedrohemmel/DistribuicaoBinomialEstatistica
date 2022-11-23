import numpy as np
import time
from scipy.special import factorial

def printInEachSecond(text) :
  arrText = []
  for i in range(len(text)):
    arrText.append(text[i])
  

  for letter in arrText:
    print(letter, end = '', flush=True)
    time.sleep(0.03)

def getUntilX(x):
  arrXAux = []
  for i in range(x + 1):
    arrXAux.append(i)

  return arrXAux

def binominalDistributionFunction(n, x, p):
  return (factorial(n)/(factorial(x)*factorial(n-x))) * np.power(p, x) * np.power((1-p), (n-x))
  
def binomialDistributionUntilX(n, arrX_BDUX, p):
  
  arrResult = []
  for x in arrX_BDUX:
    arrResult.append(binominalDistributionFunction(n, x, p))
    
  return sumOfArrResult(arrResult)
  
def binomialDistributionAfterX(n, arrX_BDAX, p):
  
  arrResult = []
  for x in arrX_BDAX:
    arrResult.append(binominalDistributionFunction(n, x, p))
    
  return 1 - sumOfArrResult(arrResult)

def sumOfArrResult(result):
  sumOfResult = 0
  for i in result:
    sumOfResult = sumOfResult + i
  
  return sumOfResult




printInEachSecond("Olá, tudo bem? Vamos fazer a benção da Distribuição Binominal")

print()

printInEachSecond("Digite a quantidade de amostras: \n")
n = int(input())\

print()

printInEachSecond("Digite a probabiidade de sucesso das amostras:\n")
p = float(input())

print()

printInEachSecond("Digite o número de sucessos desejados das amostras: \n")
x = int(input())

printInEachSecond("\nSelecione o problema desejado:\nDigite 1) " + str(x) + " será o número de sucesso das amostras;\nDigite 2) De 0 até " + str(x) + " serão os números de sucesso das amostras;\nDigite 3) Maior que " + str(x) + " serão os números de sucesso da amostra;\n")

problemChoosed = int(input())

if problemChoosed == 1:
  
  result = binominalDistributionFunction(n, x, p)
  
elif problemChoosed == 2:
  
  arrX = getUntilX(x)
  result = binomialDistributionUntilX(n, arrX, p)

elif problemChoosed == 3:
  
  arrX = getUntilX(x)
  result = binomialDistributionAfterX(n, arrX, p)

printInEachSecond("A probabilidade é " + str(round(result, 4)))

