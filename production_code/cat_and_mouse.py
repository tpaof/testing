def cat_and_mouse(x, y, z):
    if not (1 <= x <= 100 and 1 <= y <= 100 and 1 <= z <= 100):
        raise ValueError("Positions must be between 1 and 100")
    
    dist_a = abs(x - z)  
    dist_b = abs(y - z)  
    
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"