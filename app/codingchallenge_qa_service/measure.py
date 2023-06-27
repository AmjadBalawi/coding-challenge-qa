from datetime import datetime, timezone
from time import perf_counter


class Clock:
    def __init__(self):
        self.start_time = None
        self.stop_time = None

    def start(self):
        self.reset()
        self.start_time = perf_counter()

    def stop(self) -> float:
        self.stop_time = perf_counter()
        return self.get_elapsed_time()

    def get_elapsed_time(self) -> float:
        if self.start_time is None or self.stop_time is None:
            return None
        return self.stop_time - self.start_time

    def reset(self):
        self.start_time = None
        self.stop_time = None


class Measure:
    @staticmethod
    def start_clock() -> Clock:
        clock = Clock()
        clock.start()
        return clock

    @staticmethod
    def stop_clock(clock: Clock) -> float:
        return clock.stop()

    @staticmethod
    def current_time():
        return datetime.now(timezone.utc).isoformat(timespec='microseconds')
