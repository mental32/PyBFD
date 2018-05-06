##
# -*- coding: utf-8 -*-
##
import asyncio
import aiohttp
import json
from urllib.parse import quote

class Route:
    BASE = 'https://botsfordiscord.com/api/v1'

    def __init__(self, method, path, **kwargs):
        self.path = path
        self.method = method
        self.url = (self.BASE + self.path)

        if kwargs:
            parameters = {key: (quote(v) if isinstance(v, str) else v) for key, v in kwargs.items()}
            self.url = self.url.format(**parameters)

class HTTPClient:
	def __init__(self, token=None):
		self.token = token
		self.loop = asyncio.get_event_loop()

		self._session = aiohttp.ClientSession(loop=self.loop)

	def __del__(self):
		asyncio.run_coroutine_threadsafe(self._session.close(), self.loop)

	@property
	def headers(self):
		_headers = {'Content-Type': 'application/json'}

		if self.token:
			_headers['Authorization'] = self.token
		return _headers

	async def request(self, route, **kwargs):
		method = route.method
		url = route.url

		r = await self._session.request(method, url, headers=self.headers, **kwargs)
		text = await r.text(encoding='utf-8')
		try:
			data = json.loads(text)

			if 300 > r.status >= 200:
				return data

		except json.decoder.JSONDecodeError:
			return text

		finally:
			r.release()

	async def bots(self):
		route = Route('GET', '/bots')
		return await self.request(route)

	async def bot(self, bot_id):
		route = Route('GET', '/bots/{id}', id=bot_id)
		return await self.request(route)

	async def update_bot(self, bot_id, data):
		route = Route('POST', '/bots/{id}', id=bot_id)
		return await self.request(route, data=json.dumps(data))

	async def bot_embed(self, bot_id):
		route = Route('GET', '/bots/{id}/embed', id=bot_id)
		return await self.request(route)
