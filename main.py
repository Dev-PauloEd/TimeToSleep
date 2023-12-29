import os
import datetime
import time

tempo = datetime.datetime.now() # Armazena o horário atual
while tempo.hour <= 21 or tempo.minute <= 30: # Verifica se são 21:30h
    print('verificação')
    time.sleep(300) # Se for falso, espera 5m
    tempo = datetime.datetime.now() # Volta pra linha 5

os.system("shutdown -s") # Caso seja verdadeiro, desliga o computador