import Singleton
from django.shortcuts import render
from django.http import HttpResponse
import random
from paho.mqtt import client as mqtt_client
import threading


class Fuzzy:

    def __init__(self):
        self.temp = None
        self.umidade = None
        self.broker = 'broker.emqx.io'
        self.port = 1883
        self.client_id = f'python-mqtt-{random.randint(0, 1000)}'

    def connect_mqtt(self):

        def on_connect(client, userdata, flags, rc):
            """
            :param rc:
            :param flags:
            :param userdata:
            :type client: object
            """
            if rc == 0:
                print("Conectado")
            else:
                print("Error code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        client.subscribe("CoffeeTech/temperatura")
        client.subscribe("CoffeeTech/umidade")
        return client

    def on_message(self, client, userdata, message):
        """
        :param message:
        :param userdata:
        :type client: object
        """

        if message.topic == 'CoffeeTech/temperatura':
            self.temp = message.payload.decode()

        elif message.topic == 'CoffeeTech/umidade':
            self.umidade = message.payload.decode()

        print('-------------Novos dados Setados--------------')
        if self.temp is not None:
            print("Temperatura setada: " + self.temp)
        if self.umidade is not None:
            print("Umidade setada: " + self.umidade)

    def publish(self, client):
        """
        :type client: object
        """
        while True:
            client.on_message = self.on_message


class Teste(Singleton, threading.Thread):
    def __int__(self):
        threading.Thread.__init__(self)
        print(f'Are they alive? {self.is_alive()}')

    def run(self):

        fuzzy = Fuzzy()
        client = fuzzy.connect_mqtt()
        client.loop_stop()
        client.loop_start()
        fuzzy.publish(client)


def home(request):
    status = None

    if request.user.is_authenticated :

        teste = Teste()

        teste.start()

        # thread = threading.Thread(target=run, args=(5,))

        status = 'Ativado'
    else:
        status = 'Desativado'

    context = {
        'status': status,
    }
    return render(request, 'coffeetech/home.html', context)




