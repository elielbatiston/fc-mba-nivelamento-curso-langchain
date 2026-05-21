from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
load_dotenv()

long_text = """
Dawn threads a pale gold through the alley of glass.
The city yawns in a chorus of brakes and distant sirens.
Windows blink awake, one by one, like sleepy eyes.
Streetcloth of steam curls from manholes, a quiet river.
Coffee steam spirals above a newspaper's pale print.
Pedestrians sketch light on sidewalks, hurried, loud with umbrellas.
Buses swallow the morning with their loud yawns.
A sparrow perches on a steel beam, surveying the grid.
The subway sighs somewhere underground, a heartbeat rising.
Neon still glows in the corners where night refused to retire.
A cyclist cuts through the chorus, bright with chrome and momentum.
The city clears its throat, the air turning a little less electric.
Shoes hiss on concrete, a thousand small verbs of arriving.
Dawn keeps its promises in the quiet rhythm of a waking metropolis.
The morning light cascades through towering windows of steel and glass,
casting geometric shadows on busy streets below.
Traffic flows like rivers of metal and light,
while pedestrians weave through crosswalks with purpose.
Coffee shops exhale warmth and the aroma of fresh bread,
as commuters clutch their cups like talismans against the cold.
Street vendors call out in a symphony of languages,
their voices mixing with the distant hum of construction.
Pigeons dance between the feet of hurried workers,
finding crumbs of breakfast pastries on concrete sidewalks.
The city breathes in rhythm with a million heartbeats,
each person carrying dreams and deadlines in equal measure.
Skyscrapers reach toward clouds that drift like cotton,
while far below, subway trains rumble through tunnels.
This urban orchestra plays from dawn until dusk,
a endless song of ambition, struggle, and hope.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250, chunk_overlap=70, 
)

parts = splitter.create_documents([long_text])

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

#####
# chain_type="stuff" é o tipo mais simples de sumarização, onde o modelo recebe todo o texto de uma vez e gera um resumo.
# Supondo que eu tenha um livro que tem diversos capitulos com muito conteudo. Quando usa o chain_type="stuff",  
# quando vc preenche algo, você pega alguma coisa e coloca na sua janela de contexto. Se o documento é muito grande e
# eu coloque na janela de contexto talvez eu encha a janela de contexto.
# Imagine tbm que o capitulo 1 é maior que o 2 e 3, quando eu uso o chain_type="stuff" e peço pra gerar um resumo, 
# o modelo pode ter o comportamento de trazer mais informações do capilo 1 do que dos outros capitulos. 
# Pode ser que fique desequilibrado.
# Se eu tenho muito documento, não vai caber eu fazer uma sumarização com tanta coisa grande assim e é ai que entra o 
# map_reduce
#
#
# chain_type="map_reduce" é um tipo mais avançado, onde o modelo primeiro gera resumos parciais de cada parte do texto 
# e depois combina esses resumos para gerar um resumo
# Ele faz um resumo por capitulo e depois ele faz o resumo do resumo dos capitulos.
# O problema é que ele faz uma chamada para cada parte do texto e com isso gasta mais.
#####

# verbose=True é para mostrar o que está acontecendo nos bastidores, ou seja, quais chamadas estão sendo feitas para o modelo
# e depois ele mostra o resultado final.
#
# já com verbose=False ele não mostra nada, ele só mostra o resultado final, ou seja, o resumo gerado pelo modelo.

chain_sumarize = load_summarize_chain(llm, chain_type="map_reduce", verbose=True)
# chain_sumarize = load_summarize_chain(llm, chain_type="map_reduce", verbose=True, prompt=PROMPT) 
# eu tenho a opção de passar o prompt template colocando o parametro prompt conforme acima
# Assim, eu posso customizar no load_summarize_chain o prompt template que eu quero usar. Eu não fico preso aquele prompt inicial (prompt padrao) write, aconcize, etc 


result = chain_sumarize.invoke({"input_documents": parts})
print(result)
