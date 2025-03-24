from vk_girl_dater.voter.message_fliter import MessageFilter


class TestMessageFilter:
    def test_filter_since_date(self):
        msgs = [{'date': 1}, {'date': 2}, {'date': 3}]
        assert MessageFilter(msgs).since_date(2) == [{'date':2}, {'date':3}]
