
class StubEventController:
    def handle_event(self, event):
        print(event)

        if event['name'] == 'show_options':
            return ['оп1', 'оп2']