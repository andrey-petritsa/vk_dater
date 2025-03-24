def to_str_one(chat):
    return chat['id']

def to_str_many(chats):
    str_chats = []
    for chat in chats:
        str_chats.append(to_str_one(chat))

    return str_chats