from vk_girl_dater.group_usecases.show_vote_stat_command import ShowVoteStatCommand


class TestChooseWinnerCommand:
    def test_execute(self):
        cmd = ShowVoteStatCommand()
        votes = [
            {'option_number': 1, 'user_id': 1, 'first_name': 'Андрей', 'last_name': 'Петрица'},
            {'option_number': 1, 'user_id': 2, 'first_name': 'Александр', 'last_name': 'Пушкин'},
            {'option_number': 2, 'user_id': 3, 'first_name': 'Николай', 'last_name': 'Николаевич'},
        ]
        
        vote_stat = cmd.execute(votes)

        e_vote_stat = [
            {'vote_count': 2, 'option_number': 1, 'voters': ['Андрей Петрица', 'Александр Пушкин']},
            {'vote_count': 1, 'option_number': 2, 'voters': ['Николай Николаевич']}
        ]

        assert vote_stat == e_vote_stat