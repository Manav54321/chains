from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGroq(
    temperature = 1,
    model_name = "meta-llama/llama-4-scout-17b-16e-instruct"
)

prompt = PromptTemplate(
    template = "Generate a 3 mindbending facts about {topic}",
    input_variables = ["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser
# LCEL = langchain expression language

result = chain.invoke({"topic": "Margot Robbie"})

print(result)

chain.get_graph().print_ascii()