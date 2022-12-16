GOOD_WORDS = ['great', 'good', 'amazing', 'wonderful', 'cool', 'nice', 'super']
BAD_WORDS = ['ugly', 'bad', 'awful', 'disgusting', 'terrible']
LEN_CUTOFF = 20


class SomeModel:
    @staticmethod
    def predict(message: str) -> float:
        msg_len = len(message)
        message = message.lower().strip()
        message_arr = message.split()
        count_good = 0
        count_bad = 0
        for word in message_arr:
            if word in GOOD_WORDS:
                count_good += 1
            if word in BAD_WORDS:
                count_bad += 1

        if count_good == 0 and count_bad > 0:
            return 0.0
        if count_good > 0 and count_bad == 0:
            return 1.0
        if count_good == 0 and count_bad == 0:
            if msg_len > LEN_CUTOFF:
                return LEN_CUTOFF / msg_len
            return 1. - msg_len / LEN_CUTOFF
        return count_good / (count_bad + count_good)

    def train(self):
        pass


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if not message:
        raise Exception("Sorry, message is empty")
    prob = model.predict(message)
    print(prob)
    if prob < bad_thresholds:
        return "неуд"
    if good_thresholds < prob:
        return "отл"
    return "норм"
