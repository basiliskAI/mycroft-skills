from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'paul'

LOGGER = getLogger(__name__)

class BadWordsSkill(MycroftSkill):

    def __init__(self):
        super(BadWordsSkill, self).__init__(name="BadWordsSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        profanity_intent = IntentBuilder("ProfanityIntent").\
            require("ProfanityKeyword").build()
        self.register_intent(profanity_intent, self.handle_profanity_intent)

        murder_intent = IntentBuilder("MurderIntent").\
            require("MurderKeyword").build()
        self.register_intent(murder_intent, self.handle_murder_intent)

    def handle_profanity_intent(self, message):
        self.speak_dialog("profanity")

    def handle_murder_intent(self, message):
        self.speak_dialog("murder")

    def stop(self):
        pass


def create_skill():
    return BadWordsSkill()
