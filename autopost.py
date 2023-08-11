import requests, time

config = {
    "token": "discord token",
    "content": "Content",
    "channel": ["Channel id"]
}

def sendMessage(channel_id):
    return requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", 
    data = {
        "content": config["content"]
    }, 
    headers = {
        'authorization': config["token"]
    }, files = {
        "file" : ("./save2.jpg", open("./save2.jpg", 'rb'))
    })



while True:
    for i in config["channel"]:
        status = sendMessage(i)
        currenttime_str = time.ctime()
        if status.status_code != 200:
            print(f"{currenttime_str} Connot send message, channelID: {i}")
        else:
            print(f"{currenttime_str} Success, channelID: {i}")

    time.sleep(60 * 10)
