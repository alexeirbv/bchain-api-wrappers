import asyncio
import json
import aiohttp
import async_timeout
from base.config import AdapterError, HTTP_TIMEOUT_S
from urllib3 import disable_warnings, exceptions
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from base.models import ServiceStatus
from typing import List, Dict, Tuple
from python_graphql_client import GraphqlClient


class AbstractAdapter:
    def __init__(self, url: str, coin: str,
                 credentials: Tuple = ("", ""), family: str = "", **kwargs):
        self.url = str(url)
        self.coin = str(coin).upper()
        self.credentials = aiohttp.BasicAuth(*credentials)
        self.is_provider = None
        self.service_status = ServiceStatus()
        if not family:
            self.family = self.coin
        else:
            self.family = family

        for k, v in kwargs.items():
            setattr(self, k, v)

    async def get_status(self) -> ServiceStatus:
        return NotImplementedError

    def _set_height_error(self, height):
        if height <= 0:
            self.service_status = ServiceStatus(
                error_code=AdapterError.INSTANCE_ZERO_HEIGHT.value,
                error_message=f"Height {height} is not valid"
            )

    def _set_response_error(self, ex):
        self.service_status = ServiceStatus(
            error_code=AdapterError.RESPONSE_PARSE_ERROR.value,
            error_message=f"Can't parse reponse: {ex}"
        )

    async def _send_http_request(self, url, url_params="", body="", method="GET", parse_json=True,
                                 http_headers=None, set_error=True) -> Dict:
        try:
            if not http_headers:
                http_headers = {}
            software_names = [SoftwareName.CHROME.value]
            operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
            user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems,
                                           limit=100)

            print("Sending request to " + url)

            # Cause of self-signed or expired TLS certs
            disable_warnings(exceptions.InsecureRequestWarning)

            headers = {
                "User-Agent": user_agent_rotator.get_random_user_agent(),
                "Content-Type": "application/json",
                **http_headers
            }

            with async_timeout.timeout(HTTP_TIMEOUT_S):
                async with aiohttp.ClientSession() as session:
                    async with session.request(url=url + url_params, method=method,
                                               data=body, headers=headers, auth=self.credentials) as response:
                        response_data = await response.text()
                        response.raise_for_status()
                        await session.close()
            return {"success": True, "response": json.loads(response_data)} if parse_json \
                else {"success": True, "response": response_data}
        except (aiohttp.ClientError, asyncio.exceptions.TimeoutError, json.decoder.JSONDecodeError) as ex:
            if set_error:
                self.service_status = ServiceStatus(
                    error_code=AdapterError.HTTP_ERROR.value,
                    error_message=ex.__str__()
                )
            return {"success": False, "error": ex.__str__()}

    async def _send_graphql_request(self, url: str, query: str, set_error=True) -> Dict:
        try:
            client = GraphqlClient(endpoint=url)
            response_data = await client.execute_async(query=query)
            return {"success": True, "response": response_data}
        except aiohttp.ClientError as ex:
            if set_error:
                self.service_status = ServiceStatus(
                    error_code=AdapterError.HTTP_ERROR.value,
                    error_message=ex.__str__()
                )
            return {"success": False, "error": ex.__str__()}
