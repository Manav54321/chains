# LangChain Chains

This repository demonstrates how to use Chains in LangChain to build modular AI pipelines.

## What are Chains?

In LangChain, a Chain is a sequence of components connected together to perform a task. Each component in the chain does one job, and the output of one step becomes the input of the next.

For example:
Prompt → LLM → Output Parser

LangChain chains help break down tasks into manageable steps. You can combine models, prompts, tools, and logic using chains to create flexible AI applications.

## How This Works

This project uses LangChain's `Runnable` interfaces to build a conditional chain. Here's what it does:

1. Takes a feedback text input.
2. Uses a prompt and LLM to classify the feedback as Positive or Negative.
3. Parses the classification using a Pydantic model.
4. Based on the sentiment, routes the input to different prompts to generate an appropriate response.
5. Returns the final response.

The routing logic is handled using `RunnableBranch`, which acts like an if-else statement.

## Key Components Used

- `PromptTemplate`: To define prompt templates for the classifier and response generator.
- `ChatGroq`: LLM wrapper for making API calls to Groq-hosted LLMs.
- `PydanticOutputParser`: To parse the output of the model into structured format.
- `RunnableBranch`: For conditional logic based on sentiment.
- `RunnableLambda`: For simple transformations inside chains.

## Example Use Case

Input:
"I love the new features in the app, they are amazing."

Step-by-step flow:
1. Classify sentiment → Positive
2. Choose the positive response prompt
3. Generate and return the appropriate reply

## Why Use Chains

- Clear and modular code
- Easier debugging and testing
- Scalable logic using simple building blocks
- Useful for tasks like routing, classification, tool use, and complex workflows
