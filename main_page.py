
import gradio as gr
import random

class MainPage():
    def render(self):
        column = gr.Column(visible=False,)
        with column:
            hello = gr.Markdown(
                "<br> <br> <br><br> <br><h1 style='text-align: center; margin-bottom: 1rem'> <font size='36'>🤖  <br> Hello! </font></h1> ")
        return column
