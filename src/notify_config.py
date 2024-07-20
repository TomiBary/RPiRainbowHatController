class NotifyConfig: #singleton
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(NotifyConfig, cls).__new__(cls)
            cls.instance.check_freq_sec = 10
            cls.instance.sound_freq_sec = 60
            cls.instance.notify_freq_sec = 200
            cls.instance.notified_without_hydrat = 0
            cls.instance.time_notify_count = {
                5: 1,
                20: 3,
                100: 5
            }
        return cls.instance

    def get_notify_count(self):
        for k in self.instance.time_notify_count.keys():
            if k >= self.instance.notified_without_hydrat:
                v = self.instance.time_notify_count[k]
                print(f"get_notify_count = {v}, notified_without_hydrat = {self.instance.notified_without_hydrat}")
                return v
        print("Error in get_notify_count")
        return 1

CONFIG = NotifyConfig().instance
