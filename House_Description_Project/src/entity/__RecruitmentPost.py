import json
from datetime import datetime


class RecruitmentPost:

    def __init__(self, name, address, district, post_date, expiration_date,
                 city=None,
                 project_name=None,
                 investor=None,
                 price=None,
                 area=None,
                 bedroom=None):
        self.name = name
        self.address = address
        self.district = district
        self.post_date = post_date
        self.expiration_date = expiration_date
        self.city = city
        self.project_name = project_name
        self.investor = investor
        self.price = str(price)
        self.area = str(area)
        self.bedroom = str(bedroom)

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        dict_data = self.to_dict()
        #dict_data['post_date'] = self.post_date.strftime(format='%d-%m-%Y')
        #dict_data['expiration_date'] = self.expiration_date.strftime(format='%d-%m-%Y')
        return json.dumps(dict_data)
