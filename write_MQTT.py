import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
     
        print("[STATUS] Conectado ao Broker, Resultado de conexao: "+str(rc))

 
        global Connected                
        Connected = True              
 
    else:
 
        print("[STATUS] Não conectou no Broker, Resultado de conexao: "+str(rc))
 
Connected = False   #g
 
broker_address= "test.mosquitto.org"
port = 1883
 
client = mqttClient.Client("FreechainsIOT")               
client.on_connect= on_connect                     
client.connect(broker_address, port=port)        
 
client.loop_start()        
 
while Connected != True:    
    time.sleep(0.1)
 
try:
    while True:
 
        value = input('Digite a mensagem:')
        client.publish("FreechainsIOT/temp",value)


 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()