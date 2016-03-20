import unittest

from game_of_life import *

class test_game_of_life(unittest.TestCase):

    def test_next_generation_of_empty_pattern_is_empty(self):
        self.assertEquals(next([]),[])

    def test_a_single_cell_dies(self):
        self.assertEquals(next([(0,0)]), [])

    def test_can_count_live_neighbours_of_a_cell(self):
        pattern = [
            (-1, -1),       (1, -1),
                    (0, 0),
            (-1, 1),        (1, 1)
            ]
        self.assertEquals(number_of_living_neighbours(pattern, (0, 0)), 4)