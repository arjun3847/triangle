def classify_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    if a + b <= c:
        return "Not a triangle"
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    if a**2 + b**2 == c**2:
        triangle_type += " and Right"
    return triangle_type
