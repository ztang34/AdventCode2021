class Player:

    dirac_dice_map = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}
    def __init__(self, starting_position) -> None:
        self.position = starting_position
        self.total_score = 0
        self.rolled_count = 0
        self.total_combination = 1
        self.history_moves = []
    
    def move(self, number):
        self.position = (self.position + number % 10) % 10
        if self.position == 0:
            self.position = 10
        self.total_score += self.position
        self.rolled_count += 3
        self.total_combination *= self.dirac_dice_map[number]
        self.history_moves.append(number)