#!/usr/bin/python

import unittest
import levenshtein

class TestLevenshtein(unittest.TestCase):
    
    lev_strings_to_test = (
        ('asd', 'dsa', 2,),
        ('asd', 'sda', 2,),
        ('asd', 'fgh', 3,),
        ('kentucky', 'abcdefg', 8,),
        ('same string', 'same string', 0,),
    )
    
    dam_lev_strings_to_test = (
        ('abcde', 'abdce', 1,),
        ('abcde', 'abdgce', 2,),
        ('as', 'sa', 1,),
        ('same string', 'same string', 0,),
        ('askgdf913636ajhga', 'ags366391jwd', 12,),
    )
    
    @unittest.skip
    def test_levenshtein_distance(self):
        for s1, s2, d in self.lev_strings_to_test:
            self.assertEqual(levenshtein.levenshtein_distance(s1, s2), d)
    
    def test_damerau_levenshtein(self):
        for s1, s2, d in self.dam_lev_strings_to_test:
            self.assertEqual(levenshtein.damerau_levenshtein(s1, s2), d)

if __name__ == '__main__':
    unittest.main()
