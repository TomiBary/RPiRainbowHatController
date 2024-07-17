import requests, threading
import time, os, sys, json
import hydratation

def check_hydrat_network():
    try:
        while True:
            print("Test")
            json = requests.get("http://localhost:8080/hydrat").json()
            if json['current_target'] - json['current'] > 0.5:
                print("Napij se !!! {}".format(os.getpid()))
            time.sleep(3)   # 3 seconds.
    except KeyboardInterrupt:
        pass
# Start execution in the background.
# t = threading.Thread(target=check_hydrat)
# print(t.get_native_id())
# t.start()

def check_hydrat_local(check_freq_sec = 30, sound_freq_sec = 60, notify_freq_sec = 600):
    try:
        while True:
            ideal = hydratation.get_ideal_hydration()
            if ideal - hydratation.current_hydration > 0.5:
                print("Mel bys vyipt vodu !!!")
                #TODO Play sound more times when he didnt drink enough
                play_sound()
                displayNotification("You should drink some water!","Hydrat Reminder","subtitle","Pop")
                
            else:
                print("Ideal: {} Current: {}".format(ideal, hydratation.current_hydration))

            time.sleep(check_freq_sec)   # 30 seconds.
    except KeyboardInterrupt:
        pass

def play_sound():
    os.system("afplay /System/Library/Sounds/Ping.aiff")

def displayNotification(message,title=None,subtitle=None,soundname=None):
	"""
		Display an OSX notification with message title an subtitle
		sounds are located in /System/Library/Sounds or ~/Library/Sounds
	"""
	titlePart = ''
	if(not title is None):
		titlePart = 'with title "{0}"'.format(title)
	subtitlePart = ''
	if(not subtitle is None):
		subtitlePart = 'subtitle "{0}"'.format(subtitle)
	soundnamePart = ''
	if(not soundname is None):
		soundnamePart = 'sound name "{0}"'.format(soundname)

	appleScriptNotification = 'display notification "{0}" {1} {2} {3}'.format(message,titlePart,subtitlePart,soundnamePart)
	os.system("osascript -e '{0}'".format(appleScriptNotification))


config_keys = ["check_freq_sec", "sound_freq_sec", "notify_freq_sec"]
config_values_from_args = json.loads(sys.argv[1])
c = config = {config_keys[i]: config_values_from_args[i] for i in range(len(config_keys))}
print(config)
check_hydrat_local(c['check_freq_sec'], c['sound_freq_sec'], c['notify_freq_sec'])
