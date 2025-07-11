from pytest import MonkeyPatch


class MyModel:
    def to_patch():
        return 2


def test_my_model(monkeypatch: MonkeyPatch):
    # org = MyModel.to_patch

    def with_org(callable):
        def wrapped(self, *args, **kwargs):
            return 2 * callable(*args, **kwargs)

        return wrapped

    monkeypatch.setattr(MyModel, "to_patch", with_org(MyModel.to_patch))

    result = MyModel().to_patch()
    assert result == 4
