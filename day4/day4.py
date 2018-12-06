from collections import defaultdict
import datetime
from pathlib import Path

class Guard:

    def __init__(self, id):
        self.id = id
        self.shifts = []

    def get_sleep_time(self):
        total = 0
        for s in self.shifts:
            total += s.get_total_asleep()
        return total

    def get_most_asleep_minute(self):
        minutes = defaultdict(int)
        for s in self.shifts:
            ma = s.get_minutes_asleep()
            for m in ma:
                minutes[m] += 1
        if len(minutes) == 0:
            return (0, 0)
        return max(minutes.items(), key=lambda kv: kv[1])


class Shift:

    def __init__(self, date):
        self.date = date

        if date.hour > 0:
            self.date += datetime.timedelta(days=1)
            self.date.replace(hour=0)

        self.awake = []
        self.asleep = []

    def get_total_awake(self):
        return 60 - self.get_total_asleep()

    def get_minutes_asleep(self):
        minutes = []
        for i in range(len(self.asleep)):
            period_start = self.asleep[i]
            if len(self.awake) > i:
                period_end = self.awake[i]
            else:
                period_end = 60
            minutes += range(period_start, period_end)
        return minutes

    def get_total_asleep(self):
        return len(self.get_minutes_asleep())

def get_time(line):
    split = line.split(']')
    date = split[0][1:].split(' ')
    major = date[0].split('-')
    minor = date[1].split(':')
    return datetime.datetime(int(major[0]), int(major[1]), int(major[2]), int(minor[0]), int(minor[1]))

def part1(input_str):
    guards = []
    curr_guard = None
    input_strs = input_str.splitlines()
    input_strs.sort()
    for line in input_strs:
        found = False
        if "begins" in line:
            split = line.split(' ')
            id = int(split[3][1:])
            for g in guards:
                if g.id == id:
                    curr_guard = g
                    found = True
                    break

            time = get_time(line)
            s = Shift(time)

            if found is False:
                curr_guard = Guard(id)
                curr_guard.shifts.append(s)
                guards.append(curr_guard)
            else:
                curr_guard.shifts.append(s)
        elif "falls" in line:
            t = get_time(line)
            curr_guard.shifts[-1].asleep.append(t.minute)
        elif "wakes" in line:
            t = get_time(line)
            curr_guard.shifts[-1].awake.append(t.minute)

    max = None
    for g in guards:
        #print(str(g.id) + ": " + str(g.get_sleep_time()))
        if max is None or g.get_sleep_time() > max.get_sleep_time():
            max = g

    print(max.id * max.get_most_asleep_minute()[0])

def part2(input_str):
    guards = []
    curr_guard = None
    input_strs = input_str.splitlines()
    input_strs.sort()
    for line in input_strs:
        found = False
        if "begins" in line:
            split = line.split(' ')
            id = int(split[3][1:])
            for g in guards:
                if g.id == id:
                    curr_guard = g
                    found = True
                    break

            time = get_time(line)
            s = Shift(time)

            if found is False:
                curr_guard = Guard(id)
                curr_guard.shifts.append(s)
                guards.append(curr_guard)
            else:
                curr_guard.shifts.append(s)
        elif "falls" in line:
            t = get_time(line)
            curr_guard.shifts[-1].asleep.append(t.minute)
        elif "wakes" in line:
            t = get_time(line)
            curr_guard.shifts[-1].awake.append(t.minute)

    max = None
    for g in guards:
        #print(str(g.id) + ": " + str(g.get_sleep_time()))
        mam = g.get_most_asleep_minute()
        if max is None or mam[1] > max.get_most_asleep_minute()[1]:
            max = g

    print(max.id * max.get_most_asleep_minute()[0])

def main():
    input_str = Path("input").read_text()
    part1(input_str)
    part2(input_str)

if __name__ == "__main__":
    main()