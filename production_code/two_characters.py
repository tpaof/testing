def Two_characters(s):
    unique_chars = set(s)
    max_length = 0
    
    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered = [c for c in s if c == char1 or c == char2]
                if all(filtered[i] != filtered[i+1] for i in range(len(filtered)-1)):
                    max_length = max(max_length, len(filtered))
    
    return max_length