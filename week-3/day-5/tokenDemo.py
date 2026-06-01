import re

# Scenario 1: Token followed by a space
text_log = "User logged in. Auth_token: xyz123_abc456 status: active"

# Scenario 2: Token followed by a quote
text_json = '{"session": "valid", "Auth_token":"token_in_quotes"}'

pattern = r"Auth_token:\s*([^\s\"]+)"

# Extracting from text_log
match_log = re.search(pattern, text_log)
if match_log:
    print(f"Found Token 1: {match_log.group(1)}")  # Output: xyz123_abc456

# Extracting from text_json
match_json = re.search(pattern, text_json)
if match_json:
    print(f"Found Token 2: {match_json.group(1)}")  # Output: token_in_quotes
