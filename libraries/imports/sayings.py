def main():
    hello("david")
    goodbye("david")

def goodbye(text):
    print(f"Goodbye {text}")

def hello(text):
    print(f"Hello {text}")

# Checks if the file is being run through the CLI and not being imported
# Can cause bugs when importing this file
if __name__ == "__main__":
    main()