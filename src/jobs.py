import time
import asyncio


class JobScheduler:

    def __init__(self):
        self.jobs = []

    def add_jobs(self, *jobs):
        self.jobs.extend(jobs)

    def add_job(self, job):
        self.jobs.append(job)

    def run(self):
        jobs_count = len(self.jobs)
        if jobs_count > 0:
            print(f"Scheduled jobs: {jobs_count}, {list(map(lambda x: x.name, self.jobs))}")
        self.jobs[:] = [j for j in self.jobs if not j.is_finished]
        for job in self.jobs[:]:
            if job.run() is True:
                self.jobs.remove(job)  # TODO if job is removed next job is not executed as next


class Job:
    is_finished = False

    @staticmethod
    def pause(seconds=1):
        return Job("Pause job", False, time.sleep, (seconds,))

    def __init__(self, name, is_async, job_func, args=None):
        self.name = name
        self.is_async = is_async
        self.job_func = job_func
        self.args = args

    def with_args(self, args):
        self.args = args
        return self

    def run(self):
        if self.is_async:
            return asyncio.run(self.job_func(*self.args))
        else:
            if self.args:
                return self.job_func(*self.args)
            else:
                return self.job_func()

    def __mul__(self, multiplier):
        if not isinstance(multiplier, int) or multiplier < 0:
            raise TypeError("Multiplier must be a non-negative integer")
        return [Job(self.name, self.is_async, self.job_func, self.args) for _ in range(multiplier)]

    def __str__(self):
        return f"Job({self.name}, {self.is_async}, {self.job_func}, {self.args})"

    def __repr__(self):
        return f"Job({self.name}, {self.is_async}, {self.job_func}, {self.args})"
