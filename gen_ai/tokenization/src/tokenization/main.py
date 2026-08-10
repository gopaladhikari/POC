import tiktoken


def main():
    enc = tiktoken.encoding_for_model("gpt-4")
    text = "Hello, world!"
    token_encoded = enc.encode(text)

    token_decoded = [9906, 11, 1917, 0]
    token = enc.decode(token_decoded)

    print(f"Encoded: {token_encoded}")
    print(f"Decoded: {token}")


if __name__ == "__main__":
    main()
