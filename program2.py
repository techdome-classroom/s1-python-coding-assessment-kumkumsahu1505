def decode_message(s: str, p: str) -> bool:
    # This function will call the match function to check if the message matches the pattern
    def match(message, pattern):
        def is_match(i, j):
            # If we reach the end of both the message and pattern, it's a match
            if i == len(message) and j == len(pattern):
                return True
            # If only the pattern is exhausted but not the message, it's not a match
            if j == len(pattern):
                return False

            # Handle the '*' wildcard
            if pattern[j] == '*':
                # Try two options: 
                # 1. '*' matches no characters -> move only in the pattern
                # 2. '*' matches one or more characters -> move in both pattern and message
                if i < len(message) and is_match(i + 1, j):
                    return True
                return is_match(i, j + 1)

            # Handle the '?' wildcard or exact character match
            if i < len(message) and (pattern[j] == '?' or pattern[j] == message[i]):
                return is_match(i + 1, j + 1)

            # If no match is found
            return False

        return is_match(0, 0)

    # Call the match function with the input message and pattern
    return match(s, p)