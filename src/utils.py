import os

def play_sound(sound_name=None):
    """
        Play a sound
        sounds are located in /System/Library/Sounds or ~/Library/Sounds
    """

    default_sound = '/System/Library/Sounds/Ping.aiff'
    sounds_dir = '/System/Library/Sounds'
    #check if sound_name contains .
    if not sound_name is None and not '.' in sound_name:
        sound_name = sound_name + '.aiff'

    sound_to_play_path = os.path.join(sounds_dir, sound_name)

    if not os.path.exists(sound_to_play_path):
        files = [f for f in os.listdir(sounds_dir) if os.path.isfile(os.path.join(sounds_dir, f))]
        print(f'Sound: "{sound_to_play_path}" does not exist')
        print(f'Available sounds: {files}')
        os.system(f"afplay {default_sound}")
        return

    os.system(f"afplay {sound_to_play_path}")
    print(f'Playing sound: {sound_to_play_path}')

def display_notification(message,title=None,subtitle=None,soundname=None):
    """
        Display an OSX notification with message title an subtitle
        sounds are located in /System/Library/Sounds or ~/Library/Sounds
    """
    title_part = ''
    if not title is None:
        title_part = f'with title "{title}"'
    subtitle_part = ''
    if not subtitle is None:
        subtitle_part = f'subtitle "{subtitle}"'
    soundname_part = ''
    if not soundname is None:
        soundname_part = f'sound name "{soundname}"'

    apple_script_notification = 'display notification "{0}" {1} {2} {3}'.format(message,title_part,subtitle_part,soundname_part)
    os.system(f"osascript -e '{apple_script_notification}'")