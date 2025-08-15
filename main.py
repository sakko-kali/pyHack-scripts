

def txt_info(txt):
    with open(txt, "r", encoding="utf-8") as file:
        arr = file.read().split()

    output=f"Количество слов: {str(len(arr))}\n"
    seen = set()
    for i in arr:
        if arr.count(i) > 1 and i not in seen:
            output+=f"{i} - {arr.count(i)}\n"
            seen.add(i)
    return output

print(txt_info('111.txt'))
