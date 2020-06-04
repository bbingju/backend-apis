import wirepas_messaging

from .request import Request
# from .gateway_result_code import GatewayResultCode


class UpgradeFirmwareRequest(Request):
    """
    UpgradeFirmwareRequest: Request to upgrade a firmware

    Attributes:
        url (str): url where is a firmware binary to upgrade
    """
    def __init__(self, url, req_id=None, **kwargs):
        super(UpgradeFirmwareRequest, self).__init__(req_id=req_id, **kwargs)
        self.url = url

    @property
    def payload(self):
        message = wirepas_messaging.gateway.GenericMessage()
        message.customer.customer_name = "vinetech"

        upgrade_firmware = message.customer.upgrade_firmware_req
        upgrade_firmware.header.CopyFrom(self._make_request_header())

        upgrade_firmware.url = self.url

        return message.SerializeToString()
