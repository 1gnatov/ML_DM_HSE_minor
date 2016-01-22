class Field:
    def __init__(self, field_file, num_ships=10):
        self.field = self._fill(field_file)
        self.num_ships = num_ships

    def _fill(self, field_file):
        field = []
        with open(field_file) as input_file:
            for line in input_file:
                field.append([i for i in line.strip().split(',')])
        return field

    def _neighborhood(self, x, y):
        return [(i,j) for i in [x - 1, x, x + 1]
                     for j in [y - 1, y, y + 1]
                if i >= 0 and i < 10 and j >= 0 and j < 10
                and not (i == x and j == y)]

    def fire(self, x, y):
        """
        1 - miss
        2 - wounded
        3 - already wounded
        4 - killed
        5 - no more ships
        """

        if self.field[x][y] == '.':
            return 1
        elif self.field[x][y] == '#':
            self.field[x][y] = 'x'
            for (neighb_x, neighb_y) in self._neighborhood(x, y):
                if self.field[neighb_x][neighb_y] == '#':
                    return 2
            # killed a ship
            self.num_ships -= 1
            if self.num_ships == 0:
                return 5
            return 4
        elif self.field[x][y] == 'x':
            return 3


    def __str__(self):
        '''
        prints the field
        '''
        s = '  abcdefghij\n'
        for line_id, line in enumerate(self.field):
            line_string = str(line_id) + '|'
            for character in line:
                line_string += character
            s += line_string + '\n'
        return s


class Player:
    def __init__(self, field, opponent_field):
        self.own_field = field
        self.opponent_field = opponent_field
        self.winned = False
    def fire(self, x, y):
        status = self.opponent_field.fire(x, y)
        if status == 5:
            self.winned = True
        return status


class Game:
    def __init__(self, field1_path, field2_path, reveal_comp_field=False):
        player_field = Field(field1_path)
        comp_field = Field(field2_path)
        self.player = Player(field=player_field,
                        opponent_field=comp_field)
        self.comp = Player(field=comp_field,
                        opponent_field=player_field)
        self.fire_status = {1: 'Missed.',
                            2: 'Wounded',
                            3: 'Already wounded.',
                            4: 'Killed.',
                            5: 'Won.'}
        self.field_horiz_axis = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                                 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                                 'i': 8, 'j': 9}
        self.field_horiz_axis_inverse = {0: 'a', 1: 'b', 2: 'c', 3: 'd',
                                        4: 'e', 5: 'f', 6: 'g', 7: 'h',
                                        8: 'i', 9:'j'}
        self.reveal_comp_field = reveal_comp_field

    # TODO print opponent field without revealing his ships
    def player_step(self, reveal_opponent_field=False):
        print('Your hit: ')
        inserted = input() # in a form 'a4' or 'c8'
        x, y = int(inserted[1]), self.field_horiz_axis[inserted[0]]
        status = self.player.fire(x, y)
        print(self.fire_status[status])
        if reveal_opponent_field:
            print(self.player.opponent_field)

    # TODO make computer 'smarter'
    def computer_step(self):
        from random import choice
        x, y = choice(range(10)), choice(range(10))
        print('Computer hits {0}{1}'.format(self.field_horiz_axis_inverse[y], x))
        status = self.comp.fire(x, y)
        print(self.fire_status[status])
        print(self.comp.opponent_field)

    def start(self):
        while not self.player.winned and not self.comp.winned:
            self.player_step(reveal_opponent_field=self.reveal_comp_field)
            self.computer_step()
        if self.player.winned:
            print('You win!')
        else:
            print('You lose!')

# TODO settings from param file
Game('../input/field1.txt', '../input/field2.txt', reveal_comp_field=True).start()






