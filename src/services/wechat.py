# -*- coding: utf-8 -*-
from enum import Enum
from datetime import datetime
import xml.etree.ElementTree as ET
from src.utils import camel_to_snake_case

# 微信 普通消息类型
class WechatMessageType(Enum):
    TEXT = 'text'
    IMAGE = 'image'
    VOICE = 'voice'
    VIDEO = 'video'
    SHORTVIDEO = 'shortvideo'
    LOCATION = 'location'
    LINK = 'link'

# 通用参数
class BasicMessage():
    def __init__(self, to_user_name='', from_user_name='', create_time=0, msg_type='text', msg_id=''):
        self.to_user_name = to_user_name
        self.from_user_name = from_user_name
        self.create_time = create_time
        self.msg_type = msg_type
        self.msg_id = msg_id
        self.extra = dict()
    def clone(self, source):
        self.to_user_name = source.to_user_name
        self.from_user_name = source.from_user_name
        self.create_time = source.create_time
        self.msg_type = source.msg_type
        self.msg_id = source.msg_id
        self.extra = dict()
    def to_dict(self):
        return {
            'to_user_name': self.to_user_name,
            'from_user_name': self.from_user_name,
            'create_time': self.create_time,
            'msg_type': self.msg_type,
            'msg_id': self.msg_id
        }

# 文本消息
class TextMessage(BasicMessage):
    def __init__(self, message, content):
        super().clone(message)
        self.content = content
    def to_dict(self):
        d = super().to_dict()
        d['content'] = self.content
        return d

# 图片消息
class ImageMessage(BasicMessage):
    def __init__(self, message, pic_url, media_id):
        super().clone(message)
        self.pic_url = pic_url
        self.media_id = media_id
    def to_dict(self):
        d = super().to_dict()
        d['pic_url'] = self.pic_url
        d['media_id'] = self.media_id
        return d

# 语音消息
class VoiceMessage(BasicMessage):
    def __init__(self, message, media_id, format):
        super().clone(message)
        self.media_id = media_id
        self.format = format
    def to_dict(self):
        d = super().to_dict()
        d['media_id'] = self.media_id
        d['format'] = self.format
        return d

# 视频消息 or 小视频消息
class VideoMessage(BasicMessage):
    def __init__(self, message, media_id, thumb_media_id):
        super().clone(message)
        self.media_id = media_id
        self.thumb_media_id = thumb_media_id
    def to_dict(self):
        d = super().to_dict()
        d['media_id'] = self.media_id
        d['thumb_media_id'] = self.thumb_media_id
        return d

class LocationMessage(BasicMessage):
    def __init__(self, message, location_x, location_y, scale, label):
        super().clone(message)
        self.location_x = location_x
        self.location_y = location_y
        self.scale = scale
        self.label = label
    def to_dict(self):
        d = super().to_dict()
        d['location_x'] = self.location_x
        d['location_y'] = self.location_y
        d['scale'] = self.scale
        d['label'] = self.label
        return d

class LinkMessage(BasicMessage):
    def __init__(self, message, title, description, url):
        super().clone(message)
        self.title = title
        self.description = description
        self.url = url
    def to_dict(self):
        d = super().to_dict()
        d['title'] = self.title
        d['description'] = self.description
        d['url'] = self.url
        return d

def parse_message_body(xml_text):
    root = ET.fromstring(xml_text)

    # 取出公共字段
    message = BasicMessage()
    for child in root:
        field = child.tag
        value = child.text
        if field == 'ToUserName':
            message.to_user_name = value
        elif field == 'FromUserName':
            message.from_user_name = value
        elif field == 'CreateTime':
            message.create_time = datetime.fromtimestamp(int(value))
        elif field == 'MsgType':
            message.msg_type = value
        elif field == 'MsgId':
            message.msg_id = value
        else:
            message.extra[camel_to_snake_case(field)] = value

    # 转换为具体的消息类型
    converters = {
        WechatMessageType.TEXT.value: (lambda: TextMessage(message, message.extra['content'])),
        WechatMessageType.IMAGE.value: (lambda: ImageMessage(message, message.extra['pic_url'], message.extra['media_id'])),
        WechatMessageType.VOICE.value: (lambda: VoiceMessage(message, message.extra['media_id'], message.extra['format'])),
        WechatMessageType.VIDEO.value: (lambda: VideoMessage(message, message.extra['media_id'], message.extra['thumb_media_id'])),
        WechatMessageType.SHORTVIDEO.value: (lambda: VideoMessage(message, message.extra['media_id'], message.extra['thumb_media_id'])),
        WechatMessageType.LOCATION.value: (lambda: LocationMessage(
            message,
            message.extra['location_x'],
            message.extra['location_y'],
            message.extra['scale'],
            message.extra['label']
        )),
        WechatMessageType.LINK.value: (lambda: LinkMessage(
            message,
            message.extra['title'],
            message.extra['description'],
            message.extra['url'],
        ))
    }
    if message.msg_type in converters:
        message = converters[message.msg_type]()
    return message
