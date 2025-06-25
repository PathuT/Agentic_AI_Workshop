from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate

class RAGAgent:
    def __init__(self, vectorstore_path: str, google_api_key: str):
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=google_api_key
        )

        # ✅ Safe if you're loading your own FAISS index
        self.vectorstore = FAISS.load_local(
            folder_path=vectorstore_path,
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            google_api_key=google_api_key
        )

        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
            Use the following context to answer the user's question:

            {context}

            Question:
            {question}

            Answer:
            """
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vectorstore.as_retriever(),
            return_source_documents=False,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def run(self, query: str) -> str:
        return self.qa_chain.run(query)
