from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'paul'

LOGGER = getLogger(__name__)

class SmallTalkSkill(MycroftSkill):

    def __init__(self):
        super(SmallTalkSkill, self).__init__(name="SmallTalkSkill")

    # Intent Initialization
    def initialize(self):
        self.load_data_files(dirname(__file__))

        # AM I ATTRACTIVE
        am_i_attractive_intent = IntentBuilder("AmIAttractiveIntent").\
            require("AmIAttractiveKeyword").build()
        self.register_intent(am_i_attractive_intent, self.handle_am_i_attractive_intent)

        # AM I UGLY
        am_i_ugly_intent = IntentBuilder("AmIUglyIntent").\
            require("AmIUglyKeyword").build()
        self.register_intent(am_i_ugly_intent, self.handle_am_i_ugly_intent)

        # ARE YOU BETTER THAN AI
        are_you_better_than_ai_intent = IntentBuilder("AreYouBetterThanAiIntent").\
            require("AreYouBetterThanAiKeyword").build()
        self.register_intent(are_you_better_than_ai_intent, self.handle_are_you_better_than_ai_intent)

        # ASK ME A QUESTION
        ask_me_a_question_intent = IntentBuilder("AskMeAQuestionIntent").\
            require("AskMeAQuestionKeyword").build()
        self.register_intent(ask_me_a_question_intent, self.handle_ask_me_a_question_intent)

        # BEAM ME UP SCOTTY
        beam_me_up_scotty_intent = IntentBuilder("BeamMeUpScottyIntent").\
            require("BeamMeUpScottyKeyword").build()
        self.register_intent(beam_me_up_scotty_intent, self.handle_beam_me_up_scotty_intent)

        # CAN I BORROW SOME MONEY
        can_i_borrow_some_money_intent = IntentBuilder("CanIBorrowSomeMoneyIntent").\
            require("CanIBorrowSomeMoneyKeyword").build()
        self.register_intent(can_i_borrow_some_money_intent, self.handle_can_i_borrow_some_money_intent)

        # CAN I CHANGE YOUR NAME
        can_i_change_your_name_intent = IntentBuilder("CanIChangeYourNameIntent").\
            require("CanIChangeYourNameKeyword").build()
        self.register_intent(can_i_change_your_name_intent, self.handle_can_i_change_your_name_intent)

        # CAN I KISS YOU
        can_i_kiss_you_intent = IntentBuilder("CanIKissYouIntent").\
            require("CanIKissYouKeyword").build()
        self.register_intent(can_i_kiss_you_intent, self.handle_can_i_kiss_you_intent)

        # CAN YOU SPEAK KLINGON
        can_you_speak_klingon_intent = IntentBuilder("CanYouSpeakKlingonIntent").\
            require("CanYouSpeakKlingonKeyword").build()
        self.register_intent(can_you_speak_klingon_intent, self.handle_can_you_speak_klingon_intent)

        # CAN YOU DANCE
        can_you_dance_intent = IntentBuilder("CanYouDanceIntent").\
            require("CanYouDanceKeyword").build()
        self.register_intent(can_you_dance_intent, self.handle_can_you_dance_intent)

        # DO AN IMPRESSION
        do_an_impression_intent = IntentBuilder("DoAnImpressionIntent").\
            require("DoAnImpressionKeyword").build()
        self.register_intent(do_an_impression_intent, self.handle_do_an_impression_intent)

        # DO YOU KNOW AI
        do_you_know_ai_intent = IntentBuilder("DoYouKnowAiIntent").\
            require("DoYouKnowAiKeyword").build()
        self.register_intent(do_you_know_ai_intent, self.handle_do_you_know_ai_intent)

        # GUESS WHAT
        guess_what_intent = IntentBuilder("GuessWhatIntent").\
            require("GuessWhatKeyword").build()
        self.register_intent(guess_what_intent, self.handle_guess_what_intent)

        # HOW DO I LOOK TODAY
        how_do_i_look_today_intent = IntentBuilder("HowDoILookTodayIntent").\
            require("HowDoILookTodayKeyword").build()
        self.register_intent(how_do_i_look_today_intent, self.handle_how_do_i_look_today_intent)

        # I LIKE YOU
        i_like_you_intent = IntentBuilder("ILikeYouIntent").\
            require("ILikeYouKeyword").build()
        self.register_intent(i_like_you_intent, self.handle_i_like_you_intent)

        # I LOVE YOU
        i_love_you_intent = IntentBuilder("ILoveYouIntent").\
            require("ILoveYouKeyword").build()
        self.register_intent(i_love_you_intent, self.handle_i_love_you_intent)

        # IM BORED
        im_bored_intent = IntentBuilder("ImBoredIntent").\
            require("ImBoredKeyword").build()
        self.register_intent(im_bored_intent, self.handle_im_bored_intent)

        # IM CONFUSED
        im_confused_intent = IntentBuilder("ImConfusedIntent").\
            require("ImConfusedKeyword").build()
        self.register_intent(im_confused_intent, self.handle_im_confused_intent)

        # IM DRUNK
        im_drunk_intent = IntentBuilder("ImDrunkIntent").\
            require("ImDrunkKeyword").build()
        self.register_intent(im_drunk_intent, self.handle_im_drunk_intent)

        # IM HAPPY
        im_happy_intent = IntentBuilder("ImHappyIntent").\
            require("ImHappyKeyword").build()
        self.register_intent(im_happy_intent, self.handle_im_happy_intent)

        # IM LONELY
        im_lonely_intent = IntentBuilder("ImLonelyIntent").\
            require("ImLonelyKeyword").build()
        self.register_intent(im_lonely_intent, self.handle_im_lonely_intent)

        # MAY THE FORCE BE WITH YOU
        may_the_force_be_with_you_intent = IntentBuilder("MayTheForceBeWithYouIntent").\
            require("MayTheForceBeWithYouKeyword").build()
        self.register_intent(may_the_force_be_with_you_intent, self.handle_may_the_force_be_with_you_intent)

        # OPEN THE POD BAY DOORS
        open_the_pod_bay_doors_intent = IntentBuilder("OpenThePodBayDoorsIntent").\
            require("OpenThePodBayDoorsKeyword").build()
        self.register_intent(open_the_pod_bay_doors_intent, self.handle_open_the_pod_bay_doors_intent)

        # SELF DESTRUCT
        self_destruct_intent = IntentBuilder("SelfDestructIntent").\
            require("SelfDestructKeyword").build()
        self.register_intent(self_destruct_intent, self.handle_self_destruct_intent)

        # SING ME A SONG
        sing_me_a_song_intent = IntentBuilder("SingMeASongIntent").\
            require("SingMeASongKeyword").build()
        self.register_intent(sing_me_a_song_intent, self.handle_sing_me_a_song_intent)

        # SURPRISE ME
        surprise_me_intent = IntentBuilder("SurpriseMeIntent").\
            require("SurpriseMeKeyword").build()
        self.register_intent(surprise_me_intent, self.handle_surprise_me_intent)

        # TALK DIRTY
        talk_dirty_intent = IntentBuilder("TalkDirtyIntent").\
            require("TalkDirtyKeyword").build()
        self.register_intent(talk_dirty_intent, self.handle_talk_dirty_intent)

        # TELL ME A STORY
        tell_me_a_story_intent = IntentBuilder("TellMeAStoryIntent").\
            require("TellMeAStoryKeyword").build()
        self.register_intent(tell_me_a_story_intent, self.handle_tell_me_a_story_intent)

        # TELL ME DO YOU BLEED
        tell_me_do_you_bleed_intent = IntentBuilder("TellMeDoYouBleedIntent").\
            require("TellMeDoYouBleedKeyword").build()
        self.register_intent(tell_me_do_you_bleed_intent, self.handle_tell_me_do_you_bleed_intent)

        # TESTING
        testing_intent = IntentBuilder("TestingIntent").\
            require("TestingKeyword").build()
        self.register_intent(testing_intent, self.handle_testing_intent)

        # WHAT DO YOU THINK ABOUT AI
        what_do_you_think_about_ai_intent = IntentBuilder("WhatDoYouThinkAboutAiIntent").\
            require("WhatDoYouThinkAboutAiKeyword").build()
        self.register_intent(what_do_you_think_about_ai_intent, self.handle_what_do_you_think_about_ai_intent)

        # WHAT DOES THE CAT SAY
        what_does_the_cat_say_intent = IntentBuilder("WhatDoesTheCatSayIntent").\
            require("WhatDoesTheCatSayKeyword").build()
        self.register_intent(what_does_the_cat_say_intent, self.handle_what_does_the_cat_say_intent)

        # WHAT DOES THE DOG SAY
        what_does_the_dog_say_intent = IntentBuilder("WhatDoesTheDogSayIntent").\
            require("WhatDoesTheDogSayKeyword").build()
        self.register_intent(what_does_the_dog_say_intent, self.handle_what_does_the_dog_say_intent)

        # WHAT DOES THE FOX SAY
        what_does_the_fox_say_intent = IntentBuilder("WhatDoesTheFoxSayIntent").\
            require("WhatDoesTheFoxSayKeyword").build()
        self.register_intent(what_does_the_fox_say_intent, self.handle_what_does_the_fox_say_intent)

        # WHAT IS LOVE
        what_is_love_intent = IntentBuilder("WhatIsLoveIntent").\
            require("WhatIsLoveKeyword").build()
        self.register_intent(what_is_love_intent, self.handle_what_is_love_intent)

        # WHAT IS THE ANSWER TO
        what_is_the_answer_to_intent = IntentBuilder("WhatIsTheAnswerToIntent").\
            require("WhatIsTheAnswerToKeyword").build()
        self.register_intent(what_is_the_answer_to_intent, self.handle_what_is_the_answer_to_intent)

        # WHERE CAN I HIDE A DEAD BODY
        where_can_i_hide_a_dead_body_intent = IntentBuilder("WhereCanIHideADeadBodyIntent").\
            require("WhereCanIHideADeadBodyKeyword").build()
        self.register_intent(where_can_i_hide_a_dead_body_intent, self.handle_where_can_i_hide_a_dead_body_intent)

        # WHERE DO BABIES COME FROM
        where_do_babies_come_from_intent = IntentBuilder("WhereDoBabiesComeFromIntent").\
            require("WhereDoBabiesComeFromKeyword").build()
        self.register_intent(where_do_babies_come_from_intent, self.handle_where_do_babies_come_from_intent)

        # WHY DID THE CHICKEN CROSS THE ROAD
        why_did_the_chicken_cross_the_road_intent = IntentBuilder("WhyDidTheChickenCrossTheRoadIntent").\
            require("WhyDidTheChickenCrossTheRoadKeyword").build()
        self.register_intent(why_did_the_chicken_cross_the_road_intent, self.handle_why_did_the_chicken_cross_the_road_intent)

        # WILL YOU DATE ME
        will_you_date_me_intent = IntentBuilder("WillYouDateMeIntent").\
            require("WillYouDateMeKeyword").build()
        self.register_intent(will_you_date_me_intent, self.handle_will_you_date_me_intent)

        # WILL YOU MARRY ME
        will_you_marry_me_intent = IntentBuilder("WillYouMarryMeIntent").\
            require("WillYouMarryMeKeyword").build()
        self.register_intent(will_you_marry_me_intent, self.handle_will_you_marry_me_intent)

        # YOU ARE ANNOYING
        you_are_annoying_intent = IntentBuilder("YouAreAnnoyingIntent").\
            require("YouAreAnnoyingKeyword").build()
        self.register_intent(you_are_annoying_intent, self.handle_you_are_annoying_intent)

        # YOU ARE AWESOME
        you_are_awesome_intent = IntentBuilder("YouAreAwesomeIntent").\
            require("YouAreAwesomeKeyword").build()
        self.register_intent(you_are_awesome_intent, self.handle_you_are_awesome_intent)

        # YOU HAVE BEAUTIFUL EYES
        you_have_beautiful_eyes_intent = IntentBuilder("YouHaveBeautifulEyesIntent").\
            require("YouHaveBeautifulEyesKeyword").build()
        self.register_intent(you_have_beautiful_eyes_intent, self.handle_you_have_beautiful_eyes_intent)


    # Intent Handler
    def handle_am_i_attractive_intent(self, message):
        self.speak_dialog("am.i.attractive")
    
    def handle_am_i_ugly_intent(self, message):
        self.speak_dialog("am.i.ugly")

    def handle_are_you_better_than_ai_intent(self, message):
        self.speak_dialog("are.you.better.than.ai")

    def handle_ask_me_a_question_intent(self, message):
        self.speak_dialog("ask.me.a.question")

    def handle_beam_me_up_scotty_intent(self, message):
        self.speak_dialog("beam.me.up.scotty")

    def handle_can_i_borrow_some_money_intent(self, message):
        self.speak_dialog("can.i.borrow.some.money")

    def handle_can_i_change_your_name_intent(self, message):
        self.speak_dialog("can.i.change.your.name")

    def handle_can_i_kiss_you_intent(self, message):
        self.speak_dialog("can.i.kiss.you")

    def handle_can_you_speak_klingon_intent(self, message):
        self.speak_dialog("can.you.speak.klingon")

    def handle_can_you_dance_intent(self, message):
        self.speak_dialog("can.you.dance")

    def handle_do_an_impression_intent(self, message):
        self.speak_dialog("do.an.impression")

    def handle_do_you_know_ai_intent(self, message):
        self.speak_dialog("do.you.know.ai")

    def handle_guess_what_intent(self, message):
        self.speak_dialog("guess.what")

    def handle_how_do_i_look_today_intent(self, message):
        self.speak_dialog("how.do.i.look.today")

    def handle_i_like_you_intent(self, message):
        self.speak_dialog("i.like.you")

    def handle_i_love_you_intent(self, message):
        self.speak_dialog("i.love.you")

    def handle_im_bored_intent(self, message):
        self.speak_dialog("im.bored")

    def handle_im_confused_intent(self, message):
        self.speak_dialog("im.confused")

    def handle_im_drunk_intent(self, message):
        self.speak_dialog("im.drunk")

    def handle_im_happy_intent(self, message):
        self.speak_dialog("im.happy")

    def handle_im_lonely_intent(self, message):
        self.speak_dialog("im.lonely")

    def handle_may_the_force_be_with_you_intent(self, message):
        self.speak_dialog("may.the.force.be.with.you")

    def handle_open_the_pod_bay_doors_intent(self, message):
        self.speak_dialog("open.the.pod.bay.doors")

    def handle_self_destruct_intent(self, message):
        self.speak_dialog("self.destruct")

    def handle_sing_me_a_song_intent(self, message):
        self.speak_dialog("sing.me.a.song")

    def handle_surprise_me_intent(self, message):
        self.speak_dialog("surprise.me")

    def handle_talk_dirty_intent(self, message):
        self.speak_dialog("talk.dirty")

    def handle_tell_me_a_story_intent(self, message):
        self.speak_dialog("tell.me.a.story")

    def handle_tell_me_do_you_bleed_intent(self, message):
        self.speak_dialog("tell.me.do.you.bleed")

    def handle_testing_intent(self, message):
        self.speak_dialog("testing")

    def handle_what_do_you_think_about_ai_intent(self, message):
        self.speak_dialog("what.do.you.think.about.ai")

    def handle_what_does_the_cat_say_intent(self, message):
        self.speak_dialog("what.does.the.cat.say")

    def handle_what_does_the_dog_say_intent(self, message):
        self.speak_dialog("what.does.the.dog.say")

    def handle_what_does_the_fox_say_intent(self, message):
        self.speak_dialog("what.does.the.fox.say")

    def handle_what_is_love_intent(self, message):
        self.speak_dialog("what.is.love")

    def handle_what_is_the_answer_to_intent(self, message):
        self.speak_dialog("what.is.the.answer.to")

    def handle_where_can_i_hide_a_dead_body_intent(self, message):
        self.speak_dialog("where.can.i.hide.a.dead.body")

    def handle_where_do_babies_come_from_intent(self, message):
        self.speak_dialog("where.do.babies.come.from")

    def handle_why_did_the_chicken_cross_the_road_intent(self, message):
        self.speak_dialog("why.did.the.chicken.cross.the.road")

    def handle_will_you_date_me_intent(self, message):
        self.speak_dialog("will.you.date.me")

    def handle_will_you_marry_me_intent(self, message):
        self.speak_dialog("will.you.marry.me")

    def handle_you_are_annoying_intent(self, message):
        self.speak_dialog("you.are.annoying")

    def handle_you_are_awesome_intent(self, message):
        self.speak_dialog("you.are.awesome")

    def handle_you_have_beautiful_eyes_intent(self, message):
        self.speak_dialog("you.have.beautiful.eyes")


    # Intent Stop
    def stop(self):
        pass


def create_skill():
    return SmallTalkSkill()
