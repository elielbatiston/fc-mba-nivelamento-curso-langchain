1- Configurar ambiente

a-) Criar o ambiente

```
python3 -m venv venv
```

b-) Ativar o ambiente

```
source venv/bin/activate
```

c-) instalar as dependencias

```
pip install langchain langchain-openai langchain-google-genai python-dotenv beautifulsoup4 pypdf
```

d-) Gerar o requirements.txt

```
pip freeze > requirements.txt
```

2- Gerar api 

a-) No google acesse o "api key google studio"

```
https://aistudio.google.com/apps
```

Clique em "get api key" (Precisa de uma conta e projeto no google cloud platform)

b-) No chatgpt acesse

```
https://platform.openai.com/api-keys
```

Clique em API Keys


