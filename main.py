# main.py
import brain
import tools

def start_assistant():
    print("Assistant is online. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
            
        # Logic to decide if we use a 'Hand' or just the 'Brain'
        if "time" in user_input.lower():
            print(f"Assistant: The time is {tools.get_time()}")
        elif "search" in user_input.lower():
            query = user_input.replace("search", "").strip()
            print(f"Assistant: {tools.search_google(query)}")
        else:
            # Use the Brain for everything else
            reply = brain.ask_ai(user_input)
            print(f"Assistant: {reply}")

if __name__ == "__main__":
    start_assistant()
