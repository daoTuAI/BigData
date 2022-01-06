# Created by quang at 9/11/2021
import json
import time

from src.generating.post_generator import PostGenerator

from kafka import KafkaProducer

BOOTSTRAP_SERVERS = ['kafka:9093', 'kafka1:9093']

TOPIC = 'post'


class KafkaSender:

    def __init__(self):
        self.__producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

    def send(self, topic: str, message: str):
        return self.__producer.send(topic, bytearray(message.encode()))


class PostStreamingSimulator:

    def __init__(self, n_post_per_sec=1):
        self.__post_generator = PostGenerator()
        self.__kafka_sender = KafkaSender()
        self.__n_post_per_sec = n_post_per_sec

    def simulating(self):
        while True:
            for i in range(self.__n_post_per_sec):
                post = self.__post_generator.generate().to_json()
                print(post)
                sending = self.__kafka_sender.send(TOPIC, post)
                meta_data = sending.get(10)
            time.sleep(10)
