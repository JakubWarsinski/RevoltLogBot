from revolt import Message

def is_valid_message(message: Message) -> bool:
    if message.author.bot:
        return False
    
    if not message.content and not message.attachments:
        return False
    
    if message.content.startswith("/"):
        return False
    
    return True