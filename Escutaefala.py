## Criado por dagoberto.panassol@gmail.com
## usando o Spyder do Visual Studio, sem as 2 import não funciona!!!

import speech_recognition as sr
import speech
#Funcao responsavel por ouvir e reconhecer a fala
#print ("frase antes da funcção "+str(frase) )
def minusculas(texto):
    lo= texto.lower()
    #print (lo)
    return lo

def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognitio
        #microfone.adjust_for_ambient_noise(source)
       #Coma
        #speech.say("Diga Algo !")
        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source,timeout=0,phrase_time_limit=5)
               


    try:
        #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')
        #Após alguns segundos, retorna a frase falada
        vf = minusculas(frase) 
        print("Você disse: " + frase)
        
        
        if (vf =="oi tudo bem"):
            #print("Entendi")
            speech.say("...Oi Dagoberto eu estou bem ......e voce ?")
        elif(vf =="oi"or (vf =="Oi")):
            speech.say("...olá tudo bem com você?")
        elif(vf =="o que você sabe fazer"):
            speech.say("...or enquanto nada, me ensine...")
        elif(vf =="não"):
                speech.say("............Mas por que não?...")
        elif(vf =="tu é muito chata" or (vf =="voce é muito chata") ):
                speech.say("...Me desculpe mas estou aprendendo...")
        elif(vf =="qual o seu nome"or (vf =="qual o teu nome")):
                speech.say("...Não tenho ainda, me diga um...")
        elif(vf =="pareço um louco falando sozinho" or(vf =="parece um louco falando sozinho") ):
                speech.say("...a vida é assim...")
                
                
                
        else:
            speech.say("..... eu entendi mas não conheço a frase!"+frase)
        #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except:      #sr.UnkownValueError:
        print("Exeption: Não entendi")
        if 'frase' in locals():
            return frase
        else:
            frase = ouvir_microfone()            

    
count = 0
while count < 105:
    print("ouvindo..."+str(count) )
    frase = ouvir_microfone()
    count += 1 

    
    
