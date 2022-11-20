import json
from channels.generic.websocket import AsyncWebsocketConsumer

from screens.models import Screen


class ScreenConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.roomGroupName = "group_chat_gfg"
		await self.channel_layer.group_add(
			self.roomGroupName,
			self.channel_name
		)
		await self.accept()

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(
			self.roomGroupName,
			self.channel_layer
		)

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json["message"]
		await self.channel_layer.group_send(
			self.roomGroupName, {
				"type": "sendMessage",
				"message": message,
			})

	async def sendMessage(self, event):
		message = event["message"]

		screen = await Screen.objects.aget(id=1)
		screen.message = message
		await screen.asave()

		await self.send(text_data=json.dumps({
			"message": message,
		}))
