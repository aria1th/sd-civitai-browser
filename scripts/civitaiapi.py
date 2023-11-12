import gradio as gr
from modules import script_callbacks

def on_ui_tabs_called():
    with gr.Blocks() as script_civitai_interface:
        with gr.Tab("CivitAi-Browser"):
            # dummy
            gr.Label("CivitAi-Browser")
    return (script_civitai_interface, "CivitAi", "civitai-interface"),

script_callbacks.on_ui_tabs(on_ui_tabs_called)