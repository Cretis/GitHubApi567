import unittest
from HW04a import get_git_hub


class TestHw04(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(get_git_hub('Cretis'), ['Repo:GitHubApi567 Number of commits: 3',
                                                 'Repo:SSW567 Number of commits: 2',
                                                 'Repo:SSW810 Number of commits: 4',
                                                 'Repo:Triangle567 Number of commits: 17', ])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
