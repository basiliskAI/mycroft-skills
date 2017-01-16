from adapt.intent import IntentBuilder
from os.path import dirname
from requests import HTTPError

from mycroft.messagebus.message import Message
from mycroft.skills.scheduled_skills import ScheduledSkill

import random

__author__ = 'paulquinit'


class RandomQuotesSkill(ScheduledSkill):
    def __init__(self):
        super(RandomQuotesSkill, self).__init__("RandomQuotesSkill")
        chance = random.randint(10,2010)
        self.max_delay = chance

    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.schedule()

    def notify(self, timestamp):
        self.speak_dialog("random.quotes")
        self.schedule()

    def get_times(self):
        chance = random.randint(10,2010)
        self.max_delay = chance
        return [self.get_utc_time() + self.max_delay]

    def stop(self):
        pass


def create_skill():
    return RandomQuotesSkill()
