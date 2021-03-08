from base import abstract
from base.models import ServiceStatus
from base.config import AdapterError
import asyncio


class AdaYoroiBackendBased(abstract.AbstractAdapter):
    async def get_status(self) -> ServiceStatus:

        await self.__is_server_ok()
        if self.service_status.error_code:
            return self.service_status
        else:
            await self.__get_height()
            return self.service_status

    async def __is_server_ok(self):
        resp = await self._send_http_request(
            url=f"{self.url}/status"
        )
        if not self.service_status.error_code:
            try:
                status = resp.get("isServerOk")
                if not status:
                    return ServiceStatus(
                        error_code=AdapterError.INSTANCE_REPORT_ERROR.value,
                        error_message="Error: Backend responded that isServerOk == false"
                    )
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())

    async def __get_height(self):
        resp = await self._send_http_request(
            url=f"{self.url}/v2/bestBlock",
        )

        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["height"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())


if __name__ == '__main__':
    a = AdaYoroiBackendBased(url="https://ada-backend.guarda.co", coin="ada")
    print(asyncio.get_event_loop().run_until_complete(a.get_status()))
