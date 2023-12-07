import gradio as gr
import random


class MainPage():
    def render(self):
        from launch_page import Landing_Page
        landingPage = Landing_Page()
        column = gr.Column(visible=False, )
        with column:
            hello = gr.Markdown(
                "<h1 style='text-align: center; margin-bottom: 1rem'> 🤖 Hello, " + landingPage.name + " </font></h1> ")
            chatbot = gr.Chatbot()

        return column
