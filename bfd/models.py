##
# -*- coding: utf-8 -*-
##

class BotProfile:
	__slots__ = ['_client', 'avatar', 'invite', 'website', 'guild_count', 'timestamp', 'owner', 'id', 'approved', 'verified', 'shortdesc', 'longdesc', 'name', 'prefix', 'desctype']

	def __init__(self, client, data):
		self._client = client

		self.name = data.get('name')
		self.prefix = data.get('prefix')
		self.avatar = data.get('avatar')
		self.invite = data.get('invite')
		self.website = data.get('website')

		self.shortdesc = data.get('shortDesc')
		self.longdesc = data.get('longDesc')
		self.desctype = data.get('type')

		self.guild_count = data.get('count')
		self.timestamp = data.get('timestamp')
		self.owner = Owner.from_profile_data(client, data)
		self.id = data.get('id')

		self.approved = data.get('approved', False)		
		self.verified = data.get('verified', False)

	def __repr__(self):
		return '<bfd.BotProfile: <id=%s, owner=%s>>' %(self.id, self.owner.id)

	async def embed(self):
		return await self._client.http.bot_embed(self.id)

	async def update(self, **data):
		return await self._client.http.update_bot(self.id, data)


class Owner:
	__slots__ = ['_client', 'name', 'id']

	def __init__(self, client, name, user_id):
		self._client = client

		self.name = name
		self.id = user_id

	def __repr__(self):
		return '<bdf.Owner: <name="%s", id=%s>>' %(self.name, self.id)

	@classmethod
	def from_profile_data(cls, client, data):
		user_id = data.get('owner')
		name = data.get('ownernametwo')

		return cls(client, name, user_id)
