from revolt import Client

CLIENT : Client

CHANNELS = {}

CHANNEL_IDS = {
    "Joined_Users" : "01JY9JWBY0Q4VAE6XRTMH7W6N1",
    "Leaved_Users" : "01JY9JX7BXPCF5DSDVENWTAPVJ",
    "Kicked_Users" : "01JYC64PM315VXJW9X1Q4FDKD8",
    "Banned_Users" : "01JYC4F206AJZAB9KCCA6JYEHH",
    "Edited_Messages" : "01JY9P0PS5M0DG9C1R3VXHZKBR",
    "Posted_Messages" : "01JY9JVPXE6NFTA12F2QYZZ9SZ",
    "Removed_Messages" : "01JY9JW1QB00KWT2C3QAASK6WA"
}

class ServerData:
    def __init__(self, client: Client):
        global CLIENT
        
        CLIENT = client

    async def initialize(self):
        global CHANNELS

        for name, id in CHANNEL_IDS.items():
            try:
                CHANNELS[name] = await CLIENT.fetch_channel(id)
            except ValueError as e:
                print(e)

        print("Config initialization done.")


async def fetch_channel(name: str):
    global CHANNELS

    try:
        CHANNELS[name] = await CLIENT.fetch_channel(CHANNEL_IDS[name])
    except ValueError as e:
        print(e)