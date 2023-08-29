import speech_recognition as sr
import os
import pygame
from selenium import webdriver
import ctypes
import psutil
import pyautogui
import time
from unidecode import unidecode
from urllib.parse import quote
import ctypes
from gtts import gTTS
import subprocess


def noticias():
    nav = webdriver.Chrome() 
    nav.get("https://projetocomprova.com.br/")
    noticias = nav.find_elements_by_class_name('answer__title')
    for i in noticias:
        speak(str(i.text))
    nav.close()
    
def dicionario(word):
    word = quote(word)
    word = word.replace("%20", "")
    nav = webdriver.Chrome()
    nav.get("https://www.dicio.com.br/" + word + "/")
    significado = nav.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/p/span[2]')
    nav.close()
    print(significado.text)
    
def pesquisar(search):
    search = str(search).replace(" ", "+")  
    nav = webdriver.Chrome()
    nav.get("https://www.google.com/search?q=" + search + "&sxsrf=AJOqlzWaIk0xBgGpDGLrrDTqO6T8qJqhWA%3A1675428085778&ei=9QDdY6aQL6aE1sQPwOOf8A4&ved=0ahUKEwjm3pj_r_n8AhUmgpUCHcDxB-4Q4dUDCA8&uact=5&oq=pagina+de+outros&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICAAQFhAeEA86CggAEEcQ1gQQsAM6CAgAEIAEELEDOgQIABBDOgoIABCxAxCDARBDOgsILhCABBCxAxDUAjoFCAAQgAQ6CAgAELEDEIMBOgsIABCABBCxAxCDAToICC4QgAQQywE6CAgAEIAEEMsBOggIABAWEB4QCkoECEEYAEoECEYYAFCaAliWDGDwDGgBcAF4AIAB1AGIAdwIkgEFMC43LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp")
    
def kill_process(process_name):
    for process in psutil.process_iter():
        if process.name() == process_name:
            process.kill()

def speak(text):
    if os.path.exists('output.mp3'):
        os.remove('output.mp3')
        tts = gTTS(text=text, lang='pt')
        tts.save("output.mp3")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.quit()
    else:
        tts = gTTS(text=text, lang='pt')
        tts.save("output.mp3")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.quit()



def comandos(text):

    comandos = {
    'bom dia': lambda: speak('Bom dia Arthur'),
    'como você vai': lambda: speak('Estou bem e você?'),
    'abrir navegador': lambda: (speak('Abrindo navegador'), os.system("start brave.exe")),
    'abrir editor de text': lambda: (speak("Abrindo editor de text"), os.system("start notepad.exe")),
    'tocar música': lambda: (speak('Vamos ouvir uma música, Arthur'), os.system("start spotify.exe"), time.sleep(3), pyautogui.press('space')),
    'suspender computador': lambda: (speak('Suspendendo o computador'), subprocess.call('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')),
    'desligar computador': lambda: (speak('Desligando o computador'), os.system("shutdown /s /t 1")),
    'fechar navegador': lambda: (speak('Fechando navegador'), os.system("taskkill /f /im brave.exe")),
    'ferrou': lambda: ctypes.windll.user32.LockWorkStation(),
    'o que você pode fazer': lambda: speak("Meus comandos são: bom dia, como você vai, abrir navegador, fechar navegador, tocar música, notícias, pesquisar, adicionar uma meta, e vários outros"),
    'notícias': lambda: (speak("Notícias de hoje"), noticias()),
    }
    
    
    comandosComArgumento = {
    'qual o significado da palavra': lambda text: (speak("Pesquisando significado da palavra " + text.split("qual o significado da palavra")[1]), 
                                                   print(unidecode(text.split("qual o significado da palavra")[1])), 
                                                   dicionario(unidecode(text.split("qual o significado da palavra")[1]))),
    'pesquisar': lambda text: (speak("Pesquisando"), pesquisar(text.split("pesquisar")[1])),
    'adicionar uma meta': lambda text: speak("Meta " + text.split("adicionar uma meta")[1] + " adicionada com sucesso"),
    }
    for acao in comandosComArgumento.keys():
        if acao in text:
            return comandosComArgumento.get(acao, lambda: None)(text)
        else:
            for acao in comandos.keys():
                if acao in text:   
                    return comandos.get(acao, lambda: None)()
        
r = sr.Recognizer()
palavra_ativacao = "PC"
with sr.Microphone() as source:
    print("Diga 'PC' para ativar o reconhecimento de fala...")
    while True:
        # Ouça o áudio e converta-o em text
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='pt-BR')
            print("Você disse: " + str(text))
            if palavra_ativacao in text:
                # Ouça a frase e converta-a em text
                audio = r.listen(source, timeout=3)
                try:
                    text = r.recognize_google(audio, language='pt-BR')
                    print("Você disse: " + str(text))
                    comandos(str(text).lower())
                except sr.UnknownValueError:
                    print("Não foi possível reconhecer a fala")
                except sr.RequestError as e:
                    print("Erro ao conectar-se ao serviço de reconhecimento de fala: {0}".format(e))
        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala")
        except sr.RequestError as e:
            print("Erro ao conectar-se ao serviço de reconhecimento de fala: {0}".format(e))