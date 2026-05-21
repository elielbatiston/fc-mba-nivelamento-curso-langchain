from langchain.prompts import PromptTemplate 

template = PromptTemplate(
    input_variables=["name", "age"],
    template="Hi, I'm {name} and I'm {age} years old! Tell me a joke with my name!"
)

text = template.format(name="Eliel", age=46)
print(text)
