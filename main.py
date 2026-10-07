from dotenv import load_dotenv

load_dotenv()

import os
# from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI

# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
