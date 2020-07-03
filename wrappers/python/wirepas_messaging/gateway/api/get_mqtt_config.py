import wirepas_messaging

from .request import Request
from .response import Response

class GetMqttConfigRequest(Request):
    def __init__(self, req_id=None, **kwargs):
        super(GetMqttConfigRequest, self).__init__(req_id=req_id, **kwargs)

    @classmethod
    def from_payload(cls, payload):
        message = wirepas_messaging.gateway.GenericMessage()
        try:
            message.ParseFromString(payload)
                except Exception:
            # Any Exception is promoted to Generic API exception
            raise GatewayAPIParsingException("Cannot parse GetConfigsRequest payload")

        req = message.customer.get_mqtt_config_req
        

    @property
    def payload(self):
        message = wirepas_messaging.gateway.GenericMessage()
        get_mqtt_config = message.customer.mqtt_get_config_req
        get_mqtt_config.header.CopyFrom(self._make_request_header())

        return message.SerializeToString()
