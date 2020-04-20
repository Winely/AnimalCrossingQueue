import unittest

from src.services.wechat import parse_message_body

class WechatServiceTest(unittest.TestCase):
    def test_parse_wechat_text_message(self):
        test_xml = """
        <xml><ToUserName><![CDATA[gh_2c148e27b924]]></ToUserName>
        <FromUserName><![CDATA[oT-_Nv0MU1B5lKvdSgAw6_fM3l6Y]]></FromUserName>
        <CreateTime>1534254497</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[hello]]></Content>
        <MsgId>6589572888778149127</MsgId>
        </xml>
        """
        message = parse_message_body(test_xml)
        self.assertEqual(message.to_user_name, 'gh_2c148e27b924')
        self.assertEqual(message.from_user_name, 'oT-_Nv0MU1B5lKvdSgAw6_fM3l6Y')
        self.assertEqual(message.msg_type, 'text')
        self.assertEqual(message.msg_id, '6589572888778149127')
        self.assertEqual(message.content, 'hello')
