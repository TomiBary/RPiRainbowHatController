import schedule
import rh_jobs
from jobs import *


class Project:
    message = None
    run_test_jobs = False
    delay_between_text_letters = 0.2  # Seconds
    job_repeat_count = 5  # How many times to repeat the job

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
        self.schedule_jobs_internal(self.fetch_crypto_prices_jobs)

    # Schedule the job to run every 10 minutes
    def schedule_display_crypto_prices_job(self):
        self.schedule_jobs_internal(self.display_crypto_prices_jobs)

    def schedule_display_time_job(self):
        self.schedule_jobs_internal(self.display_time_jobs)

    def schedule_display_date_job(self):
        self.schedule_jobs_internal(self.display_date_jobs)

    def schedule_jobs_internal(self, *jobs):
        self.job_scheduler.add_jobs(jobs)

    def create_jobs(self):
        self.fetch_crypto_prices_jobs = Job("Fetch prices", False, rh_jobs.fetch_crypto_prices_job,
                                            (self.job_repeat_count,))
        self.display_crypto_prices_jobs = Job("Display prices", False, rh_jobs.display_crypto_prices_job)
        self.display_time_jobs = Job("Display time", False, rh_jobs.display_time_job) * self.job_repeat_count
        self.display_date_jobs = Job("Display date", False, rh_jobs.display_date_job) * self.job_repeat_count
        # Needs to be run at the start, to get the current prices for display job
        self.job_scheduler.add_job(self.fetch_crypto_prices_jobs)

    def schedule_jobs(self):
        self.create_jobs()
        if self.run_test_jobs:
            self.job_scheduler.add_jobs(self.fetch_crypto_prices_jobs, self.display_crypto_prices_jobs,
                                        *self.display_time_jobs, *self.display_date_jobs)
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
