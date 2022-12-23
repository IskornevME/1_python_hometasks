import time
from typing import Union, TypeVar, TextIO


Number = Union[None, int, float]
Str = Union[str, None]
FileObj = Union[TextIO, None]
SelfMetricTimer = TypeVar("SelfMetricTimer", bound="MetricTimer")


class BaseMetric:
    metric_type: Str = None

    def __init__(self, name: str):
        self.name = name
        self.value: Number = None

    def get_name(self) -> str:
        if self.metric_type:
            return str(self.name) + "." + str(self.metric_type)
        return ""

    def get_value(self) -> Number:
        return self.value

    def add(self, value=None):
        pass

    def clear(self):
        self.value = None


class MetricAvg(BaseMetric):
    metric_type: Str = "avg"

    def __init__(self, name: str):
        super().__init__(name)
        self.num_calls: int = 0

    def get_name(self) -> str:
        return super().get_name()

    def get_value(self) -> Number:
        return self.value

    def add(self, value: Number = None):
        if not value:
            raise ValueError("please enter some value")
        self.num_calls += 1
        if self.value:
            self.value = (self.value * (self.num_calls - 1) + value) / self.num_calls
        else:
            self.value = value

    def clear(self):
        super().clear()
        self.num_calls = 0


class MetricCount(BaseMetric):
    metric_type: Str = "count"

    def __init__(self, name: str):
        super().__init__(name)
        self.num_calls: int = 0

    def get_name(self) -> str:
        return super().get_name()

    def get_value(self) -> Number:
        return self.value

    def add(self, value: Number = None):
        if value:
            raise ValueError("No need to specify args")
        self.num_calls += 1
        self.value = self.num_calls

    def clear(self):
        super().clear()
        self.num_calls = 0


class MetricTimer(BaseMetric):
    metric_type: Str = "timer"

    def __init__(self, name: str, file: FileObj = None):
        super().__init__(name)
        self.start: float = 0
        self.end: float = 0
        self.file: FileObj = file
        self.num_calls: int = 0

    def __enter__(self: SelfMetricTimer) -> SelfMetricTimer:
        self.num_calls += 1
        self.start = time.time()
        return self

    def __exit__(self, cls, error: str, trace_back) -> bool:
        self.end = time.time()
        if self.value:
            self.value += self.end - self.start
        else:
            self.value = self.end - self.start

        if self.file:
            print(error, file=self.file)
        if isinstance(error, Exception):
            return True
        return True

    def get_name(self) -> str:
        return super().get_name()

    def get_value(self) -> Number:
        return self.value

    def add(self, value=None):
        if not value:
            raise ValueError("please enter some value")
        self.num_calls += 1
        if self.value:
            self.value += value
        else:
            self.value = value

    def clear(self):
        super().clear()
        self.num_calls = 0


class Stats:
    metrics_dict: dict = dict()

    @staticmethod
    def timer(name: str, file: FileObj = None) -> MetricTimer:
        met_timer = MetricTimer(name, file)
        met_name = met_timer.get_name()
        if met_name not in Stats.metrics_dict.keys():
            Stats.metrics_dict[met_name] = met_timer
        return Stats.metrics_dict[met_name]

    @staticmethod
    def avg(name: str) -> MetricAvg:
        met_avg = MetricAvg(name)
        met_name = met_avg.get_name()
        if met_name not in Stats.metrics_dict.keys():
            Stats.metrics_dict[met_name] = met_avg
        return Stats.metrics_dict[met_name]

    @staticmethod
    def count(name: str) -> MetricCount:
        met_count = MetricCount(name)
        met_name = met_count.get_name()
        if met_name not in Stats.metrics_dict.keys():
            Stats.metrics_dict[met_name] = met_count
        return Stats.metrics_dict[met_name]

    @staticmethod
    def collect() -> dict:
        res_dict: dict = dict()
        for key, val in Stats.metrics_dict.items():
            if val.num_calls > 0:
                res_dict[key] = val.get_value()
            val.clear()
        Stats.metrics_dict = dict()
        return res_dict
