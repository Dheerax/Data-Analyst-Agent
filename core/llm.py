from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from os import getenv

load_dotenv()

def get_llm(model: str = "gemini-1.5-flash", temperature: float = 0.1):
    llm = ChatGoogleGenerativeAI(
        model=model,
        temperature=temperature,
        convert_system_message_to_human=True,
        google_api_key=getenv('GOOGLE_API_KEY')
    )

    return llm
