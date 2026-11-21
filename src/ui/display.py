"""
Goal is to have the tui for the editor mode
for now the keybinding are implemented here
later need to move that to the input -> key_handler.py
"""

from prompt_toolkit.layout import Layout,Window,HSplit,VSplit,FormattedTextControl
from prompt_toolkit import Application
from prompt_toolkit.layout.controls import UIContent,UIControl
from typing import Any,Tuple




class Editor(UIControl):
    def __init__(self,lines):
        self.lines = lines
        self.lenght = len(self.lines)

    def create_content(self, width, height) -> UIContent:
        def get_line(idx:int) -> list[Tuple[str,Any]]:
            return [("",self.lines[idx])]
        return UIContent(get_line=get_line,line_count=len(self.lenght))
     
class StatusBar(UIControl):
    """
    It handels the text rendering of the status bar """
    def __init__(self,state,lines):
        self.state = state['Mode']
        self.lines = lines
    def create_content(self, width, height):
        def get_line(idx:int) -> list[Tuple[str,Any]]:
            return [("",f"file Name:{self.lines}")]
        return UIContent(get_line=get_line,line_count=len,show_cursor=False)


if __name__ == "__main__":
    from prompt_toolkit.key_binding import KeyBindings
    #from prompt_toolkit.filters import Condition
    state = {"filename":"test.txt","Mode":"Normal"}
    FileName = state['filename']

    #class KeyHandler
    kb = KeyBindings() 
    #status = {"mode":"normal"}

    #is_normal = Condition(lambda: status["mode"] == 'normal' )

    @kb.add(':','q') #can add filter 
    def _(event) :
        event.app.exit()

    lines = [f"lines for the test line cnt: {i+1}" for i in range(100)]
    editor_win = Window(Editor(lines,state)) 
    status_bar = Window(StatusBar(FileName,state['Mode']))

    app = Application()
    app.run()