import os
import time
import sys
import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import json

from datetime import datetime


# token do device criado no Thingsboard
password= "4MPXTVQqsmObvx7fkXWW"
# Endereço do broker, no caso o host do Thingsboard
broker = "thingsboard.lcc.ime.uerj.br"
# topico do dispositivo
topic = "v1/devices/me/telemetry"

#Intervalo de Captura e upload em segundos
INTERVAL=5 

sensor = {'temperatura': 0, 'umidade': 0}

next_reading = time.time() 

client = mqtt.Client()

# Configurando o token de acesso
client.username_pw_set(password)

# Conectando no ThingBoard usando porta MQTT não segura e 60 segundos de intervalo
client.connect(broker, 1883, 60)

client.loop_start()
print("Inicio em: "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

try:
    while True:
        umidade,temperatura = dht.read_retry(dht.DHT22, 4)
#        umidade = round(umidade, 2)
#        temperatura = round(temperatura, 2)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": "+"Temperatura:"+str(temperatura)+ " Umidade:"+str(umidade))
        sensor['temperatura'] = temperatura
        sensor['umidade'] = umidade

        # Enviando os dados para o thingboard
        client.publish(topic, json.dumps(sensor), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
    print("Parada em: "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


client.loop_stop()
client.disconnect()