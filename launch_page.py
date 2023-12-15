import gradio as gr
import landing_page

with gr.Blocks(theme=landing_page.Custom()) as demo:
    landing_page.renderDesign()  # Rendering the landing page

demo.launch()  # Launch the demo
