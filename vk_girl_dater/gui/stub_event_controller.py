
class StubEventController:
    @classmethod
    def handle_event(cls, event):
        print(event)

        if event['name'] == 'show_options':
            return ['оп1', 'оп2']