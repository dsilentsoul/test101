# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
import boto3
client = boto3.client('lex-runtime', verify=False)

class EchoBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        response = client.post_text(
            botName='FirstBot',
            botAlias='FirstbotOne',
            userId=turn_context.activity.id,
            inputText=turn_context.activity.text,
        )
        print(response)
        text = response['message']
        print(text)
        #print(turn_context.activity, type(turn_context.activity))
        print(turn_context.activity.text,type(turn_context.activity.text))
        return await turn_context.send_activity(
            MessageFactory.text(f"Echo: {text}")
        )
