from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal 

model = ChatGroq(
    temperature=1,
    groq_api_key="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",
    model_name="meta-llama/llama-4-scout-17b-16e-instruct"
)

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal["Positive", "Negative"] = Field(description="The sentiment of the feedback")

parser_2 = PydanticOutputParser(pydantic_object=Feedback)

prompt_1 = PromptTemplate(
    template = "classify the following feedback text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables = ["feedback"],
    partial_variables = {"format_instructions": parser_2.get_format_instructions()}
)

classifier_chain = prompt_1 | model | parser_2

prompt_2 = PromptTemplate(
    template = "write an appropriate response to the following Positive feedback text \n {feedback}",
    input_variables = ["feedback"]
)

prompt_3 = PromptTemplate(
    template = "write an appropriate response to the following Negative feedback text \n {feedback}",
    input_variables = ["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt_2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt_3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback": "I kinda like it : )"}))

chain.get_graph().print_ascii()
