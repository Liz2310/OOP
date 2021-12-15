import datetime
import time

"""The fact that functions are top-level objects is most often 
used to pass them around to be executed at a later date, for 
example, when a certain condition has been satisfied. Let's 
build an event-driven timer that does just this"""

class TimedEvent:
    """The TimedEvent class is not really meant to be accessed
    by other classes; all it does is store endtime and callback.
    We could even use a tuple or namedtuple here, but as it is
    convenient to give the object a behavior that tells us
    whether or not the event is ready to run, we use a class instead."""

    def __init__(self, endtime, callback): #callback is a message
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now()


class Timer:
    """The Timer class simply stores a list of upcoming events.
    It has a call_after method to add a new event. This method
    accepts a delay parameter representing the number of seconds
    to wait before executing the callback, and the callback function
    itself: a function to be executed at the correct time. This
    callback function should accept one argument."""

    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        """The run method is very simple; it uses a generator expression
        to filter out any events whose time has come, and executes them in order. """
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)


def format_time(message, *args):
    """It uses the format string syntax to add the current time to the message"""

    now = datetime.datetime.now()
    print(f"{now:%I:%M:%S}: {message}")


def one(timer):
    format_time("Called One")


def two(timer):
    format_time("Called Two")


def three(timer):
    format_time("Called Three")


class Repeater:
    def __init__(self):
        self.count = 0

    def repeater(self, timer):
        format_time(f"repeat {self.count}")
        self.count += 1
        timer.call_after(5, self.repeater)

timer = Timer()
timer.call_after(1, one)
timer.call_after(2, one)
timer.call_after(2, two)
timer.call_after(4, two)
timer.call_after(3, three)
timer.call_after(6, three)
repeater = Repeater()
timer.call_after(5, repeater.repeater)
format_time("Starting")
timer.run()