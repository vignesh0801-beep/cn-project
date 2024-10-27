from twilio.rest import Client

account_sid = 'AC055caf982adc2f9d44fed9fd56c862c0'
auth_token = 'ad752261378c9f3fbd010008c567867f'
client = Client(account_sid, auth_token)

def sendSms():
    message = client.messages.create(
        from_='+12562978755',
        body='intruder alert',
        to='+918788030694'
    )
    print(message.sid)
