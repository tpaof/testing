def funny_string(s):
    if not (1 <= len(s) <= 10000):
        raise ValueError("String length must be between 1 and 10000")
    
    r = s[::-1]
    
    for i in range(1, len(s)):
        diff_s = abs(ord(s[i]) - ord(s[i-1]))
        diff_r = abs(ord(r[i]) - ord(r[i-1]))
        if diff_s != diff_r:
            return "Not Funny"
    
    return "Funny"