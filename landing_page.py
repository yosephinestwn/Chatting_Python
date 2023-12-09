from __future__ import annotations
from typing import Iterable
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
from main_page import MainPage


class Custom(Base):
    def __init__(
            self,
            *,
            primary_hue: colors.Color | str = colors.red,
            secondary_hue: colors.Color | str = colors.gray,
            neutral_hue: colors.Color | str = colors.purple,
            spacing_size: sizes.Size | str = sizes.spacing_lg,
            radius_size: sizes.Size | str = sizes.radius_md,
            text_size: sizes.Size | str = sizes.text_lg,
            font: fonts.Font
                  | str
                  | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("Quicksand"),
                    "ui-sans-serif",
                    "sans-serif",
            ),
            font_mono: fonts.Font
                       | str
                       | Iterable[fonts.Font | str] = (
                    fonts.GoogleFont("IBM Plex Mono"),
                    "ui-monospace",
                    "monospace",
            ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            body_background_fill="linear-gradient(#5680E9, #84ceeb, #5ab9ea, #c1c8e4,#8860d0)",
            body_background_fill_dark="linear-gradient(#5680E9, #84ceeb, #5ab9ea, #c1c8e4,#8860d0)",
            button_primary_background_fill="radial-gradient(#5680E9, #8860d0)",
            button_primary_background_fill_hover="radial-gradient(#5680E9, #8860d0)",
            button_primary_text_color="white",
            button_primary_background_fill_dark="radial-gradient(#5680E9, #8860d0)",
            slider_color_dark="radial-gradient(#5680E9, #8860d0)",
            block_title_text_weight="600",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )


class Landing_Page:


    def renderDesign(self):
        mainPage = MainPage()
        firstRow = gr.Row()
        with firstRow:
            with gr.Column():
                hello = gr.Markdown(
                    "<br> <br> <br><br> <br><h1 style='text-align: center; margin-bottom: 1rem'> <font size='36'>🤖  <br> "
                    "Hello! Please put your name down below so we can know you</font></h1> ", )
                warning = gr.Markdown(
                    "<br> <br> <br><br> <br><h1 style='text-align: center; margin-bottom: 1rem'> <font size='36'>🤖  <br> "
                    "Hello! Please put your name down below so we can know you</font></h1> ", visible=False, )

        secondRow = gr.Row()
        with secondRow:
            input_text = gr.Textbox(placeholder="Please put your name here", interactive=True, show_label=False,
                                    container=False, )
            start_chatting = gr.Button("Start Chatting", interactive=True, variant='primary', scale=0, )

        thirdRow = gr.Row(visible=False)
        with thirdRow:
            hello = gr.Markdown()
        fourthRow = mainPage.render()
        start_chatting.click(fn=self.saveUserName, inputs=input_text, outputs=[warning, firstRow, secondRow, thirdRow, fourthRow, hello])

    def saveUserName(self, a):
        if not a:
            markdown = gr.Markdown(
                "<h1 style='text-align: center; margin-bottom: 1rem'> 🤖 Hello, " + a + " </font></h1> ")
            return gr.update(visible=True), gr.update(visible=True), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False), markdown
        else:
            markdown = gr.Markdown(
                "<h1 style='text-align: center; margin-bottom: 1rem'> 🤖 Hello, " + a + " </font></h1> ")
            return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(visible=True), gr.update(visible=True), markdown


