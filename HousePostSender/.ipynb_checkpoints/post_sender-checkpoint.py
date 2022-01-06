from elasticsearch7 import Elasticsearch

import json


class Sender:

    def __init__(self, elastic_host, index):
        self.__elastic_host = elastic_host #= 'http://167.172.76.134:9200/'

        self.__index = index

        self.__es = Elasticsearch(hosts=[elastic_host], 
                                  use_ssl=False)

    def send(self, df): 
        top = 0
        down = 0

        response = []

        while top < df.shape[0]:
            down = top + 1000

            entries = df.iloc[top:down].to_dict(orient='records')
            
            body = []
            
            for i, entry in enumerate(entries):
                body.append({'index': {'_index': self.__index, '_type': '_doc', '_id': top + i}})
                body.append(entry)
                
            response.append(self.__es.bulk(body=body))
            
            top = down

        return response

    def send_json(self, jsons): 
        top = 0
        down = 0

        response = []

        while top < len(jsons):
            down = top + 1000
            # entries = [json.loads(e) for e in jsons[top:down]]
            entries = jsons[top:down]
            body = []
            
            for i, entry in enumerate(entries):
                body.append({'index': {'_index': self.__index, '_type': '_doc'}})
                body.append(entry)
                
            response.append(self.__es.bulk(body=body))
            
            top = down
        return response
