import gradio as gr
from landing_page import Custom, Landing_Page


with gr.Blocks(theme=Custom()) as demo:
    landingPage = Landing_Page()
    landingPage.renderDesign()
  
demo.launch()