
"""
This will handle the Editor window redering content 
the content will be passed through
"""


from prompt_toolkit.layout import UIContent,UIControl,Window,Layout
from typing import List,Tuple,Any
from prompt_toolkit.application import Application


class Editor(UIControl):
    def __init__(self,lines):
        self.lines = lines
    def create_content(self, width, height):
        def get_line(idx:int) -> List[Tuple[str,Any]]: 
            return [("",self.lines[idx])]
        return UIContent(get_line=get_line,line_count=len(self.lines))


if __name__ == "__main__": 
    lines: List[str] = [
    "Hello, world! This is a standard test line with punctuation.",
    "def calculate_sum(a, b): return a + b  # Code snippet test line",
    "1234567890 !@#$%^&*()_+ Numbers, symbols, and special characters",
    "Unicode & Emoji test: 🚀 Café, naïve, résumé, 🌟"
    ]


    win = Window(Editor(lines))

    editor_layout = Layout(win)

    from prompt_toolkit.key_binding import KeyBindings
    kb = KeyBindings()
    @kb.add("c-q")
    @kb.add('q')
    def _(event):
        event.app.exit()

    app = Application(layout=editor_layout,full_screen=True,key_bindings=kb)
    app.run()
