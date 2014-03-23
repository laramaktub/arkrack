import unittest
from arkrack.crackers import zip_cracker
import os

class TestZipCracker(unittest.TestCase):

  def setUp(self):
    test_zip = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'testdata', 'testzip.zip')
    self._cracker = zip_cracker.ZipCracker(test_zip)

  def test_can_crack_with_right_password(self):
    self.assertTrue(self._cracker.can_crack('password'))

  def test_cannot_crack_with_wrong_password(self):
    self.assertFalse(self._cracker.can_crack('this is wrong'))


if __name__ == "__main__":
  logging.basicConfig(
      level=logging.ERROR,
      format='[%(levelname)s] (%(threadName)-10s) %(message)s',
  )
  unittest.main()