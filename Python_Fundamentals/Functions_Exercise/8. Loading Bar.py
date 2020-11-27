def loading_bar(number: int):
    sign_num = number // 10
    dots_num = 10 - sign_num
    if sign_num < 10:
        return f"{number}% [{'%' * sign_num}{'.' * dots_num}]" \
               f"\nStill loading..."
    else:
        return f"{number}% Complete!" \
               f"\n[{'%' * sign_num}{'.' * dots_num}]"


loading_input = int(input())
print(loading_bar(loading_input))
