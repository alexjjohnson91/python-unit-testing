import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution()

    def test_solution(self):
        # Arrange
        expected = 4

        # Act
        actual = self.solution.add(2, 2)

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
