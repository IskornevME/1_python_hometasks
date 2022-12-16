import unittest
from unittest.mock import patch, call

from predict_message import predict_message_mood, SomeModel


class TestPredictMessage(unittest.TestCase):
    def setUp(self):
        self.model = SomeModel()

    def test_empty_message(self):
        with self.assertRaises(Exception) as err:
            predict_message_mood("", self.model)
        expected = "Sorry, message is empty"
        self.assertEqual(str(err.exception), expected)

    def test_good_msg(self):
        with patch("predict_message.SomeModel.predict") as mpred:
            mpred.return_value = 0.9
            msg = "some message with good mood"
            res = predict_message_mood(msg, self.model)
            self.assertEqual(res, "отл")

            expected_calls = [
                call("some message with good mood"),
            ]
            self.assertEqual(expected_calls, mpred.mock_calls)

    @patch("predict_message.SomeModel.predict")
    def test_bad_msg(self, mpred):
        mpred.return_value = 0.2
        msg = "this text has very bad mood"
        res = predict_message_mood(msg, self.model)
        self.assertEqual(res, "неуд")

        expected_calls = [
            call("this text has very bad mood"),
        ]
        self.assertEqual(expected_calls, mpred.mock_calls)

    @patch("predict_message.SomeModel.predict")
    def test_all_kinds_msgs(self, mpred):
        mpred.side_effect = [
            0.0,
            0.99,
            1.0,
            0.5,
            0.29,
            0.79,
            0.4,
            0.85
        ]
        msgs = [
            "bad awful msg",
            "good nice cool amazing great msg, not bad",
            "Chapaev is amasing person",
            "this is not good and bad msg",
            "Чапаев и пустота",
            "Some text larger than 20 symbols",
            "this is badly msg",
            "this text has very bad mood"
        ]
        res = predict_message_mood(msgs[0], self.model)
        self.assertEqual(res, "неуд")
        res = predict_message_mood(msgs[1], self.model)
        self.assertEqual(res, "отл")
        res = predict_message_mood(msgs[2], self.model)
        self.assertEqual(res, "отл")
        res = predict_message_mood(msgs[3], self.model)
        self.assertEqual(res, "норм")
        res = predict_message_mood(msgs[4], self.model)
        self.assertEqual(res, "неуд")
        res = predict_message_mood(msgs[5], self.model)
        self.assertEqual(res, "норм")
        res = predict_message_mood(
            msgs[6],
            self.model,
            bad_thresholds=0.43
        )
        self.assertEqual(res, "неуд")
        res = predict_message_mood(
            msgs[7],
            self.model,
            good_thresholds=0.9
        )
        self.assertEqual(res, "норм")

        expected_calls = [
            call(msgs[i]) for i in range(len(msgs))

        ]
        self.assertEqual(expected_calls, mpred.mock_calls)
