from model import *
from view import *


def button_click():
    reader_object = 'telephone_book.csv'
    answer = menu()
    telephone_directory = read_file_csv(reader_object)

    while (answer != 6):
        if answer == 1:
            print_book(telephone_directory)
        elif answer == 2:
            search_subscriber(telephone_directory)
        elif answer == 3:
            new_subscriber(telephone_directory)
        elif answer == 4:
            export_file_txt(telephone_directory)
        elif answer == 5:
            save_request(telephone_directory)
            break

        answer = menu()