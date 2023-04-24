# main.py to run the backend server based on FastAPI
# Created by Jan Macenka @ 24 Apr 2023

# Configuration import
from config.config import (
    ACCOUNT_SID,
    AUTH_TOKEN,
    TWILIO_PHONE_NUMBER
)

# Module imports
from fastapi import FastAPI, Request
import uvicorn
from twilio.rest import Client

# Class import
from Message import Message

app = FastAPI()

# Twilio account details
client = Client(ACCOUNT_SID, AUTH_TOKEN)


@app.post('/send')
async def send_sms(message: Message):
    twilio_message = client.messages.create(
        to=message.to_number,
        from_=TWILIO_PHONE_NUMBER,
        body=message.message
    )
    return {"status": "sent", "message_id": twilio_message.sid}


@app.get('/hallo')
def egalwiedasheisst():
    return "Hallo"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
