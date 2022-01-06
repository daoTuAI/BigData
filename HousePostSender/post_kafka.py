from kafka import KafkaConsumer
from post_sender import Sender

import json
import pandas as pd


sender = Sender(elastic_host = 'http://es01:9200/',
                index = 'test-post')

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('Preprocessing_Post',
                         bootstrap_servers=['kafka:9093'],
                         auto_offset_reset='latest', enable_auto_commit=False)

list_post = []

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                       message.offset, message.key,
    #                                       message.value.decode('utf-8')))

    post = json.loads(message.value.decode('utf-8'))
    list_post.append(post)
    
    if len(list_post) > 1:
        responses = sender.send_json(list_post)
        print(responses)
        list_post = []
