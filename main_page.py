# This module is created for the layout of the main page

import time
import gradio as gr
import constants


def respond(message, chat_history):  # A function for the chatbot, so the chatbot can reply the message
    botMessage = constants.automaticAnswer(message)  # Calling the function in constants to create an automatic respond
    chat_history.append((message, botMessage))  # Display the dialogue on the chat panel
    time.sleep(2)  # Create a small delay
    return chat_history


def render():  # Render the main page
    firstRow = gr.Row(visible=False)  # It will be invisible if the landing page is still on display
    with firstRow:  # In the first row
        chatbot = gr.Chatbot(height=680)  # Creating the chat panel and bot
    secondRow = gr.Row(visible=False)  # It will be invisible if the landing page is still on display
    with secondRow:  # In the second row
        with gr.Column():  # Make the components stacked under the chat panel
            with gr.Row(): # Make the components side by side
                chooseResp = gr.Dropdown(choices=constants.QUESTIONS, interactive=True, show_label=False,
                                         container=False, )  # User prompted reply
                submitButton = gr.Button("Submit", interactive=True, variant='primary', scale=0, )  # Submit button
                clearButton = gr.ClearButton([chooseResp, chatbot], scale=0, variant='primary')  # Clear button
                submitButton.click(fn=respond, inputs=[chooseResp, chatbot], outputs=chatbot)  # Event listener if the
                # button is clicked

    return firstRow, secondRow
