from bchain_api_wrappers.base import abstract
from bchain_api_wrappers.base.models import ServiceStatus
import json


class BtcBased(abstract.AbstractAdapter):

    async def get_status(self) -> ServiceStatus:

        await self.__get_height()
        await self.__get_peers_count()
        return self.service_status

    async def __get_height(self):
        resp = await self._send_http_request(
            url=self.url,
            method="POST",
            body=json.dumps({"jsonrpc": "1.0", "id": "height-tower", "method": "getblockchaininfo", "params": []}),
        )

        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["result"]["blocks"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())

    async def __get_peers_count(self):
        resp = await self._send_http_request(
            url=self.url,
            method="POST",
            body=json.dumps({"jsonrpc": "1.0", "id": "height-tower", "method": "getpeerinfo", "params": []}),
            set_error=False
        )
        self.service_status.peers_count = len(resp["result"]) if resp.get("result") else 0
