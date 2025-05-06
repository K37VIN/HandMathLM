# HandMathLM: Handwritten Text-2-Math Solver ✍️

HandMathLM is a Handwritten Text-2-Math Solver that can convert handwritten mathematical expressions into latex format.This latex format of the expressions is then passed on to a Large Language Model which upon analysing the latex format of the expression, generates the solution to the mathematical problem.The Large Language Model used is Ollama,an open source LLM,and Mistral as the model.

## Tech Stack:

- Python(https://www.python.org)
- MyScript Web Demo (for the canvas) (https://webdemo.myscript.com/views/math/index.html)
- Ollama (https://github.com/ollama/ollama)
- Langchain(https://python.langchain.com)
- Streamlit(https://streamlit.io)

To clone this repository,run the command:

```
git clone https://github.com/K37VIN/HandMathLM.git
```

You need to install the required libraries by running the following command:

```
pip install -r requirements.txt
```

To run the application,run the following command:

```
streamlit run app.py
```
