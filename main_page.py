import time
import gradio as gr
import constants


def respond(message, chat_history):
    botMessage = constants.automaticAnswer(message)
    chat_history.append((message, botMessage))
    time.sleep(2)
    return chat_history


def render():
    firstRow = gr.Row(visible=False)
    with firstRow:
        chatbot = gr.Chatbot(height=680)
    secondRow = gr.Row(visible=False)
    with secondRow:
        with gr.Column():
            with gr.Row():
                chooseResp = gr.Dropdown(choices=constants.QUESTIONS, interactive=True, show_label=False,
                                         container=False, )
                submitButton = gr.Button("Submit", interactive=True, variant='primary', scale=0, )
                clearButton = gr.ClearButton([chooseResp, chatbot],scale=0,variant='primary')
                submitButton.click(fn=respond, inputs=[chooseResp, chatbot], outputs=chatbot)

    return firstRow, secondRow



