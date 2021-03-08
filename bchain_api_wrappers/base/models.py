from pydantic import BaseModel, create_model
from typing import Optional, Dict


class ServiceStatus(BaseModel):
    height: Optional[int] = -1
    peers_count: Optional[int] = -1
    error_code: Optional[int] = 0
    error_message: Optional[str] = ""
    additional_params: Optional[list] = []
