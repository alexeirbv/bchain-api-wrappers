from bchain_api_wrappers.base import abstract
from bchain_api_wrappers.base.models import ServiceStatus
import json


class DotBased(abstract.AbstractAdapter):

    async def get_status(self) -> ServiceStatus:

        await self.__get_height()
        await self.__get_peers_count()
        return self.service_status

    async def __get_height(self):
        resp = await self._send_http_request(
            url=self.url,
            body=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "chain_getBlock", "params": []}),
            method="POST"
        )

        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["result"]["block"]["header"]["number"], 16)
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())

    async def __get_peers_count(self):
        try:
            resp = await self._send_http_request(
                url=self.url,
                method="POST",
                body=json.dumps({"jsonrpc": "2.0", "id": "chainvisor", "method": "system_health", "params": []}),
                set_error=False
            )
            self.service_status.peers_count = int(resp["response"]["result"]["peers"])
        except (KeyError, ValueError):
            return
