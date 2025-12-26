def get_user_input():
    return input("Enter your query: ")

def validate_input(query):
    if not query:
        raise ValueError("Query cannot be empty")
    return True

