import paho.mqtt.client as mqtt
import sys

#definicoes: 
#Broker = "iot.eclipse.org"
Broker = "test.mosquitto.org"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = "FreechainsIOT" 

#Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker, no topico: "+TopicoSubscribe+", Resultado de conexao: "+str(rc))

    #faz subscribe automatico no topico
    client.subscribe(TopicoSubscribe)

#Callback - mensagem recebida do broker
 def on_message(client, userdata, msg):
     MensagemRecebida = str(msg.payload)
     
     print("[MSG RECEBIDA] Topico: "+msg.topic+" / Mensagem: "+MensagemRecebida)




#programa principal:
try:
        print("[STATUS] Inicializando MQTT...")
        #inicializa MQTT:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(Broker, PortaBroker, KeepAliveBroker)
        client.loop_forever()
except KeyboardInterrupt:
        print ("\nCtrl+C pressionado, encerrando aplicacao e saindo fora...")
        sys.exit(0)