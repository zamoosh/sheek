from .imports import *


class IpPanel:
    PATTERNS = {
        'enter_code': '7idc1u6rft5dxiz',
    }

    def __init__(self):
        self.api_key = settings.IPPANEL_TOKEN
        self.line_number = settings.IPPANEL_SMSNUMBER
        self.sms = Client(self.api_key)

    def send_with_pattern(self, pattern: str, recipient: str, values: dict, line_number=settings.IPPANEL_SMSNUMBER):
        if type(values) == dict:
            self.sms.send_pattern(pattern, line_number, recipient, values)

    def send_sms(self, recipients: list, sms_text: str, line_number=settings.IPPANEL_SMSNUMBER):
        self.sms.send(line_number, recipients, sms_text)
