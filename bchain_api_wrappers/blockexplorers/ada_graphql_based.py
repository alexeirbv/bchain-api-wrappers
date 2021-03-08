from bchain_api_wrappers.base import abstract
from bchain_api_wrappers.base.models import ServiceStatus
from bchain_api_wrappers.base.config import AdapterError


class AdaGraphQLBased(abstract.AbstractAdapter):

    async def get_status(self) -> ServiceStatus:

        await self.__is_synced()
        if self.service_status.error_code:
            return self.service_status
        else:
            await self.__get_height()
            return self.service_status

    async def __is_synced(self):

        query = """ { cardanoDbMeta { initialized }} """
        resp = await self._send_graphql_request(url=self.url, query=query)
        if not self.service_status.error_code:
            try:
                is_synced = bool(resp["response"]["data"]["cardanoDbMeta"]["initialized"])
                if not is_synced:
                    return ServiceStatus(
                        error_code=AdapterError.INSTANCE_REPORT_ERROR.value,
                        error_message="Error: { cardanoDbMeta { initialized }} == false"
                    )
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())

    async def __get_height(self):
        query = """ { cardano { tip { number slotNo epoch { number } } } } """
        resp = await self._send_graphql_request(url=self.url, query=query)

        if not self.service_status.error_code:
            try:
                height = int(resp["response"]["data"]["cardano"]["tip"]["number"])
                self._set_height_error(height=height)
                if not self.service_status.error_code:
                    self.service_status = ServiceStatus(height=height)
            except (KeyError, ValueError) as ex:
                self._set_response_error(ex.__str__())
