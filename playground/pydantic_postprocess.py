import asyncio
import pydantic
from pydantic import BaseModel
from dataclasses import dataclass


def with_post_processor(cls):
    # class WrapperClass(cls):
    #     postprocessing: list[str] = []

    #     def json(*args, **kwargs):
    #         super().json

    def _wrapped(*args, **kwargs):
        # instance = WrapperClass(*args, **kwargs)
        # return instance
        instance = cls(*args, **kwargs)
        old_json = instance.json

        def json(*args, **kwargs):
            if "exclude" not in kwargs:
                kwargs["exclude"] = set()
            kwargs["exclude"].add("postprocessing")
            kwargs["exclude"].add("json")
            return old_json(*args, **kwargs)
            # self.super_json(self, *args, **kwargs)

        instance.__dict__["postprocessing"] = []

        # instance.__dict__["super_json"] = instance.json
        instance.__dict__["json"] = json
        return instance

    return _wrapped


# @with_post_processor
class SomeModel(BaseModel):
    value: int
    name: str


class SomeModelWithPostProcessor(SomeModel):
    pass


async def long_runner(value: int):
    await asyncio.sleep(1)
    return value * 3


def attr_setter(object, property, args):
    async def go():
        value = await long_runner(*args)
        setattr(object, property, value)

    return go


somemodel = SomeModel(value=2, name="sander")

# somemodel.postprocessing = [attr_setter(somemodel, "value", (2,))]

# somemodel.__dict__["postprocessing"] = [attr_setter(somemodel, "value", (2,))]
# setattr(somemodel, "postprocessing", [attr_setter(somemodel, "value", (2,))])
somemodel.postprocessing.append(attr_setter(somemodel, "value", (2,)))


async def postprocess(a_model):
    for postprocess in a_model.postprocessing:
        await postprocess()


asyncio.run(postprocess(somemodel))
print(somemodel.json())
