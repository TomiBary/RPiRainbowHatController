#!/usr/bin/env python
import datetime
import time
from rh_project import project as p
import rainbowhat as rh
import touch_buttons

rh.buzzer.midi_note(80, 0.1)

p.run_test_jobs = False  # True
p.job_repeat_count = 3
p.delay_between_text_letters = 0.2
p.schedule_jobs()

try:
    while True:
        p.run()
except KeyboardInterrupt:
    for c in range(3):
        rh.buzzer.midi_note(150, 0.2)
        time.sleep(0.4)
    rh.display.clear()
    rh.display.show()
    time.sleep(0.5)
