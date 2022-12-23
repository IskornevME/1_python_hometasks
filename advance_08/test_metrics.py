import time
import unittest
from io import StringIO

from metrics import Stats


def calc():
    time.sleep(0.1)
    return 3.0


class TestMetrics(unittest.TestCase):
    def test_as_in_task(self):
        with Stats.timer("calc"):
            res = calc()
        expected = {"calc.timer": 0.10}
        get_answer = Stats.collect()
        self.assertAlmostEqual(
            expected['calc.timer'],
            get_answer['calc.timer'],
            places=1
        )

        Stats.count("calc").add()
        Stats.avg("calc").add(res)
        t_1 = 0
        res = 7
        t_2 = 0.3
        Stats.timer("calc").add(t_2 - t_1)
        Stats.count("calc").add()
        Stats.avg("calc").add(res)
        Stats.count("http_get_data").add()
        Stats.avg("http_get_data").add(0.7)
        Stats.count("no_used")
        expected = {
                    "calc.count": 2,
                    "calc.avg": 5.0,
                    "calc.timer": 0.3,
                    "http_get_data.count": 1,
                    "http_get_data.avg": 0.7,
                }
        get_answer = Stats.collect()
        self.assertDictEqual(expected, get_answer)
        self.assertDictEqual({}, Stats.collect())


    def test_timer(self):
        self.assertFalse(Stats.timer("calc").get_value())
        self.assertEqual(Stats.timer("calc").get_name(), "calc.timer")
        self.assertDictEqual({}, Stats.collect())
        Stats.timer("calc").add(1.0)
        self.assertEqual(Stats.timer("calc").get_value(), 1.0)
        with Stats.timer("calc"):
            time.sleep(0.5)
        with Stats.timer("calc"):
            time.sleep(0.2)
        self.assertAlmostEqual(Stats.timer("calc").get_value(), 1.71, places=1)
        Stats.collect()

        Stats.timer("calc").add(0.75)
        Stats.timer("calc").add(2)
        Stats.timer("calc_2").add(3)
        expected = {"calc.timer": 2.75, "calc_2.timer": 3}
        self.assertDictEqual(expected, Stats.collect())

        with Stats.timer("calc"):
            time.sleep(0.2)
        Stats.timer("calc").clear()
        self.assertFalse(Stats.timer("calc").get_value())


    def test_timer_no_args(self):
        with self.assertRaises(ValueError) as err:
            Stats.timer("func").add()
        expected = "please enter some value"
        self.assertEqual(str(err.exception), expected)


    def test_avg(self):
        self.assertFalse(Stats.avg("calc").get_value())
        self.assertEqual(Stats.avg("func").get_name(), "func.avg")
        self.assertDictEqual({}, Stats.collect())
        Stats.avg("calc").add(1)
        self.assertEqual(Stats.avg("calc").get_value(), 1.0)
        Stats.avg("calc").add(2)
        self.assertEqual(Stats.avg("calc").get_value(), 1.5)
        Stats.avg("calc").add(3)
        self.assertEqual(Stats.avg("calc").get_value(), 2.0)
        Stats.avg("calc").add(5)
        self.assertEqual(Stats.avg("calc").get_value(), 2.75)
        self.assertDictEqual({"calc.avg": 2.75}, Stats.collect())

        Stats.avg("calc").add(100)
        Stats.avg("mult").add(5)
        Stats.avg("mult").add(20)
        self.assertDictEqual(
            {"calc.avg": 100, "mult.avg": 12.5},
            Stats.collect()
        )
        self.assertDictEqual({}, Stats.collect())

        Stats.avg("mult").add(11)
        Stats.avg("mult").clear()
        self.assertEqual(Stats.avg("calc").get_value(), None)


    def test_avg_no_args(self):
        with self.assertRaises(ValueError) as err:
            Stats.avg("func").add()
        expected = "please enter some value"
        self.assertEqual(str(err.exception), expected)


    def test_count(self):
        self.assertFalse(Stats.count("calc").get_value())
        self.assertEqual(Stats.count("func").get_name(), "func.count")
        self.assertDictEqual({}, Stats.collect())
        Stats.count("func").add()
        self.assertEqual(Stats.count("func").get_value(), 1)
        Stats.count("func").add()
        self.assertEqual(Stats.count("func").get_value(), 2)
        Stats.count("func").add()
        Stats.count("func").add()
        self.assertEqual(Stats.count("func").get_value(), 4)
        self.assertDictEqual({"func.count": 4}, Stats.collect())

        Stats.count("calc").add()
        Stats.count("new_func").add()
        Stats.count("new_func").add()
        self.assertDictEqual(
            {"calc.count": 1, "new_func.count": 2},
            Stats.collect()
        )
        self.assertDictEqual({}, Stats.collect())

        Stats.count("mult").add()
        Stats.count("mult").clear()
        self.assertEqual(Stats.count("calc").get_value(), None)


    def test_count_args(self):
        with self.assertRaises(ValueError) as err:
            Stats.count("func").add(23)
        expected = "No need to specify args"
        self.assertEqual(str(err.exception), expected)


    def test_timer_exception(self):
        io_str = StringIO()
        count = 0
        with Stats.timer("calc", io_str):
            raise Exception("something went wrong")
        count += 1
        self.assertEqual(count, 1)


    def test_all(self):
        Stats.timer("calc").add(0.3)
        self.assertEqual(Stats.timer("calc").get_value(), 0.3)
        self.assertEqual(Stats.timer("calc").get_name(), "calc.timer")
        Stats.timer("calc").add(1)
        self.assertEqual(Stats.timer("calc").get_value(), 1.3)
        Stats.avg("func").add(3.5)
        self.assertEqual(Stats.avg("func").get_value(), 3.5)
        Stats.avg("func").add(4)
        self.assertEqual(Stats.avg("func").get_value(), 3.75)
        Stats.count("add").add()
        self.assertEqual(Stats.count("add").get_value(), 1)
        Stats.count("add").add()
        Stats.count("add").add()
        self.assertEqual(Stats.count("add").get_value(), 3)
        self.assertEqual(Stats.avg("func").get_value(), 3.75)
        Stats.timer("add").add(0.2)
        expected = {
            "calc.timer": 1.3,
            "func.avg": 3.75,
            "add.count": 3,
            "add.timer": 0.2
        }
        self.assertDictEqual(expected, Stats.collect())
        self.assertFalse(Stats.timer("calc").get_value())
        self.assertFalse(Stats.avg("func").get_value())
        self.assertFalse(Stats.count("add").get_value())
        self.assertFalse(Stats.timer("add").get_value())
        self.assertDictEqual({}, Stats.collect())

        Stats.timer("f_1").add(10)
        Stats.count("function").add()
        Stats.timer("f_1").add(15)
        Stats.avg("div").add(35)
        Stats.avg("div").add(13)
        Stats.count("function").add()
        Stats.timer("f_2").add(1.2)
        Stats.count("function").add()
        res = calc()
        Stats.avg("div").add(res)
        Stats.count("gen").add()
        Stats.avg("f_1").add(10)
        Stats.avg("f_1").add(32)
        for _ in range(10):
            Stats.count("f_1").add()
        expected = {
            "f_1.timer": 25,
            "function.count": 3,
            "div.avg": 17,
            "f_2.timer": 1.2,
            "gen.count": 1,
            "f_1.avg": 21,
            "f_1.count": 10
        }
        self.assertDictEqual(expected, Stats.collect())
        self.assertDictEqual({}, Stats.collect())


    def test_no_add_to_collect(self):
        Stats.avg("calc").add(2)
        Stats.avg("calc").add(5)
        Stats.count("func").add()

        Stats.timer("calc")
        Stats.count("no_used")
        Stats.avg("no_used")

        expected = {
            "calc.avg": 3.5,
            "func.count": 1
        }
        self.assertDictEqual(expected, Stats.collect())
        self.assertDictEqual({}, Stats.collect())
