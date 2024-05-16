# main.py

if __name__ == "__main__":
    # Run Behave tests
    from behave.__main__ import main as behave_main
    behave_main(['features'])
