import unittest
from termforge import wrap
class Tests(unittest.TestCase):
 def test_wrap(self): self.assertEqual(wrap('one two three',7),['one two','three'])
if __name__=='__main__': unittest.main()
