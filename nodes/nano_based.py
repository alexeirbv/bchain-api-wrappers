from base import abstract
from base.models import ServiceStatus
import json


class NanoBased(abstract.AbstractAdapter):
    async def get_status(self) -> ServiceStatus:

        await self.__get_height()
        return self.service_status

    async def __get_height(self):
        resp = await self._send_http_request(
            url=self.url,
            body=json.dumps({"action": "block_count", "include_cemented": False}),
            method="POST"
        )

        if not self.service_status.error_code:
            try:
                height = int(resp["count"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())
