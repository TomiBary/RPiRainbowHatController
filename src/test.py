import crypto
from rh_project import project as p

p.run_test_jobs = True
p.job_repeat_count = 3
p.schedule_jobs()
try:
    while True:
        p.run()
except KeyboardInterrupt:
    print("Exiting...")
