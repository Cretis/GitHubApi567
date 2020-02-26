import unittest
from unittest.mock import patch, Mock

from HW04a import get_git_hub


class TestHw04(unittest.TestCase):
    def testCase1(self):
        with patch('HW04a.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [
                {'name': '1'},
                {'name': '2'}
            ]
            mocked = get_git_hub('Cretis')
            self.assertEqual(mocked, ['Repo:1 Number of commits: 2',
                                      'Repo:2 Number of commits: 2',
                                      ])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
