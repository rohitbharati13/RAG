import os

# OS is built-in python module that provides a way of using operating system dependent functionality like reading or writing to the file system or its path.

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# data Location 
pdf_path = os.path.join(BASE_DIR , "Wikivoyage_Ireland.pdf")
i1 = os.path.join(BASE_DIR , "ireland1.pdf")
i2 = os.path.join(BASE_DIR , "ireland2.pdf")
i3 = os.path.join(BASE_DIR , "ireland3.pdf")
i4 = os.path.join(BASE_DIR , "ireland4.pdf")
i5 = os.path.join(BASE_DIR , "ireland5.pdf")
attraction_csv = os.path.join(BASE_DIR, "Attractions.csv")
Event = os.path.join(BASE_DIR, "Events.csv")
stops = os.path.join (BASE_DIR , "GTFS_ALL" , "stops.txt")
agency  = os.path.join (BASE_DIR , "GTFS_ALL" , "agency.txt")
routes = os.path.join (BASE_DIR , "GTFS_ALL" , "routes.txt")
trips = os.path.join (BASE_DIR , "GTFS_ALL" , "trips.txt")
NIAH = os.path.join(BASE_DIR, "NIAH_OpenData_2023_10_11.csv")

#model Names 
EMBEDDING_MODEL = "multi-qa-mpnet-base-dot-v1"      # This is a sentence transformer model that is used to generate embeddings for text data. It is based on the MPNet architecture and is trained on multiple question-answering datasets. The model is designed to produce high-quality embeddings that can be used for various natural language processing tasks, such as semantic search, clustering, and classification.
RERANKER_MODEL  = "cross-encoder/ms-marco-MiniLM-L12-v2"        # This is a cross-encoder model that is used for re-ranking search results. It is based on the MiniLM architecture and is trained on the MS MARCO dataset. The model takes a query and a list of candidate passages as input and outputs a relevance score for each passage. The passages can then be sorted based on their scores to produce a ranked list of results.
# LLM_MODEL       = "Qwen/Qwen2.5-3B-Instruct"    ---------- Not working in my laptop due to less ram issue
LLM_MODEL       = "Qwen/Qwen2.5-0.5B-Instruct"

#settings
USE_HYDE = True         # This setting indicates whether to use the "Hyde" approach for generating responses. When set to True, the system will generate hypothetical answers to questions based on the context provided. This can be useful for improving the quality of responses in certain scenarios.
USE_RERANKER = True     # This setting indicates whether to use the re-ranking functionality. When set to True, the system will re-rank the search results based on their relevance scores.
TOP_K = 8              