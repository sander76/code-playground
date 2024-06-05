from textual import on
from textual.app import App, ComposeResult
from textual.events import Resize, Show
from textual.widget import Widget
from textual.widgets import Input, Label, Static


class MyInput(Static):
    DEFAULT_CSS = """
    #myinput {
        height: 1;
        border: none;
        
    }
    """

    def compose(self):
        yield Input(id="myinput")
        yield Label()

    @on(Resize)
    def on_input_resize(self, message: Resize):
        my_width = message.size.width
        chars = "▔" * my_width
        self.query_one(Label).update(chars)


class MyApp(App):
    CSS_PATH = "myapp.tcss"

    def compose(self):
        yield MyInput()


if __name__ == "__main__":
    app = MyApp()
    app.run()
