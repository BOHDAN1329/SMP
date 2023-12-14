# runner.py
from menu import display_menu
from service import ConsumerServiceImpl

def main():
    data_file = "./files/consumers.csv"
    service = ConsumerServiceImpl(data_file)

    display_menu(service)

if __name__ == '__main__':
    main()
