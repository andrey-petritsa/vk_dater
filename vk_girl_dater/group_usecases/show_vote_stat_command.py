import random


class ShowVoteStatCommand:
    def execute(self, votes):
        vote_stat = {}
        for vote in votes:
            option_number = vote['option_number']
            voter = f"{vote['first_name']} {vote['last_name']}"

            if option_number not in vote_stat:
                vote_stat[option_number] = {'vote_count':0, 'option_number':option_number, 'voters':[]}

            vote_stat[option_number]['vote_count'] += 1
            vote_stat[option_number]['voters'].append(voter)

        result = list(vote_stat.values())
        random.shuffle(result)
        return sorted(result, key=lambda x:x['vote_count'], reverse=True)
