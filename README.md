Mycroft Skills
==============

1. 'bad_words' -> filters inputs for profanities, etc., Check vocab file for a full list.
2. 'flip_coin' -> simulates coin flip (single and double coin flip). Check vocab file for keyphrase input.
3. 'roll_dice' -> simulates die roll (single and double die roll). Check vocab file for keyphrase input.
4. 'random_quotes' -> allows mycroft to speak autonomously in a random interval. Check init.py to adjust probability.
5. 'rock_paper_scissors' -> play a game of rock, paper and scissors with mycroft.
6. 'small_talk' -> chat with mycroft. Check vocab files for inputs. Feel free to edit and add dialogs that may add an extra feel.

Misc Folder
===========

Inside are 'beep-hi.wav' and 'beep-lo.wav' sound files.

1. Place them in a directory i.e. mycroft's root directory.
2. Open 'mycroft/client/speech/mic.py'.
3. Add "play_wav('/home/user/path/to/beep_hi.wav')" and "play_wav('/home/user/path/to/beep_lo.wav')" inside listen function, before the line, 'logger.debug  
   ("Listening)' and after 'logger.debug("Thinking...")', respectively.

   For Example:

		play_wav('/home/paul/Irene/misc/beep_hi.wav')
        
        logger.debug("Listening...")        
        emitter.emit("recognizer_loop:record_begin")
        frame_data = self.record_phrase(source, sec_per_buffer)
        audio_data = self.create_audio_data(frame_data, source)
        emitter.emit("recognizer_loop:record_end")
        logger.debug("Thinking...")

        play_wav('/home/paul/Irene/misc/beep_lo.wav')



NOTE: This is my personal preference to add a notification sound when mycroft starts listening and when he accepts an input.
