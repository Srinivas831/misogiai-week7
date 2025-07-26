from collections import deque

# Max history size
MAX_HISTORY_SIZE = 5

# Initialize deques
history = deque()
forward_stack = deque()
print(history)

def add_new_page(url):
    global history, forward_stack
    if len(history) == MAX_HISTORY_SIZE:
        history.popleft()  # Remove the oldest page
    history.append(url)
    forward_stack.clear()  # Reset forward stack on new page visit
    print(f"Visited: {url}")
    show_state()

def go_back():
    global history, forward_stack
    if len(history) > 1:
        last_page = history.pop()
        forward_stack.append(last_page)
        print(f"Back to: {history[-1]}")
    else:
        print("No pages to go back to.")
    show_state()

def go_forward():
    global history, forward_stack
    if forward_stack:
        next_page = forward_stack.pop()
        history.append(next_page)
        print(f"Forward to: {next_page}")
    else:
        print("No forward history.")
    show_state()

def show_state():
    print("History:", list(history))
    print("Forward Stack:", list(forward_stack))
    print("-" * 40)

# ==== Demo ====

add_new_page("google.com")
add_new_page("github.com")
add_new_page("stackoverflow.com")
add_new_page("wikipedia.org")
add_new_page("reddit.com")
add_new_page("openai.com")  # This should remove "google.com"

go_back()   # Go back to "reddit.com"
go_back()   # Go back to "wikipedia.org"
go_forward()  # Go forward to "reddit.com"

add_new_page("news.ycombinator.com")  # New page clears forward stack
