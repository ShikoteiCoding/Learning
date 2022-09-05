

def print_banner(title, length=50):
    centered_title = " "*2 + title + " "*2
    adapted_length = len(centered_title) if len(centered_title) > length else length
    semi_diff = (adapted_length - len(centered_title)) // 2
    extra = "#" if (semi_diff * 2 + len(centered_title)) % 2 == 1 else ""
    border = "#" * semi_diff + extra
    print("\n" + "#"*adapted_length + extra)
    print(border + centered_title + border)
    print("#"*adapted_length + extra + "\n")