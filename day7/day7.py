from pathlib import Path

class Step:

    def __init__(self, name):
        self.name = name
        self.prev = []
        self.next = []
        self.time = 0
        
    def available(self):
        if not self.prev:
            return True
        for step in self.prev:
            if not step.available():
                return False
        return True

    def compl_time(self):
        return ord(self.name) - 4 # -64 for example

    def work_sec(self):
        self.time += 1

    def is_complete(self):
        return self.time >= self.compl_time()

def part1(input_str):
    steps = {}
    input_str = input_str.splitlines()
    for i in input_str:
        s = i.split(' ')
        s1, s2 = None, None

        if s[1] in steps:
            s1 = steps[s[1]]
        else:
            s1 = Step(s[1])

        if s[7] in steps:
            s2 = steps[s[7]]
        else:
            s2 = Step(s[7])
        
        s1.next.append(s2)
        s2.prev.append(s1)

        steps[s[1]] = s1
        steps[s[7]] = s2

    heads = []
    for s in steps.items():
        if not s[1].prev:
           heads.append(s[1])

    avail_steps = heads
    avail_steps.sort(key=lambda x: x.name)
    compl_steps = []
    while avail_steps:
        s = avail_steps.pop(0)
        all_prev_processed = True
        for st in s.prev:
            if st not in compl_steps:
                all_prev_processed = False
        if s in compl_steps or s in avail_steps:
            continue
        elif s.available and all_prev_processed:
            avail_steps.extend(s.next)
            avail_steps.sort(key=lambda x: x.name)
            compl_steps.append(s)
        else:
            avail_steps.append(s)

    return "".join([x.name for x in compl_steps])

def part2(input_str):
    steps = {}
    input_str = input_str.splitlines()
    for i in input_str:
        s = i.split(' ')
        s1, s2 = None, None

        if s[1] in steps:
            s1 = steps[s[1]]
        else:
            s1 = Step(s[1])

        if s[7] in steps:
            s2 = steps[s[7]]
        else:
            s2 = Step(s[7])
        
        s1.next.append(s2)
        s2.prev.append(s1)

        steps[s[1]] = s1
        steps[s[7]] = s2

    heads = []
    for s in steps.items():
        if not s[1].prev:
           heads.append(s[1])

    avail_steps = heads
    avail_steps.sort(key=lambda x: x.name)
    sch_steps = []
    backlog = []
    compl_steps = []
    avail_workers = 5 # 2 for example
    curr_time = 0
    while True:
        back_copy = backlog[:]
        for b in back_copy:
            for p in b.prev:
                if p not in compl_steps:
                    all_prev_processed = False
            if all_prev_processed:
                if b not in avail_steps:
                    avail_steps.append(b)
                backlog.remove(b)
        pop_num = min(len(avail_steps), avail_workers)
        for i in range(pop_num):
            avail_workers -= 1
            sch_steps.append(avail_steps.pop(0))
        #print([x.name for x in sch_steps])
        for s in sch_steps:
            s.work_sec()
        curr_time += 1
        for s in sch_steps:
            if s.is_complete():
                sch_steps.remove(s)
                if s in backlog:
                    backlog.remove(s)
                compl_steps.append(s)
                for n in s.next:
                    all_prev_processed = True
                    for p in n.prev:
                        if p not in compl_steps:
                            all_prev_processed = False
                    if all_prev_processed:
                        if n not in avail_steps:
                            avail_steps.append(n)
                    else:
                        if n not in backlog:
                            backlog.append(n)
                avail_workers += 1
        avail_steps.sort(key=lambda x: x.name)
        if len(compl_steps) >= len(steps):
            break

    return curr_time

def main():
    input_str = Path("input").read_text()
    print(part1(input_str))
    print(part2(input_str))

if __name__ == "__main__":
    main()
