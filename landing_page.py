# This module is created for the landing page

from __future__ import annotations
from typing import Iterable
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes
import main_page


class Custom(Base):  # A class for custom theme for the app
    def __init__(
            self,
            *,
            primary_hue: colors.Color | str = colors.gray,
            secondary_hue: colors.Color | str = colors.gray,
            neutral_hue: colors.Color | str = colors.gray,
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
            body_background_fill="linear-gradient(#988558, #C19A6B,#C2B280)",  # Background light mode
            body_background_fill_dark="linear-gradient(#080402, #0d0907, #28231d)",  # Background dark mode
            button_primary_background_fill="radial-gradient(#3f3a2b, #433f2e)",
            button_primary_background_fill_hover="radial-gradient(#2b281d, #302d21)",
            button_primary_text_color="white",
            button_primary_background_fill_dark="radial-gradient(#3f3a2b, #433f2e)",
            button_primary_background_fill_hover_dark="radial-gradient(#2b281d, #302d21)",
            slider_color="radial-gradient(#3f3a2b, #433f2e)",
            slider_color_dark="radial-gradient(#3f3a2b, #433f2e)",
            block_title_text_weight="600",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )


def saveUserName(a):  # Function to save the username (for the input)
    if not a:  # If the user does not give the input, then display a warning text
        markdown = gr.Markdown(
            "<h1 style='text-align: center; margin-bottom: 1rem'><font size='20'> 🤖 Hello, User!</font></h1> ")
        return gr.update(visible=True), gr.update(visible=True), gr.update(visible=True), gr.update(visible=False), \
            gr.update(visible=False), gr.update(visible=False), markdown
    else:  # Otherwise, display the main page and display the username on the main page
        markdown = gr.Markdown(
            "<h1 style='text-align: center; margin-bottom: 1rem'>Hello, " + a + "! <br> "
                                                                                "You can now use "
                                                                                "the chatbot. Have "
                                                                                "fun!</h1> ")
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False), gr.update(
            visible=True), \
            gr.update(visible=True), gr.update(visible=True), markdown


def renderDesign():
    firstRow = gr.Row()  # Visible when the landing page is active, invisible when the main page is active
    with firstRow:
        with gr.Column():  # Stack the components vertically
            hello = gr.Markdown(
                "<br> <br> <br><br> <br><h1 style='text-align: center; margin-bottom: 1rem'> <font size='36'>🤖  <br> "
                "Hello! Please put your name down below so we can know you</font></h1> ", )  # Hello message
            warning = gr.Markdown("<h1 style='text-align: center; margin-bottom: 1rem'><span "
                                  "style='color:red'> Please enter your name "
                                  "</span></h1><br>",
                                  visible=False, )  # Warning message

    secondRow = gr.Row()
    with secondRow:  # Make the components side by side
        input_text = gr.Textbox(placeholder="Please put your name here", interactive=True, show_label=False,
                                container=False, max_lines=1)  # Input field for the username
        start_chatting = gr.Button("Start Chatting", interactive=True, variant='primary',
                                   scale=0, )  # Start chatting button

    thirdRow = gr.Row(visible=False)  # It will be invisible if the landing page is still on display
    with thirdRow:
        hidden = gr.Markdown()  # Placeholder for the hello markdown for the main page
    hiddenPage = main_page.render()  # Rendering the layout of the main page
    fourthRow = hiddenPage[0]
    fifthRow = hiddenPage[1]
    # Event listener for the start chatting button if the button is clicked
    start_chatting.click(fn=saveUserName, inputs=input_text, outputs=[warning, firstRow, secondRow, thirdRow,
                                                                      fourthRow, fifthRow, hidden])
