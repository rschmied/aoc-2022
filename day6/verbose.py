from typing import List, Tuple
import unittest


def find_msg(msg: str, mlen: int) -> int:
    idx = 0
    for idx in range(len(msg) - mlen + 1):
        if len(set(msg[idx : idx + mlen])) == mlen:
            break
    return idx + mlen


part1_testdata: List[Tuple[str, int]] = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
    # 123456789
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
]

part2_testdata: List[Tuple[str, int]] = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
]


class TestStringMethods(unittest.TestCase):
    def test_part1(self):
        for msg, expected in part1_testdata:
            self.assertEqual(expected, find_msg(msg, 4))

    def test_part2(self):
        for msg, expected in part2_testdata:
            self.assertEqual(expected, find_msg(msg, 14))

    def test_corner1(self):
        self.assertEqual(4, find_msg("", 4))

    def test_corner2(self):
        self.assertEqual(15, find_msg("aaaaaaaaaaaabcd", 4))
        #                              123456789012345

    def test_corner3(self):
        self.assertEqual(15, find_msg("0aaa0aaaa0aaaa0", 4))
        #                              123456789012345


if __name__ == "__main__":
    unittest.main(exit=False)

    with open("input", "r") as fh:
        data = fh.readline().strip()
    print("Part 1:", find_msg(data, 4))
    print("Part 2:", find_msg(data, 14))
