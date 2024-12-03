from pydantic import SecretStr
from pydantic_settings import BaseSettings
from typing import Optional

class HORSE_INFO(BaseSettings):

    NAME : str = "mock_horses1_url"
    AGE : str = "mock_horses2_url"
    COLOR : str = "brown"
    RACE : str = "purasangre"


if __name__ == "__main__":
    config = HORSE_INFO()
    
    print(config.NAME)
    config.NAME="eje"
    print(config.NAME)
