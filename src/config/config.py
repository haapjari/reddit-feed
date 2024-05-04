import os
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def get(val: str) -> str:
        """
        Get the value of the environment variable with the given key.
        """
        env_key = val.upper()

        key: str | None = os.getenv(env_key)
        if key == None:
            return ""
        else:
            return key
