from base import abstract
from base.models import ServiceStatus
import json


class SubscanBased(abstract.AbstractAdapter):
    async def get_status(self) -> ServiceStatus:
        await self.__get_height()
        return self.service_status

    async def __get_height(self):
        resp = await self._send_http_request(
            url=f"{self.url}/api/scan/blocks",
            body=json.dumps({"row": 25, "page": 0}),
            method="POST"
        )

        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["data"]["blocks"][0]["block_num"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())
