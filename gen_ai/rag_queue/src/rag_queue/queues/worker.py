from openai import OpenAI
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from rag_queue.qdrant import initialize_database

load_dotenv()

client = OpenAI()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = initialize_database()


def process_query(query: str):
    print("Processing query:", query)

    previous_id = None

    searched_results = vector_store.similarity_search(query)

    formatted_chunks = [
        f"--- Source {i+1} (Page {doc.metadata.get('page_label', 'Unknown')}) ---\n{doc.page_content}"
        for i, doc in enumerate(searched_results)
    ]

    context = "\n\n".join(formatted_chunks)

    augmented_input = f"Context:\n{context}\n\nUser Query: {query}"

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

            {context}
            """

    request_kwargs = {
        "model": "gpt-5.6",
        "instructions": system_instruction,
        "input": augmented_input,
        "store": True,
    }

    if previous_id:
        request_kwargs["previous_response_id"] = previous_id

    try:

        response = client.responses.create(**request_kwargs)

        previous_id = response.id

        return response.output_text

    except Exception as e:
        print(f"\nAPI Error: {str(e)}")
