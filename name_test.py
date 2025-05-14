import unittest 
from name import get_full_name 
class Nametest(unittest.TestCase) :
    def test_toliq_ism(self):
        name=get_full_name('mahmud', 'sadikov')