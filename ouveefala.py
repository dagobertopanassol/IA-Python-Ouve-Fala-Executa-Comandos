from os import startfile as abre
import speech_recognition as sr
import speech
import funcoes_def
import ssh_pamk

#import sqlite3,sys
#import peewee
#Funcao responsavel por ouvir e reconhecer a fala
#print ("frase antes da funcção "+str(frase) )
#as= sys.platform()


def ouvir_comando():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        speech.say("Qual comando?")
        print("ouvir comando até 2s: ")
        audio = microfone.listen(source, phrase_time_limit=2)
    try:
        novofrase = microfone.recognize_google(audio, language='pt-BR')
        if novofrase =='None':
            print("google_traduziu: "+str(novofrase))
            return
        else:
            palavra = funcoes_def.minusculas(novofrase)
            return palavra
    except:
        print("FUNC 2 Ouvir_comando ,Exception:")
        return

def salvar_novo_comando():
    com1 = ouvir_comando()

    if com1 != type('NoneType'):
        speech.say("Salvar?"+str(com1)+ ",,,,,,,,Sim,, ou Nao?")
        aplicar_confimacao = False
        while aplicar_confimacao != True:
            confirma = confirmar_comando()
            if "sim" in str(confirma):
                funcoes_def.salvarFrase(com1)
                break
            elif "não" in str(confirma):
                print("Disse não, Nao salvei!")
                speech.say("Disse não, Nao salvei!")
                break
            else:
                print("if confirma sim ou não Else")
        else:
            print("while Else")
            confirma = confirmar_comando()
    else:
        print("salvarNovoComand Else")
    return


def confirmar_comando():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        print("ouvir confimacao 2s: ")
        audio = microfone.listen(source, phrase_time_limit=2)
    try:
        novofrase = microfone.recognize_google(audio, language='pt-BR')
        palavra = funcoes_def.minusculas(novofrase)
        return palavra
    except:
        print("confirmar_comando ,Exception:")
        confirmar_comando()
        #return

def verifica_frase_conhecida(vfc):
    #print("Entendi-> "+str(vfc))
    if vfc != type('NoneType'):
        print ("frase dita: "+str(vfc))
        if vfc == "oi tudo bem":
            speech.say("...Oi eu estou bem , qual o seu nome?")
        elif vfc == "oi" or vfc == "Oi":
            speech.say("......Oi tubo bem? qual o seu nome ? ")
        elif vfc == "o que você sabe fazer":
            speech.say("...or enquanto nada, me ensine...")
        elif vfc == "não":
            speech.say(",,,Mas por que não?...")
        elif vfc == "tu é muito chata" or (vfc == "você é muito chata"):
            speech.say("...Me desculpe mas estou aprendendo...")
        elif "qual o seu nome" in str(vfc) or "qual o teu nome" in str(vfc):
            speech.say("Conda")
        elif vfc == "pareço um louco falando sozinho" or vfc == "parece um louco falando sozinho":
            speech.say("...a vida é assim...")
        elif "é liziane" in str(vfc) or  "é lisiane" in str(vfc):
            speech.say("...Oi Liziane,, eu sei que voce trabalha na BRQ alimentos, o que você quer que eu faça ?")
        elif vfc == "otávio":
            speech.say("...oi otavio !! Já conversamos antes... O que voce quer ?")
        elif vfc == "skol":
            speech.say("...É muito boa bem gelada..A roups é a melhor, voce quer umas 20?")
        elif vfc == "tá viva":
            speech.say("...sim estou aqui, voce está muito quieto !!")
            ###COMandos
        elif vfc == "reiniciar o samba":
            ssh_pamk.restart_samba()
        elif vfc == "abrir notas":
            abre("notepad.exe")
        elif "fechar bloco de notas" in str(vfc):
            print("frase: "+str(vfc))
            funcoes_def.fecharbloco()
        elif vfc == "abrir navegador":
            abre("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif "abrir youtube" in str(vfc):
            abre('https://www.youtube.com/watch?v=Q8xTFgA32QU')
        elif vfc == "salvar um" or "salvar comando" in str(vfc):
            salvar_novo_comando()
            #segundo if
        else:
            print("a frase é desconhecida: "+str(vfc))
    # primeiro else
    else:
        print("é noneType: "+str(vfc))

vCOUNT = 0
while vCOUNT < 100000:
    print("ouvindo..."+str(vCOUNT))
    FRASE_OUVIR = funcoes_def.ouvir_mic_inicial()
    #if 'FRASE_OUVIR' in locals():
    if FRASE_OUVIR != type('NoneType'):
        verifica_frase_conhecida(FRASE_OUVIR)
    else:
        print("é nonetipe")
    vCOUNT += 1
