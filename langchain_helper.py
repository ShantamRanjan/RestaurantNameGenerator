import os
import getpass
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_perplexity import ChatPerplexity
from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain
# Ensure OPENAI_API_KEY is set for compatibility
if "OPENAI_API_KEY" not in os.environ:
	os.environ["OPENAI_API_KEY"] = os.environ.get("PERPLEXITY_API_KEY", "")


llm = ChatPerplexity(temperature=0.7)
def generate_restaurant_name_and_item(cuisine):
    prompt = PromptTemplate(
    input_variables=["cuisine"],
    template="I want open a {cuisine} restaurant . suggest me a some fancy names for it.Give only one name and show only the name without any other text or explanation.",
)
    chain = LLMChain(llm=llm, prompt=prompt, output_key="Restaurant name")
    chain.invoke({"indian"})

    prompt_items = PromptTemplate(
    input_variables=["Restaurant name"],
    template="""Suggest some menu items for {Restaurant name}.Return it as a comma separated list.Just return the list without any explanation. """,
)
    food_items_name = LLMChain(llm=llm, prompt=prompt_items, output_key="Menu items")
    chain = SequentialChain(
    chains = [chain, food_items_name],
    input_variables=['cuisine'],
    output_variables=['Restaurant name', 'Menu items'],
)
    response = chain({'cuisine': cuisine})

    return response 

if __name__ == "__main__":
    print(generate_restaurant_name_and_item("Indian"))