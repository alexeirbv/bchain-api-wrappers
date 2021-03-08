from base import abstract
from base.models import ServiceStatus


class Eth2PrysmBased(abstract.AbstractAdapter):
    async def get_status(self) -> ServiceStatus:

        await self.__get_height()
        return self.service_status

    async def __get_height(self):
        resp = await self._send_http_request(
            url=f"{self.url}/eth/v1alpha1/beacon/chainhead",
        )
        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["headSlot"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())

