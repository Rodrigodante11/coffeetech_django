from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import random
from paho.mqtt import client as mqtt_client
import threading
from dashboard.models import Dashboard
from django.contrib.auth.models import User

userLog = None


# my_module.py
class Singleton:
    _instance = None

    def __init__(self):
        self.some_attribute = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            thread = Thread()
            thread.start()
        return cls._instance


class Fuzzy:

    def __init__(self):
        self.temp = '0'
        self.umidade = '0'
        self.timer = '0'
        self.power = False
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
        client.subscribe("CoffeeTech/power")
        client.subscribe("CoffeeTech/timer")
        return client

    def on_message(self, client, userdata, message):
        """
        :param message:
        :param userdata:
        :type client: object
        """
        dashboardModel = Dashboard()

        if message.topic == 'CoffeeTech/temperatura':
            self.temp = message.payload.decode()

        elif message.topic == 'CoffeeTech/umidade':
            self.umidade = message.payload.decode()

        elif message.topic == 'CoffeeTech/power':
            # print(message.payload.decode())
            self.power = True if message.payload.decode() == '1' else False
        elif message.topic == 'CoffeeTech/timer':
            self.timer = message.payload.decode()

        user = User.objects.get(username=userLog)

        if self.power:

            dashboardModel.umidade = self.umidade
            dashboardModel.temperatura = self.temp
            dashboardModel.power = self.power
            dashboardModel.tempo = self.timer
            dashboardModel.usuario = user
            dashboardModel.pk = 1
            dashboardModel.save()
            print('-------------Novos dados Setados--------------')
            print('Esta ligado!!')

        if not self.power:
            print('-------------Novos dados Setados--------------')
            print('Esta Desligado!!')
        print("Tempo escolhido: " + self.timer)
        print("Temperatura setada: " + self.temp)
        print("Umidade setada: " + self.umidade)
        print(user)

    def publish(self, client):
        """
        :param loop:
        :type client: object
        """
        while True:
            client.on_message = self.on_message


class Thread(threading.Thread):
    def __int__(self):
        threading.Thread.__init__(self)
        print(f'Are they alive? {self.is_alive()}')

    def run(self):
        fuzzy = Fuzzy()
        client = fuzzy.connect_mqtt()
        client.loop_stop()
        client.loop_start()
        fuzzy.publish(client)


# Create your views here.
def dashboard(request):

    if request.user.is_authenticated:
        global userLog
        userLog = request.user.username
        thread = Singleton.instance()
        context = {
            'status': Dashboard.objects.get(id=1),
        }

        return render(request, 'coffeetech/dashboard.html', context)
    return render(request, 'coffeetech/dashboard.html')

