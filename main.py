import argparse
from searcher import search_codebase
from gpt_explainer import query_gpt


def print_matches(matches):
    for match in matches:
        print(f"File: {match['file']} (Line {match['line_number']})")
        print(match["code"])
        print("-----")


def print_streaming_response(stream):
    """Print the streaming response from GPT-4.1"""
    print("\nGPT-4.1 Response:")
    for chunk in stream:
        if hasattr(chunk, 'content') and chunk.content:
            print(chunk.content, end="", flush=True)
    print("\n")


def main():
    parser = argparse.ArgumentParser(
        description="Keyword-Based Code Search with GPT-4.1"
    )
    parser.add_argument("--path", required=True, help="Path to the codebase")
    parser.add_argument(
        "--explain",
        action="store_true",
        help="Query GPT-4.1 to generate explanation based on the found snippets.",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive chat mode",
    )
    args = parser.parse_args()
    
    allowed_extensions = [".py", ".js", ".txt", ".md", ".html", ".css", ".sh"]

    if args.interactive:
        print("Welcome to the Code Search Chatbot!")
        print("Ask questions about your codebase or type 'quit' to exit.")
        
        while True:
            question = input("\nEnter your question about the codebase: ")
            
            if question.lower() == 'quit':
                print("Exiting chatbot. Goodbye!")
                break
                
            # Extract keywords from the question (using first 5 words for simplicity)
            keywords = question.lower().split()[:5]

            print("Searching codebase...")
            matches = search_codebase(args.path, keywords, allowed_extensions)

            if not matches:
                print("No relevant code snippets found.")
                continue

            # If explain flag is not set, simply print the matching snippets
            if not args.explain:
                print_matches(matches)
            else:
                print("Querying GPT-4.1...")
                stream = query_gpt(question, matches, stream=True)
                print_streaming_response(stream)
    else:
        # Original non-interactive mode
        question = input("Enter your question about the codebase: ")
        
        # Extract keywords from the question (using first 5 words for simplicity)
        keywords = question.lower().split()[:5]

        print("Searching codebase...")
        matches = search_codebase(args.path, keywords, allowed_extensions)

        if not matches:
            print("No relevant code snippets found.")
            return

        # If explain flag is not set, simply print the matching snippets
        if not args.explain:
            print_matches(matches)
            return

        print("Querying GPT-4.1...")
        if args.stream:
            stream = query_gpt(question, matches, stream=True)
            print_streaming_response(stream)
        else:
            response = query_gpt(question, matches)
            print("\nGPT-4.1 Response:")
            print(response)


if __name__ == "__main__":
    main()
