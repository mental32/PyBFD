##
# -*- coding: utf-8 -*-
##
import asyncio

from .http import HTTPClient
from .models import BotProfile

class Client:
	def __init__(self, token=None):
		self.loop = asyncio.get_event_loop()
		self.http = HTTPClient(token)

	async def get_bot(self, bot_id):
		data = await self.http.bot(bot_id)
		if not data:
			raise
		return BotProfile(self, data)

	async def get_bots(self):
		return (BotProfile(self, item) for item in (await self.http.bots()))
