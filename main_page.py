import gradio as gr

from Globals import Globals

NAME = Globals("No")

class MainPage:

    def render(self):
        firstRow = gr.Row(visible=False)
        with firstRow:
            chatbot = gr.Chatbot()
        return firstRow


