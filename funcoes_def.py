# -*- coding: utf-8 -*-
"""
Dagoberto
"""
# ok import matplotlib.pyplot as plt ## graficos
import speech_recognition as sr
import speech
import os

"""
a = 4
b = 45
def soma(x,y):
    res = x+y
    return res

def imprime(x):
    print ("Proc: "+str(x) )
    
num = soma(a,b)
imprime(num)    

t="Asd"

def geragrafico():
    plt.plot([1,2,3],[5,7,4])
    plt.show()
    return
"""
def fecharbloco():
   try:
       os.system('TASKKILL /F /IM notepad.exe')
   except:
       return

def minusculas(texto):
    normalizada = texto.lower()
    return normalizada

## Ouvinte principal
def ouvir_mic_inicial():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source, phrase_time_limit=3.5)
    try:
        frase_ouvir = microfone.recognize_google(audio, language='pt-BR')
        vfrase = minusculas(frase_ouvir)
        return vfrase
    except:
        print("ouvir_mic_inicial_exception")
        return False

def salvarFrase(f):
    arquivo = open('bancofrase.txt','a')
    #print("Salvando nova frase: " + str(f))
    arquivo.write(str(f)) 
    arquivo.write("\n")
    print("Frase nova salva com sucesso !!! " + arquivo.name )
    arquivo.close()
    speech.say("Salvo com sucesso")
    return True

def consulta():
    #linha  = 1
    arquivo = open('bancofrase.txt','r')  
    for linha in arquivo:
        linha = linha.rstrip()
        print (linha)    
    #arquivo.write(texto + "\n")
    print("Operação concluída no arquivo.")
    arquivo.close()
    speech.say('texto1')
    return

#salvarFrase(t)
#consulta()
    
"""    
count = 0
while count < 105:
    print(count)
    #frase = ouvir_microfone()
    count += 1 

r = compare(t)
print (str(r))
"""