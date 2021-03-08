from base import abstract
from base.models import ServiceStatus
from base.config import AdapterError


class BlockBookBased(abstract.AbstractAdapter):

    async def get_status(self) -> ServiceStatus:

        await self.__is_synced()
        if self.service_status.error_code:
            return self.service_status
        else:
            await self.__get_height()
            return self.service_status

    async def __is_synced(self):
        resp = await self._send_http_request(
            url=f"{self.url}/api",
        )
        if not self.service_status.error_code:
            try:
                is_synced = bool(resp["response"]["blockbook"]["inSync"])
                if not is_synced:
                    self.service_status = ServiceStatus(
                        error_code=AdapterError.INSTANCE_REPORT_ERROR.value,
                        error_message="Error: Blockbook isSynced == false"
                    )
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())

    async def __get_height(self):
        resp = await self._send_http_request(
            url=f"{self.url}/api",
        )
        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["blockbook"]["bestHeight"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())
