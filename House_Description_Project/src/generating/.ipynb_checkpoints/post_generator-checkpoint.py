# Created by quang at 9/4/2021
import datetime
import os
import random

from src.entity import RecruitmentPost

import pandas as pd


class PostGenerator:

    __POST_POOL_PATH = 'data/raw/job_description.csv'

    def __init__(self):
        root_dir = os.getcwd()
        data_path = os.path.join(root_dir, PostGenerator.__POST_POOL_PATH)
        self.__post_pool = pd.read_csv(data_path)

    def generate(self) -> RecruitmentPost:
        rand_post = self.__post_pool.sample(n = 1).iloc[0]
        now = datetime.datetime.now()
        r_hour = random.randint(1, 5)
        r_minutes = random.randint(1, 30)
        r_second = random.randint(1, 30)
        update_time = now - datetime.timedelta(hours=r_hour,
                                               minutes=r_minutes,
                                               seconds=r_second)
        new_post = RecruitmentPost(
            url=rand_post['url'],
            title=rand_post['title'],
            update_time=update_time,
            salary=rand_post['salary'],
            job_experience_level=rand_post['job_experience_years'],
            job_level=rand_post['job_level'],
            working_location=rand_post['working_location'],
            sectors=rand_post['sectors'],
            job_number_available=rand_post['job_number_available'],
            required_gender_specific=rand_post['required_gender_specific'],
            job_attributes=rand_post['job_attributes'],
            job_formality=rand_post['job_formality'],
            job_trial_period=rand_post['job_trial_period'],
            job_descriptions=rand_post['job_descriptions'],
            job_requirements=rand_post['job_requirements'],
            job_benefits=rand_post['job_benefits'],
            application_deadline=rand_post['application_deadline'],
            company_name=rand_post['company_name'],
            company_address=rand_post['company_address'],
            crawling_timestamp=now.strftime('%d/%m/%Y %H:%M:%S'),
            job_other_info=rand_post['job_other_info'],
            required_age_specific=rand_post['required_age_specific']
        )
        return new_post


if __name__ == '__main__':
    generator = PostGenerator()
    post = generator.generate()
    print(post.to_dict())