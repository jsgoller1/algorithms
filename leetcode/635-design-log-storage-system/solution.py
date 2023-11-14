def get_granularity_level(granularity):
    granularities = ["Year", "Month", "Day", "Hour", "Minute", "Second"]
    if granularity in granularities:
        return granularities.index(granularity)
    return -1


class Log:
    def __init__(self, id, timestamp):
        self.id = id
        ts_fields = timestamp.split(":")
        self.year = ts_fields[0]
        self.month = ts_fields[1]
        self.day = ts_fields[2]
        self.hour = ts_fields[3]
        self.minute = ts_fields[4]
        self.second = ts_fields[5]

    def before(self, other, granularity):
        granularity_level = get_granularity_level(granularity)
        comparisons = [(self.year, other.year), (self.month, other.month),
                       (self.day, other.day), (self.hour, other.hour),
                       (self.minute, other.minute), (self.second, other.second)]
        for level, attr_pair in enumerate(comparisons):
            ours, theirs = attr_pair
            if theirs < ours:
                return False
            if ours < theirs:
                return True
            if granularity_level <= level:
                return True
        return True

    def __repr__(self):
        return f"Log(id:{self.id}, ts:{self.year}:{self.month}:{self.day}:{self.hour}:{self.minute}:{self.second})"


class LogSystem:

    def __init__(self):
        self.storage = {}

    def put(self, log_id: int, timestamp: str) -> None:
        self.storage[log_id] = Log(log_id, timestamp)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start_log = Log(-1, start)
        end_log = Log(-1, end)
        return [log.id for log in self.storage.values() if (start_log.before(log, granularity) and log.before(end_log, granularity))]
