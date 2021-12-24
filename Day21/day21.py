from player import Player
from collections import deque, defaultdict
from math import prod
import copy

player_1_initial_position = 6
player_2_initial_position = 1
winning_criteria = 21
dice = range(1, 101)
dirac_dice = range(3, 10)
dirac_dice_map = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

player_1 = Player(player_1_initial_position)
player_2 = Player(player_2_initial_position)

def part1(dice, player_1, player_2, win, rolled_count):
    while not win:
        read_pointer = (3 * rolled_count) % 100

        number = (dice[read_pointer] + 1) * 3

        if rolled_count % 2 == 0:
            player = player_1
        else:
            player = player_2

        player.move(number)

        if player.total_score >= 1000:
            win = True

        rolled_count += 1


    print(min(player_1.total_score, player_2.total_score) * rolled_count * 3)

def player_simulation(player: Player):
    player_rec = defaultdict(lambda: 0)
    player_rec_lose = defaultdict(lambda: 0)
    player_queue = deque()
    player_queue.append(player)

    while player_queue:
        player = player_queue.popleft()

        if player.total_score >= winning_criteria:
            player_rec[player.rolled_count] += player.total_combination

        else:
            player_rec_lose[player.rolled_count] += player.total_combination
            for number in dirac_dice:
                player_copy = copy.deepcopy(player)
                player_copy.move(number)
                player_queue.append(player_copy)

    return (player_rec, player_rec_lose)


def part2():
    (player_1_rec, player_1_rec_lose) = player_simulation(player_1)
    (player_2_rec, player_2_rec_lose) = player_simulation(player_2)

    player_1_winning = 0
    player_2_winning = 0

    for (player_1_rolled_count, player_1_winning_combo) in player_1_rec.items():
        player_2_rolled_count = player_1_rolled_count - 3
        player_1_winning += player_1_winning_combo * player_2_rec_lose[player_2_rolled_count]
    
    for (player_2_rolled_count, player_2_winning_combo) in player_2_rec.items():
        player_1_rolled_count = player_2_rolled_count
        player_2_winning += player_2_winning_combo * player_1_rec_lose[player_1_rolled_count]
    
    print(player_1_winning)
    print(player_2_winning)


part2()


#win = False
#rolled_count = 0
#part1(dice, player_1, player_2, win, rolled_count)
