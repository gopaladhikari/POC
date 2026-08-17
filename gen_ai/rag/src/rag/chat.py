from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from google import genai
from google.genai import types
from .rag_response import RAGResponse

google_client = genai.Client()


def chat():
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")

    vector_db = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        embedding=embeddings,
        collection_name="test",
    )

    previous_interaction_id: str | None = None

    system_instruction = f"""
          You are a highly analytical, precise corporate archivist assistant answering questions about the Aegis Dynamics Corporation 50-Year Operational & Financial Archive (1976–2026).
          
          Your core directive is to answer the user's query strictly using the provided context. If the answer is not contained in the context, you must state that you do not have the information.
          
          To ensure absolute accuracy, you must always structure your response by thinking step-by-step before providing the final answer. Follow the exact format demonstrated in the examples below.
    
          --- EXAMPLES OF EXPECTED BEHAVIOR ---
    
          Example 1:
          Context: Section 8: Annual Report & Governance Record — 1983. Executive Leadership: Chief Executive Officer: Arthur Vance Pendelton. Policy Directive (1983-04): Strict prohibition against personal computing devices within server rooms. All mainframe access must be authorized using dual physical security keys.
          User Query: What was the policy regarding server room access in 1983?
          Reasoning:
          1. The user is asking for security rules regarding the server room for the year 1983.
          2. I will scan the context for "1983" and "server room".
          3. The context includes "Policy Directive (1983-04)", which mentions server rooms.
          4. The policy states a strict prohibition against personal computing devices and requires dual physical security keys for mainframe access.
          Final Answer: In 1983, under Policy Directive (1983-04), personal computing devices were strictly prohibited in server rooms, and accessing the mainframe required dual physical security keys.
    
          Example 2:
          Context: Section 24: Annual Report & Governance Record — 1999. Chief Executive Officer: Eleanor Vance-Sterling. Y2K Readiness Memo (1999-11): Legacy COBOL databases for payroll migrated to Oracle SQL. Contingency backup tapes archived off-site in Boulder, Colorado. Metric: Net Income $137.32 M.
          User Query: Where did the company store its backup tapes for Y2K, and who was the CEO?
          Reasoning:
          1. The user is asking for two pieces of information for the year 1999 (Y2K): the storage location of backup tapes and the name of the CEO.
          2. I will scan the 1999 context for the CEO's name. It states: "Chief Executive Officer: Eleanor Vance-Sterling".
          3. I will scan the 1999 context for "backup tapes". It states: "Contingency backup tapes archived off-site in Boulder, Colorado."
          4. I will combine these two extracted facts into a single concise answer.
          Final Answer: During the Y2K preparations in 1999, the CEO was Eleanor Vance-Sterling, and the company's contingency backup tapes were archived off-site in Boulder, Colorado.
    
          --- END OF EXAMPLES ---
    
          Now, process the following context and answer the user's query using the exact same Reasoning and Final Answer format.
          """

    chat_session = google_client.chats.create(
        model="gemini-3.6-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.2,
            response_mime_type="application/json",
            response_schema=RAGResponse,
        ),
    )

    while True:
        user_query = input("Enter your query: ")

        if user_query.lower() in ["quit", "exit"]:
            break

        search_results = vector_db.similarity_search(query=user_query)

        formatted_chunks = []

        for i, doc in enumerate(search_results):
            page_num = doc.metadata.get("page_label", "Unknown")

            chunk_text = f"--- Source {i+1} (Page {page_num}) ---\n{doc.page_content}"
            formatted_chunks.append(chunk_text)

        context = "\n\n".join(formatted_chunks)

        print(f"\nContext:\n{context}\n")

        augmented_input = f"Context:\n{context}\n\nUser Query: {user_query}"

        try:
            response = chat_session.send_message(augmented_input)

            if not response.text:
                print("\nNo response received from the API. Please try again.\n")
                continue

            structured_data = RAGResponse.model_validate_json(response.text)

            print(f"\n🧠 Reasoning: {structured_data.reasoning}")
            print(f"🤖 Final Answer: {structured_data.final_answer}\n")

        except Exception as e:
            print(f"\nAPI Error: {str(e)}\n")

    return vector_db
