from revolt import Message, SendableEmbed, TextChannel, Member
from datetime import datetime


def format_datetime():
    return datetime.now().strftime("%d/%m/%Y %H:%M")


async def generate_message_description(channel : TextChannel, message : Message, event_type : str, *, second_message : Message = None, color : str = None):
    user_id = message.author.id
    content = message.content
    attachments = message.attachments
    
    description = f"**USER**: <@{user_id}>\n\n"
    
    if content:
        description += f"**CONTENT**:\n*{content}*\n\n"
    
    if attachments:
        description += "**ATTACHMENTS**:\n"
        description += "\n".join(item.url for item in attachments) + "\n\n"

    if second_message:
        content = second_message.content
        attachments = second_message.attachments

        if content:
            description += f"**CHANGED TO**:\n*{content}*\n\n"
    
        if attachments:
            description += "**ATTACHMENTS**:\n"
            description += "\n".join(item.url for item in attachments) + "\n\n"
    
    description += f"**{event_type.upper()} AT**: *{format_datetime()}*"
    
    embed = SendableEmbed(
        description=str(description),
        colour=color,
    )

    await channel.send(embed=embed)

    print("Generated Message")