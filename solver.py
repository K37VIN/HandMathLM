from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain

llm=Ollama(model="mistral")

template="""

You are a math expert proficient in solving math problems.Solve and provide only the final answer to the problems

Problem: {equation}
"""

prompt=PromptTemplate(input_variables=["equation"],template=template)
llm=Ollama(model="mistral")
chain=LLMChain(llm=llm,prompt=prompt)

def solve_equation_text(equation_text):
    return chain.run(equation_text)