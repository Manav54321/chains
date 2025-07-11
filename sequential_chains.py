from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGroq(
    temperature = 1,
    groq_api_key = "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",
    model_name = "meta-llama/llama-4-scout-17b-16e-instruct"
)

prompt_1 = PromptTemplate(
    template= "Generate a detailed report on {topic}",
    input_variables = ["topic"]
)

prompt_2 = PromptTemplate(
    template= "Summarize the report on {text} in 3 bullet points",
    input_variables = ["text"]
)

parser = StrOutputParser()

chain = prompt_1 | model | parser | prompt_2 | model | parser

result = chain.invoke({"topic": "Travis Scott"})

print(result)

chain.get_graph().print_ascii()