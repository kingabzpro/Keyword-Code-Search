import argparse

from gpt_explainer import query_gpt
from searcher import search_codebase


def print_streaming_response(stream):
    """Print the streaming response from GPT-4.1"""
    print("\nGPT-4.1 Response:")
    for event in stream:
        # Check if the event includes a text delta.
        if hasattr(event, "delta") and event.delta:
            print(event.delta, end="")
    print("\n")


def main():
    parser = argparse.ArgumentParser(
        description="Keyword-Based Code Search with GPT-4.1"
    )
    parser.add_argument("--path", required=True, help="Path to the codebase")
    args = parser.parse_args()

    allowed_extensions = [".py", ".js", ".txt", ".md", ".html", ".css", ".sh"]

    print("Welcome to the Code Search Chatbot!")
    print("Ask questions about your codebase or type 'quit' to exit.")

    while True:
        question = input("\nEnter your question about the codebase: ")

        if question.lower() == "quit":
            print("Exiting chatbot. Goodbye!")
            break

        # Extract keywords from the question and remove stop words
        stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 
                     'in', 'on', 'at', 'to', 'for', 'with', 'by', 'about', 'like', 
                     'from', 'of', 'as', 'how', 'what', 'when', 'where', 'why', 'who'}
        keywords = [word for word in question.lower().split() if word not in stop_words][:5]

        print("Searching codebase...")
        matches = search_codebase(args.path, keywords, allowed_extensions)

        if not matches:
            print("No relevant code snippets found.")
            continue

        print("Querying GPT-4.1...")
        stream = query_gpt(question, matches)
        print_streaming_response(stream)


if __name__ == "__main__":
    main()
