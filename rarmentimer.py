# -*- coding: utf-8 -*
from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
import time
from kivy.clock import Clock
from datetime import datetime, timedelta

Config.set('graphics', 'width', '460')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'resizable', False)
Builder.load_file("rarmentimer.kv")


class RarmenTimer(App):
    stop_watch_start = False
    seconds = 180

    def __init__(self, **kwargs):
        super(RarmenTimer, self).__init__(**kwargs)
        self.title = 'Rarmen Timer'
        now = datetime.now()
        self.wait_time = datetime(now.year, now.month, now.day, hour=0, minute=0, second=0)
        self.wait_time = self.wait_time + timedelta(seconds=self.seconds)

    def build(self):
        self.root.ids.time.text = '{}'.format(
            self.wait_time.time().strftime("%M:%S"))

    def update_time(self, seconds):
        if self.stop_watch_start:
            self.wait_time -= timedelta(seconds=1)

        self.root.ids.time.text = '{}'.format(
            self.wait_time.time().strftime("%M:%S"))

    def start_stop(self):
        if self.stop_watch_start:
            self.stop_watch_start = False
            self.root.ids.bt_start_stop.text = 'Start'
            Clock.unschedule(self.update_time)
        else:
            self.stop_watch_start = True
            self.root.ids.bt_start_stop.text = 'Stop'
            Clock.schedule_interval(self.update_time, 1)

    def reset(self):

        if self.stop_watch_start:
            self.root.ids.bt_start_stop.text = 'Start'
            self.stop_watch_start = False

        now = datetime.now()
        self.wait_time = datetime(now.year, now.month, now.day, hour=0, minute=0, second=0)
        self.wait_time = self.wait_time + timedelta(seconds=180)

        self.root.ids.time.text = '{}'.format(
            self.wait_time.time().strftime("%M:%S"))


if __name__ == '__main__':
    RarmenTimer().run()
