from pydantic import BaseModel
from cat import plugin


class MySettings(BaseModel):
    number_of_results: int = 10


@plugin
def settings_schema():
    return MySettings.schema()
