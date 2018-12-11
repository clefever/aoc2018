from collections import defaultdict
from pathlib import Path

class Marble:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = self if next is None else next
        self.prev = self if prev is None else prev

    def insert(self, value):
        m = Marble(value, self.next.next, self.next)
        self.next.next = m
        self.next.next.next.prev = m
        return m

def game_high_score(player_count, last_marble_worth):
    scores = defaultdict(int)
    marble_count = 1
    curr_player = 1
    marble = Marble(0)

    for i in range(1, last_marble_worth):
        if i % 23 == 0:
            for _ in range(8):
                marble = marble.prev
            scores[curr_player] += i + marble.next.value
            temp = marble.next.next
            marble.next = temp
            marble_count -= 1
            marble = temp
        else:
            marble = marble.insert(i)
            marble_count += 1
        curr_player += 1
        if curr_player % (player_count + 1) == 0:
            curr_player = 1

    high_score = max(scores.items(), key=lambda kv: kv[1])
    return high_score[1]

def get_params(input_str):
    split = input_str.split(' ')
    return int(split[0]), int(split[6])

def main():
    input_str = Path("input").read_text()
    player_count, last_marble_worth = get_params(input_str)
    print(game_high_score(player_count, last_marble_worth))
    print(game_high_score(player_count, last_marble_worth * 100))

if __name__ == "__main__":
    main()
