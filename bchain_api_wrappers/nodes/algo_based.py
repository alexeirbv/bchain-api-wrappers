from bchain_api_wrappers.base import abstract
from bchain_api_wrappers.base.models import ServiceStatus


class AlgoBased(abstract.AbstractAdapter):
    def __init__(self, url: str, coin: str, **kwargs):
        super().__init__(url, coin, **kwargs)
        try:
            self.api_token = self.api_token
        except AttributeError:
            self.api_token = "887da563be462e10dbe99c87b5d7be742610838a41bede7bf73cb391696334a1"

    async def get_status(self) -> ServiceStatus:

        await self.__get_height()
        return self.service_status

    async def __get_height(self):
        resp = await self._send_http_request(
            url=f"{self.url}/v2/status",
            method="GET",
            http_headers={
                "X-Algo-API-token": self.api_token
            }
        )
        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["last-round"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())
