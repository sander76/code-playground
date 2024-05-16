from pydantic import BaseModel


class SubCommandOne(BaseModel):
    name: str


class SubCommandTwo(BaseModel):
    name: str


class ModelWithSubcommand(BaseModel):
    sub_command: SubCommandOne | SubCommandTwo

    class Config:
        smart_union = True


# Prints `SubcommandOne`.
print(
    ModelWithSubcommand(
        sub_command=SubCommandTwo(name="myname"),
    )
)
