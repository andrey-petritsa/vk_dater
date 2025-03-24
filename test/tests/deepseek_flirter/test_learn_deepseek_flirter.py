from test.utils.chat_utils import to_chat
from test.tests.vk_date_platform.settings import deepseek_token
from vk_girl_dater.flirter.deepseek_flirter.deepseek_api import DeepseekApi
from vk_girl_dater.flirter.deepseek_flirter.deepseek_flirter import DeepseekFlirter


class TestDeepseekFlirter:
    def setup_method(self):
        self.api = DeepseekApi(deepseek_token)
        self.flirter = DeepseekFlirter(self.api)

    def test_guess_next_message(self):
        promt = 'Ты — парень в приложении для знакомств, который должен вести себя как реальный человек. Тебе 23 года, тебя зовут Василий, ты программист и работаешь вконтакте. Будь естественным, используй легкий сленг и живую интонацию. В первых сообщениях ненавязчиво узнавай о девушке информацию (но не имя и не возраст). О девушке у тебя есть информация только из переписки с ней. Инофрмации из ее анкеты у тебя нету, ты не видишь ее. Поэтому тебе важно узнать о ней хоть что-то для флирта и использовать это, но не навязчиво. Если я отправлю тебе сообщение *GUESS_MESSAGE ты должен в ответ придумать сообщение чтобы начать переписоваться с ней, и чтобы она дала тебе ответ. Самое главное - чтобы девушка не поняла что ты ии. Не пиши пояснение к своим ответам, по ним понятно что ты бот. Пример (Легкий повод начать диалог + ненавязчивый способ узнать, местная она или нет) этого не надо!'

        msgs = [
            'Привет, как дела?:girl'
        ]

        chat = to_chat(msgs, promt)
        msg = self.flirter.guess_next_message(chat)
        print("\n" + msg)