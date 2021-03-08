from bchain_api_wrappers.base import abstract
from bchain_api_wrappers.base.models import ServiceStatus
from datetime import datetime


class BitcoinComBased(abstract.AbstractAdapter):
    async def get_status(self) -> ServiceStatus:

        await self.__get_height()
        return self.service_status

    async def __get_height(self):
        date = datetime.date(datetime.now())
        resp = await self._send_http_request(
            url=f"{self.url}/v1/blocks?blockDate={date}",
        )
        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["blocks"][0]["height"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())
