
import gradio as gr

def summarize(text):
    if not text:
        return "Please enter some text."
    sentences = text.split('.')
    short = sentences[0] if sentences else text
    return "Summary: " + short.strip()

with gr.Blocks() as demo:
    gr.Markdown("## AI Text Summarizer API")
    inp = gr.Textbox(label="Enter Text")
    out = gr.Textbox(label="Summary")
    inp.change(fn=summarize, inputs=inp, outputs=out)

demo.launch(server_name="0.0.0.0", server_port=7860)
