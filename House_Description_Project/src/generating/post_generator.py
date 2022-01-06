import datetime
import os
import random

from src.entity import RecruitmentPost

import pandas as pd


class PostGenerator:

    __POST_POOL_PATH = 'data/raw/sell_apartment.csv'

    def __init__(self):
        root_dir = os.getcwd()
        data_path = os.path.join(root_dir, PostGenerator.__POST_POOL_PATH)
        self.__post_pool = pd.read_csv(data_path)

    def generate(self) -> RecruitmentPost:
        rand_post = self.__post_pool.sample(n = 1).iloc[0]
        new_post = RecruitmentPost(
            name=rand_post['name'],
            address=rand_post['address'],
            district=rand_post['district'],
            post_date=rand_post['post_date'],
            expiration_date=rand_post['expiration_date'],
            city=rand_post['city'],
            project_name=rand_post['project_name'],
            investor=rand_post['investor'],
            price=rand_post['price'],
            area=rand_post['area'],
            bedroom=rand_post['bedroom'],
        )
        return new_post


if __name__ == '__main__':
    generator = PostGenerator()
    post = generator.generate()
    print(post.to_dict())
