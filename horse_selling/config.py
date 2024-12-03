from pydantic import SecretStr
from pydantic_settings import BaseSettings
from typing import Optional

class HORSE_INFO(BaseSettings):

    NAME : str = "mock_horses1_url"
    AGE : str = "mock_horses2_url"
    COLOR : str = "brown"
    RACE : str = "purasangre"


if __name__ == "__main__":
    config = PAGEINFO()
    print(config.DRIVERPATH.get_secret_value())
    print(config.HORSES1_URL)
