

def print_banner(title, length=50):
    centered_title = " "*2 + title + " "*2
    adapted_length = len(centered_title)
    if adapted_length > 50:
        print("#"*adapted_length)
        print(centered_title)
        print("#"*adapted_length)
    else:
        semi_diff = (length - len(centered_title)) // 2
        extra = "#" if (semi_diff * 2 + len(centered_title)) % 2 == 1 else ""
        border = "#" * semi_diff + extra
        print("#"*length + extra)
        print(border + centered_title + border)
        print("#"*length + extra)
        