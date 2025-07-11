from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

import gradio as gr

# === MODEL ===
model = ChatGroq(
    temperature=1,
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

# === PROMPTS ===
prompt_1 = PromptTemplate(
    template="Generate a short and simple notes on the given text:\n{text}",
    input_variables=["text"]
)

prompt_2 = PromptTemplate(
    template="Generate a quiz of 5 short yes/no questions on the given text:\n{text}",
    input_variables=["text"]
)

prompt_3 = PromptTemplate(
    template="Merge the following notes and quiz into a single document:\n\nNotes:\n{notes}\n\nQuiz:\n{quiz}",
    input_variables=["notes", "quiz"]
)

# === PARSER ===
parser = StrOutputParser()

# === CHAINS ===
parallel_chain = RunnableParallel({
    "notes": prompt_1 | model | parser,
    "quiz": prompt_2 | model | parser
})

chain = prompt_3 | model | parser

merged_chain = parallel_chain | chain

# === FUNCTION ===
def generate_output(text):
    return merged_chain.invoke({"text": text})

# === SIMPLE GRADIO UI ===
gr.Interface(
    fn=generate_output,
    inputs=gr.Textbox(lines=12, label="Input Text"),
    outputs=gr.Textbox(lines=20, label="Output"),
).launch()
