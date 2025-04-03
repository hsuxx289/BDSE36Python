def menu(**options):
    def menu_selector():

        option_string='/'.join(options)

        while True:
            choice = input(f'選擇執行項目({option_string}): ')
            if choice in options:
                return options[choice]
                break
            print('選項不存在!')
    return menu_selector

if __name__ == '__main__':
    import operator
    
    a, b = 10, 3
    my_menu = menu(        
                add=operator.add,
                sub=operator.sub,
                mul=operator.mul,
                div=operator.truediv)
    
    print(my_menu()(a, b))