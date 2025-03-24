import time
from datetime import datetime

from test.tests.vk_date_platform.settings import group_id
from vk_girl_dater.chat_group_presenters.chat_presenter import ChatPresenter
from vk_girl_dater.chat_group_presenters.option_presenter import OptionPresenter
from vk_girl_dater.chat_group_presenters.vote_presenter import VotePresenter
from vk_girl_dater.group_usecases.send_message_to_group_command import SendMessageToGroupCommand
from vk_girl_dater.group_usecases.show_vote_stat_command import ShowVoteStatCommand
from vk_girl_dater.main import setup_utils, setup_usecases
import vk_girl_dater.utils as utils
from vk_girl_dater.voter.event_parser import EventParser
from vk_girl_dater.voter.group_chat import GroupChat
import vk_girl_dater.usecases as usecases
from vk_girl_dater.voter.telegram import Telegram

VOTE_TIME = 60*2

setup_utils()
setup_usecases()

telegram = Telegram()
group_chat = GroupChat(telegram)

send_message_to_group_command = SendMessageToGroupCommand(group_chat)
chat_presenter = ChatPresenter()
option_presenter = OptionPresenter()
event_parser = EventParser()
show_vote_stat_command = ShowVoteStatCommand()
voter_presenter = VotePresenter()

def read_allowed_chat_ids():
    f = open('chats.txt', 'r')
    f_content = f.read()
    ids = [int(id) for id in f_content.split('\n')]

    return ids

while(True):
    chats = usecases.get_chats_info_command.execute()
    not_answered_chats = [chat for chat in chats if not chat['is_answered']]
    allowed_chat_ids = read_allowed_chat_ids()
    allowed_chats = [chat for chat in not_answered_chats if chat['id'] in allowed_chat_ids]

    for chat in not_answered_chats:
        print(f"Current time: {datetime.now()}")
        chat = usecases.get_chat_command.execute(chat['id'])
        chat['messages'] = chat['messages'][-5:]
        chat_view = chat_presenter.present(chat['messages'])
        options = usecases.get_message_options_command.execute(chat)
        voter_presenter.set_options(options)
        option_view = option_presenter.present(options)
        vote_start_timestamp = utils.time_provider.get_now_date_as_timestamp()
        start_vote_msg = f'Начинается голосование\n{chat_view}\n\n\n--------------{option_view}'
        send_message_to_group_command.execute(start_vote_msg, group_id)

        time.sleep(VOTE_TIME)

        msgs = group_chat.get_messages_since(vote_start_timestamp)
        events = event_parser.to_events(msgs)
        votes = [event['context'] for event in events if event['name'] == 'vote_option']
        vote_stats = show_vote_stat_command.execute(votes)
        view_vote_stats = voter_presenter.present(vote_stats)
        send_message_to_group_command.execute(view_vote_stats, group_id)

        if len(vote_stats) != 0:
            win_option = options[vote_stats[0]['option_number'] - 1]
            message = {'user_id': chat['id'], 'text': win_option}
            usecases.send_message_command.execute(message)
            print(f'Отправляю сообщение:{win_option} в {chat["id"]}')

    time.sleep(60)


