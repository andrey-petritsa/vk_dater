class EventController:
    @classmethod
    def handle_event(cls, event):
        print(event)

        if event['name'] == 'show_options':
            return ['123', '456']