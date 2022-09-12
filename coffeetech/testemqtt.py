# import random
# from paho.mqtt import client as mqtt_client
#
# class Fuzzy:
#     def __init__(self):
#         self.temp = None
#         self.umidade = None
#         self.setpoint_changed = 36
#         self.broker = 'broker.emqx.io'
#         self.port = 1883
#         self.client_id = f'python-mqtt-{random.randint(0, 1000)}'
#
#     def connect_mqtt(self):
#         def on_connect(client, userdata, flags, rc):
#             """
#             :param rc:
#             :param flags:
#             :param userdata:
#             :type client: object
#             """
#             if rc == 0:
#                 print("Conectado")
#             else:
#                 print("Error code %d\n", rc)
#
#         client = mqtt_client.Client(self.client_id)
#         client.on_connect = on_connect
#         client.connect(self.broker, self.port)
#         client.subscribe("CoffeeTech/temperatura")
#         client.subscribe("CoffeeTech/umidade")
#         return client
#
#     def on_message(self, client, userdata, message):
#         """
#         :param message:
#         :param userdata:
#         :type client: object
#         """
#
#         if message.topic == 'CoffeeTech/temperatura':
#             self.temp = message.payload.decode()
#             self.setpoint_changed = int(self.temp)
#
#         elif message.topic == 'CoffeeTech/umidade':
#             self.umidade = message.payload.decode()
#             self.setpoint_changed = int(self.umidade)
#
#         print('-------------Novos dados Setados--------------')
#         if self.temp is not None:
#             print("Temperatura setada: " + self.temp)
#         if self.umidade is not None:
#             print("Umidade setada: " + self.umidade)
#
#     def publish(self, client):
#         """
#         :type client: object
#         """
#         while True:
#             client.on_message = self.on_message
#
#
# def run():
#     fuzzy = Fuzzy()
#     client = fuzzy.connect_mqtt()
#     client.loop_start()
#     fuzzy.publish(client)
#
#
# run()

import threading


def countdown(thread, count):
  while count > 0:
    count -= 1


class Frankenstein(threading.Thread):
  def __init__(self, nickname, lifespan):
    threading.Thread.__init__(self)
    self.nickname = nickname
    self.lifespan = lifespan
    print(f'{nickname} created before run(). Alive yet? {self.is_alive()}')

  def run(self):
    print(f'{self.nickname} rising...')
    print(f'Are they alive? {self.is_alive()}')
    countdown(self, self.lifespan)


frankie = Frankenstein("Frankie", 5)

frankie.start()
frankie.join()

print(f'Are they still alive? {frankie.is_alive()}')