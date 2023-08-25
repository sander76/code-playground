from pydantic import Field


class Switch:
    """Switch"""

    normal_open: bool | None = Field(None, title="normalOpen", alias="normalOpen")

    open: bool | None = Field(None, title="open")

    class Config:
        title = "Switch"


class StrictSwitch(Switch):
    open: bool
