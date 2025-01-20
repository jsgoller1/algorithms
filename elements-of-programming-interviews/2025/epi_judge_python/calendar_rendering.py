import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

from collections import defaultdict

def find_max_simultaneous_events(A: List[Event]) -> int:
    deltas = defaultdict(int)
    for start, finish in A: 
        deltas[start] += 1
        deltas[finish+1] -= 1 

    current_events = most = 0
    for time in range(max(deltas.keys())):
        current_events += deltas[time]
        most = max(most, current_events)    
    return most 


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
