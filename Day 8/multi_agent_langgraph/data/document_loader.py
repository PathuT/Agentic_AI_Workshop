from langchain.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader

def load_documents(data_folder: str, file_types=None):
    """
    Load documents from the given folder with specified file types.
    file_types example: ["*.txt", "*.pdf"]
    """
    if file_types is None:
        file_types = ["*.txt", "*.pdf"]  # default load text and pdf files

    loaders = []
    for file_type in file_types:
        if file_type.endswith("txt"):
            loaders.append(DirectoryLoader(data_folder, glob=file_type, loader_cls=TextLoader))
        elif file_type.endswith("pdf"):
            loaders.append(DirectoryLoader(data_folder, glob=file_type, loader_cls=PyPDFLoader))
        # add more loaders if needed (e.g., docx, html)
    
    all_docs = []
    for loader in loaders:
        docs = loader.load()
        all_docs.extend(docs)
    
    return all_docs
