from bchain_api_wrappers.base import abstract
from bchain_api_wrappers.base.models import ServiceStatus
from bchain_api_wrappers.base.config import COIN_FAMILIES


class GoalSeekerBased(abstract.AbstractAdapter):

    async def get_status(self) -> ServiceStatus:
        await self.__get_height()
        return self.service_status

    async def __get_height(self):
        try:
            resp = await self._send_http_request(
                url=f"{self.url}/Prod/{str(COIN_FAMILIES[self.coin]).lower()}/mainnet/status",
                http_headers={
                    "authority": self.url,
                    "origin": "https://goalseeker.purestake.io"
                },
                parse_json=True
            )
            if not self.service_status.error_code:
                height = int(resp["response"]["latestBlock"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
        except (KeyError, ValueError) as ex:
            self._set_response_error(ex.__str__())
