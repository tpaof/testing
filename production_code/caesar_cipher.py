def caesar_cipher(s, k):
    if not s:
        raise ValueError("String cannot be empty")
    
    k = k % 26
    
    result = ""
    for char in s:
        if char.isalpha():
            ascii_base = 65 if char.isupper() else 97
            
            shifted = (ord(char) - ascii_base + k) % 26
            
            result += chr(shifted + ascii_base)
        elif char == '-':
            result += char
        else:
            raise ValueError("String must contain only alphabets and hyphens")
            
    return result