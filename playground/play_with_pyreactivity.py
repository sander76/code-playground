from reactivity import ref, watch, watch_effect
import gc
import time


class Controller:
    def __init__(self) -> None:
        self.value = ref(10)


class View:
    def __init__(self, controller: Controller) -> None:
        self._controller = controller
        self._watch = watch(self._controller.value, self._value_changed)

    def _value_changed(self, new_value):
        print(new_value)

    def unwatch(self):
        self._watch()


if __name__ == "__main__":
    controller = Controller()
    view = View(controller)
    obj = view
    controller.value.value = 20
    referers = gc.get_referrers(view)
    for refer in referers:
        print(refer)
    print(len(gc.get_referrers(view)))

    view.unwatch()
    for i in range(10):
        time.sleep(1)

        referers = gc.get_referrers(view)
        for referer in referers:
            print(refer)
        print(len(gc.get_referrers(view)))
