from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
import warnings
warnings.filterwarnings("ignore")

llm = Ollama(model="llama3.2")

def generate_res(cuisine):
    prompt_temp_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = "I want to open a {cuisine} food restraunt, generate a name for it. Print only the name")
    name_chain = LLMChain(llm = llm, prompt= prompt_temp_name, output_key= "restaurant_name")

    prompt_temp_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest some menu items for {restaurant_name}, give the output in comma seprated list")
    items_chain = LLMChain(llm = llm, prompt= prompt_temp_items, output_key= "menu_items")

    chain = SequentialChain(chains= [name_chain, items_chain],
                           input_variables = ['cuisine'],
                           output_variables = ['restaurant_name', 'menu_items'])
    result = chain.invoke({'cuisine': 'Indian'})
    return result

if( __name__== "__main__"):
    print(generate_res("Italiano"))
