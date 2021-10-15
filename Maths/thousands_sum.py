def thousands_sum(a: str, b: str) -> str:
    converted_a, converted_b = int(a[:-1]), int(b[:-1])
    return f"{converted_a+converted_b}K"


print(thousands_sum("10k", "20k"))
