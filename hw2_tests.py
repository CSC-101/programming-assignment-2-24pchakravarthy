import data
import hw2
import unittest




# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        p1 = data.Point(3, 3)
        p2 = data.Point(7, 7)
        r1 = hw2.create_rectangle(p1, p2)
        self.assertEqual(r1, data.Rectangle(data.Point(3,7), data.Point(7,3)))

    def test_create_rectangle2(self):
        p1 = data.Point(6, 6)
        p2 = data.Point(6, 13)
        r1 = hw2.create_rectangle(p1, p2)
        self.assertEqual(r1, data.Rectangle(data.Point(6, 13), data.Point(6, 6)))

    # Part 2
    def test_shorter_duration_than1(self):
        d1 = data.Duration(2, 45)
        d2 = data.Duration(3, 32)
        r1 = hw2.shorter_duration_than(d1, d2)
        self.assertEqual(r1, True)

    def test_shorter_duration_than2(self):
        d1 = data.Duration(2, 10)
        d2 = data.Duration(2, 10)
        r1 = hw2.shorter_duration_than(d1, d2)
        self.assertEqual(r1, False)


    # Part 3
    def test_song_shorter_than1(self):
        s1 = [data.Song("Artist 1", "Title 1", data.Duration(1, 40)),
              data.Song("Artist 2", "Title 2", data.Duration(2, 30)),
              data.Song("Artist 3", "Title 3", data.Duration(3, 50))]
        highestduration = data.Duration(4, 30)
        r1 = hw2.song_shorter_than(s1, highestduration)
        self.assertEqual(r1, [data.Song('Artist 1', 'Title 1', data.Duration(1, 40)), data.Song('Artist 2', 'Title 2', data.Duration(2, 30)), data.Song('Artist 3', 'Title 3', data.Duration(3, 50))])

    def test_song_shorter_than2(self):
        s2 = [data.Song("Artist 1", "Title 1", data.Duration(1, 40)),
              data.Song("Artist 2", "Title 2", data.Duration(1, 20)),
              data.Song("Artist 3", "Title 3", data.Duration(1, 50))]
        highestduration2 = data.Duration(1, 20)
        r2 = hw2.song_shorter_than(s2, highestduration2)
        self.assertEqual(r2, [])


    # Part 4
    def test_running_time1(self):
        s1 = [data.Song("Artist A", "Title 1", data.Duration(1, 40)),
              data.Song("Artist B", "Title 2", data.Duration(2, 30)),
              data.Song("Artist C", "Title 3", data.Duration(3, 50))]
        p1 = [1, 2, 0, 1, 2]
        r1 = hw2.running_time(s1, p1)
        self.assertEqual(r1, data.Duration(8, 0))

    def test_running_time2(self):
        s2 = [data.Song("First Artist", "1st Title", data.Duration(3, 30)),
              data.Song("Second Artist", "2nd Title", data.Duration(5, 15)),
              data.Song("Third Artist", "Third Title", data.Duration(4, 20))]
        p2 = [-1, -2, 0, 1, -1, 1, 2]
        r2 = hw2.running_time(s2, p2)
        self.assertEqual(r2, data.Duration(13, 5))

    # Part 5
    def test_validate_route1(self):
        c1 = [["los angeles", "laguna beach"], ["laguna beach", "redondo beach"], ["irvine", "palm springs"]]
        r1 = ["los angeles", "laguna beach", "redondo beach", "laguna beach"]
        v1 = hw2.validate_route(c1, r1)
        self.assertEqual(v1, True)

    def test_validate_route2(self):
        c2 = [["irvine", "palm springs"], ["thousand oaks, catalina"], ["catalina", "irvine"]]
        r2 = ["irvine", "palm springs", "catalina", "thousand oaks", "catalina"]
        v2 = hw2.validate_route(c2, r2)
        self.assertEqual(v2, False)


    # Part 6
    def test_longest_repetition1(self):
        n1 = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 5, 7, 8, 5, 1, 1, 2, 4, 3]
        r1 = hw2.longest_repetition(n1)
        self.assertEqual(r1, 8)
    def test_longest_repetition2(self):
        n1 = []
        r1 = hw2.longest_repetition(n1)
        self.assertEqual(r1, None)
    def test_longest_repetition3(self):
        n1 = [7, 8, 9, 10, 11]
        r1 = hw2.longest_repetition(n1)
        self.assertEqual(r1, 0)




if __name__ == '__main__':
    unittest.main()
