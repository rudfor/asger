# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_item(index: int, item: list, tax=1.25):
    """
    index is human-readable so index starts with 1 :)
    """
    print(f'Item {index} ex.tax {item[index-1]}')
    print(f'Item {index} taxed {item[index-1]*tax}')
    return item[index-1]*tax


# Press the green button in the gutter to run the script.
if __name__ == '_main_':
    items = [80, 140, 230]
    print_item(1, items)
    print_item(2, items)
    print_item(3, items)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
