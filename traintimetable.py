import datetime

name = 'traintimetable'

class Train:
    def __init__(self, earliest_departure_time):
        self.earliest_departure_time = earliest_departure_time

class Station:
    def __init__(self, turnaround_time, scheduled_out, scheduled_in):
        self.trains = []
        self.turnaround_time = turnaround_time
        self.scheduled_out = scheduled_out
        self.scheduled_in = scheduled_in

        for scheduleEntry in scheduled_in:
            self.add_train(scheduleEntry.end_time + turnaround_time)

        self.requires_trains = 0

        for out in scheduled_out:
            at = self.can_depart_at(out.start_time)
            if not at:
                self.requires_trains += 1
            else:
                self.remove_train(at)

    def can_depart_at(self, time):
        available_trains = [train for train in self.trains if train.earliest_departure_time <= time]
        
        if not available_trains:
            return None

        return available_trains[0]

    def add_train(self, time):
        train = Train(time)
        self.trains.append(train)

    def remove_train(self, train):
        self.trains.remove(train)

class ScheduleEntry:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

        self.start_hours = self.start_time // 60
        self.start_minutes = self.start_time % 60
        self.end_hours = self.end_time // 60
        self.end_minutes = self.end_time % 60

    def __eq__(self, other):
        return self.start_time == other.start_time and self.end_time == other.end_time

    def __lt__(self, other):
        return self.start_time < other.start_time or (self.start_time == other.start_time and self.end_time < other.end_time)

    def __gt__(self, other):
        return self.start_time > other.start_time or (self.start_time == other.start_time and self.end_time > other.end_time)      

    def __repr__(self):
        return f"Start: {self.start_hours:02d}:{self.start_minutes:02d}, End: {self.end_hours:02d}:{self.end_minutes:02d}"

def num_trains(turnaround_time, departing_a, departing_b):
    departing_a = sorted(departing_a)
    departing_b = sorted(departing_b)

    station_a = Station(turnaround_time, departing_a, departing_b)
    station_b = Station(turnaround_time, departing_b, departing_a)
    

    for scheduleEntry in departing_a:
        pass

    return (station_a.requires_trains, station_b.requires_trains)

def parse_time(line):
    start, end = line.strip().split(' ')
    start_time = datetime.datetime.strptime(start, '%H:%M').time()
    end_time = datetime.datetime.strptime(end, '%H:%M').time()
    
    scheduleEntry = ScheduleEntry(start_time.hour * 60 + start_time.minute, end_time.hour * 60 + end_time.minute)
    return scheduleEntry

def parse_test(f):
    turnaround_time = int(f.readline())
    (n_a, n_b) = [int(x) for x in f.readline().split(' ')]

    a = []
    b = []

    for i in range(n_a):
        a.append(parse_time(f.readline()))

    for i in range(n_b):
        b.append(parse_time(f.readline()))

    return (turnaround_time, a, b)

def parse_tests(size):
    tests = []

    with open(f'{name}.{size}.in') as f:
        n = int(f.readline())

        for i in range(n):
            test = parse_test(f)
            tests.append(test)

    return tests

def write_results(results, size):
    with open(f'{name}.{size}.out', 'w') as f:
        for i, result in enumerate(results):
            f.write(f'Case #{i+1}: {result[0]} {result[1]}\n')

def run_test(size='tiny'):
    results = []

    for test in parse_tests(size):
        result = num_trains(*test)
        results.append(result)

    write_results(results, size)

run_test('tiny')
run_test('small')
run_test('large')