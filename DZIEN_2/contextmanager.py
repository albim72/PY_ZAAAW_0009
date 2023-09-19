class ContextManager:
    def __init__(self):
        print('inicjacja funkcji __init__')

    def __enter__(self):
        print('inicjacja funkcji __enter__')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('inicjacja funkcji __exit__')

with ContextManager() as manager:
    print('działanie w bloku with...')
