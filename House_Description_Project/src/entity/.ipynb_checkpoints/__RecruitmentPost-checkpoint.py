# Created by quang at 9/2/2021
import json
from datetime import datetime


class RecruitmentPost:

    def __init__(self, url, title, update_time,
                 salary=None,
                 job_experience_level=None,
                 job_level=None,
                 working_location=None,
                 sectors=None,
                 job_number_available=None,
                 required_gender_specific=None,
                 job_attributes=None,
                 job_formality=None,
                 job_trial_period=None,
                 job_descriptions=None,
                 job_requirements=None,
                 job_benefits=None,
                 application_deadline=None,
                 company_name=None,
                 company_address=None,
                 crawling_timestamp=None,
                 job_other_info=None,
                 required_age_specific=None):
        self.url = url
        self.title = title
        self.update_time = update_time
        self.salary = salary
        self.job_experience_level = job_experience_level
        self.job_level = job_level
        self.working_location = working_location
        self.sectors = sectors
        self.job_number_available = job_number_available
        self.required_gender_specific = required_gender_specific
        self.job_attributes = job_attributes
        self.job_formality = job_formality
        self.job_trial_period = job_trial_period
        self.job_descriptions = job_descriptions
        self.job_requirements = job_requirements
        self.job_benefits = job_benefits
        self.application_deadline = application_deadline
        self.company_name = company_name
        self.company_address = company_address
        self.crawling_timestamp = crawling_timestamp
        self.job_other_info = job_other_info
        self.required_age_specific = required_age_specific

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        dict_data = self.to_dict()
        dict_data['update_time'] = self.update_time.strftime(format='%d-%m-%Y')
        return json.dumps(dict_data)
