"""
Handels the status bar
"""

from prompt_toolkit.layout import UIContent,UIControl,Window,Layout
from typing import List,Tuple,Any
from prompt_toolkit.application import Application


class StatusBar(UIControl):

    def __init__(self,mode):
        self.mode = mode

    def create_content(self, width, height):
        left_text = f"--{self.mode}--"
        right_text = f"Size:{width}X{height}"
        padding_len = max(0,width-len(right_text)-len(left_text))
        formatted_text = left_text+" "*padding_len+right_text

        def get_line(idx:int) -> List[Tuple[str,Any]]: 
            return [("",formatted_text)]

        return UIContent(get_line=get_line,line_count=1)


if __name__ == "__main__": 
    lines: List[str] = [
    "Hello, world! This is a standard test line with punctuation.",
    "def calculate_sum(a, b): return a + b  # Code snippet test line",
    "1234567890 !@#$%^&*()_+ Numbers, symbols, and special characters",
    "Unicode & Emoji test: 🚀 Café, naïve, résumé, 🌟"
    ]

    mode = "Normal"
    win = Window(StatusBar(mode))

    editor_layout = Layout(win)

    from prompt_toolkit.key_binding import KeyBindings
    kb = KeyBindings()
    @kb.add("c-q")
    @kb.add('q')
    def _(event):
        event.app.exit()

    app = Application(layout=editor_layout,full_screen=True,key_bindings=kb)
    app.run()

