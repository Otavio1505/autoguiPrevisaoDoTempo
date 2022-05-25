import pyautogui as p
import time
print('='*30,'RECEBER PREVISÃO DO TEMPO','='*30)
print('[Digitar localidade sem a presença de acentuações]')
cidade = str(input('[Ex: Sao Paulo - SP] '
                  'Cidade: '))
contato = int(input('[Ex: 5522981437863] '
                   'Número do celular: '))

p.hotkey('win','d')
time.sleep(0.5)
p.press('win')
time.sleep(0.5)
p.write('Microsoft Edge')
time.sleep(0.5)
p.press('enter')      # <--- Abertura do Navegador
time.sleep(1)
p.hotkey('win', 'up')
time.sleep(1)
p.write('https://web.whatsapp.com/')
time.sleep(0.2)
p.press('enter')       # <--- Abertura do Site
time.sleep(10)

p.moveTo(x=33, y=150)
p.click()

time.sleep(0.5)
p.write(f'+{contato}')   # <--- É inserido o contato informado
time.sleep(1)
p.press('enter')
time.sleep(0.5)

p.hotkey('ctrl','t')
time.sleep(0.5)
p.write(f'Previsao do tempo {cidade}')   # <--- É feita a pesquisa da previsão do tempo do local informado
time.sleep(0.5)
p.press('enter')
time.sleep(3)


p.hotkey('ctrl', '2')
time.sleep(0.1)
p.moveTo(x=250, y=269)
time.sleep(0.1)
p.mouseDown()
time.sleep(0.1)
p.moveTo(x=324, y=266)
time.sleep(0.1)
p.mouseUp()
time.sleep(0.1)
p.rightClick()       # <--- É feita a leitura em voz alta da previsão do tempo, afim de que o reprodutor de áudio do Wpp capte
time.sleep(0.1)
p.moveTo(x=336, y=461)
time.sleep(0.5)
p.click()
time.sleep(0.1)

#p.hotkey('alt','tab')
p.moveTo(x=110, y=8)
p.click()
time.sleep(0.2)
p.moveTo(x=1329, y=691)
time.sleep(0.5)
p.click()        # <---- Início do Áudio
time.sleep(4.7)
p.moveTo(x=1328, y=684)
p.click()             # <--- Término do audio
time.sleep(1.5)
p.hotkey('ctrl', '2')
p.moveTo(x=495, y=48)
p.click()
p.hotkey('ctrl', 'c')     # <--- É feita a Cópia da URL do site em que foi feita a pesquisa da previsão do tempo (Google)
time.sleep(0.5)
p.moveTo(x=110, y=8)
p.click()
p.moveTo(x=775, y=690)
p.hotkey('ctrl', 'v')    # <--- É colada na conversa do Wpp a URL do site copiado e efetuado o envio em seguida
p.press('enter')
time.sleep(1.5)
p.hotkey('ctrl', '2')
time.sleep(0.5)

#foto
p.keyDown('shift')
p.hotkey('win', 's')
p.keyUp('shift')
time.sleep(1)
p.moveTo(x=171, y=235)
p.mouseDown()
time.sleep(1)
p.moveTo(x=850, y=324)
time.sleep(0.1)
p.mouseUp()         # <--- É feita a captura de tela da previsão do tempo + nome da localidade
time.sleep(2.5)
p.hotkey('ctrl', '1')
time.sleep(0.5)
p.hotkey('ctrl', 'v')
time.sleep(0.8)
p.press('enter')    # <--- A captura de tela é enviada na conversa