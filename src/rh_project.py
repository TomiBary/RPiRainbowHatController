import schedule, time
from jobs import *
from utils import get_crypto_price_message, rh_display_text
from datetime import datetime as dt


def fetch_crypto_prices_job(*args):
    Project.message = get_crypto_price_message()
    Project.message.text *= args[1]
    print(f"Fetched crypto prices")
    return True


def display_crypto_prices_job(*args):
    msg = Project.message
    print("Crypto prices:" + msg.text)
    while msg.is_next():
        time.sleep(0.2)
        text = msg.get_next()
        rh_display_text(text)
    rh_display_text()
    msg.set_index(0)
    return True


def display_time_job(*args):
    current_time = dt.now().strftime('%H.%M')  # time.strftime('%H.%M', time.gmtime())
    print("Time:" + current_time)
    rh_display_text(current_time)
    time.sleep(1.2)
    rh_display_text()
    time.sleep(0.3)
    return True


def display_date_job(*args):
    current_date = dt.now().strftime('%d.%m.')  # time.strftime('%d.%m.', time.gmtime())
    print("Date:" + current_date)
    rh_display_text(current_date)
    time.sleep(1.2)
    rh_display_text()
    time.sleep(0.3)
    return True


class Project:
    message = None
    add_pause_jobs = False
    run_test_jobs = False
    job_repeat_count = 3  # How many times to repeat the job

    fetch_crypto_prices_jobs = []
    display_crypto_prices_jobs = []
    display_time_jobs = []
    display_date_jobs = []

    # Instantiate the JobScheduler
    job_scheduler = JobScheduler()

    def __init__(self, job_repeat_count=3, run_test_jobs=False):
        self.job_repeat_count = job_repeat_count
        self.run_test_jobs = run_test_jobs

    def schedule_fetch_crypto_prices_job(self):
        self.job_scheduler.add_job(self.fetch_crypto_prices_jobs)
        if self.add_pause_jobs:
            self.job_scheduler.add_job(Job.pause())

    # Schedule the job to run every 10 minutes
    def schedule_display_crypto_prices_job(self):
        self.job_scheduler.add_job(self.display_crypto_prices_jobs)
        if self.add_pause_jobs:
            self.job_scheduler.add_job(Job.pause())

    def schedule_display_time_job(self):
        self.job_scheduler.add_jobs(*self.display_time_jobs)
        if self.add_pause_jobs:
            self.job_scheduler.add_job(Job.pause())

    def schedule_display_date_job(self):
        self.job_scheduler.add_jobs(*self.display_date_jobs)
        if self.add_pause_jobs:
            self.job_scheduler.add_job(Job.pause())

    def create_jobs(self):
        # Fetch shouldn't be repeated
        self.fetch_crypto_prices_jobs = Job("Fetch prices", False, fetch_crypto_prices_job, (1, self.job_repeat_count))
        self.display_crypto_prices_jobs = Job("Display prices", False, display_crypto_prices_job, (4, ))
        self.display_time_jobs = Job("Display time", False, display_time_job, (2,)) * self.job_repeat_count
        self.display_date_jobs = Job("Display date", False, display_date_job, (3,)) * self.job_repeat_count
        # Needs to be run at the start, to get the current prices for display job
        self.job_scheduler.add_job(self.fetch_crypto_prices_jobs)

    def schedule_jobs(self):
        self.create_jobs()
        if self.run_test_jobs:
            # TODO schedule jobs to the second scheduler to call them instantly. self.job_scheduler.add_job(Job.pause(10))
            schedule.every().minute.at(":30").do(self.schedule_fetch_crypto_prices_job)
            schedule.every().minute.at(":00").do(self.schedule_display_crypto_prices_job)
            schedule.every().minute.at(":05").do(self.schedule_display_date_job)
            schedule.every().minute.at(":10").do(self.schedule_display_time_job)
        else:
            schedule.every(20).minutes.at(":00").do(self.schedule_fetch_crypto_prices_job)
            schedule.every(5).minutes.at(":30").do(self.schedule_display_crypto_prices_job)
            schedule.every().hour.at(":05").do(self.schedule_display_date_job)
            schedule.every().hour.at(":00").do(self.schedule_display_time_job)
            schedule.every().hour.at(":15").do(self.schedule_display_time_job)
            schedule.every().hour.at(":30").do(self.schedule_display_time_job)
            schedule.every().hour.at(":45").do(self.schedule_display_time_job)

    def run(self):
        schedule.run_pending()  # Run the scheduled jobs -> Add them to the sequential JobScheduler queue
        self.job_scheduler.run()  # Run the JobScheduler queue
        time.sleep(1)


project = Project()
