from data import ChannelService
import re
from loader import client
from telethon import errors

class ChannelParser:
    """
    A class for parsing Telegram channels.

    Methods
    -------
    _get_channel_id(channel: str) -> str|None:
        Get the ID of the given Telegram channel.

    _get_channel_name(channel: str) -> str|None:
        Get the name of the given Telegram channel.

    set_name() -> None:
        Set the name of all channels returned by ChannelService.get_all_channels().
    """
    
    async def _get_channel_id(self, channel: str)->str|None:
        """
        Get the ID of the given Telegram channel.

        Parameters
        ----------
        channel : str
            The name or username of the channel.

        Returns
        -------
        str
            The ID of the channel.
        """
        try:
            entity = await client.get_entity(channel)
            channel_id = entity.id
            return channel_id
        except errors.ChannelInvalidError:
            print('Channel not found')
            return None

    async def _get_channel_name(self, channel: str)->str|None:
        """
        Get the name of the given Telegram channel.

        Parameters
        ----------
        channel : str
            The ID of the channel.

        Returns
        -------
        str
            The name of the channel.
        """
        try:
            entity = await client.get_entity(channel)
            channel_name = entity.title
            return channel_name
        except errors.ChannelInvalidError:
            print('Channel not found')
            return None

    async def set_name(self)->None:
        """
        Set the name of all channels returned by ChannelService.get_all_channels().
        """
        channels = ChannelService.get_all_channels()
        for k, v in channels.items():
            if v == None:
                id = await self._get_channel_id(k)
                name = await self._get_channel_name(id)
                ChannelService.update_name(k, name)