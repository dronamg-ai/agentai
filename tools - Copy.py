# tools.py
import datetime
import webbrowser

def get_time():
    """Returns the current system time."""
    return datetime.datetime.now().strftime("%H:%M:%S")

def search_google(query):
    """Opens a browser and searches Google."""
    webbrowser.open(f"https://google.com{query}")
    return f"Searching Google for {query}..."
