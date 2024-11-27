import sys
from file_handler import FileHandler
from address_book import AddressBook
from ui import UI
from exceptions import NotNumberError, WrongNumberError, NotAddressFormatError, log_exception

class Menu:
    def start(self):
        file_path = "C:/Users/Max/OOP/Lab_3/Python/addresses.txt"

        # Заготовочка для демонстрації неправильного шляху до файлу для NotFoundFileError 
        #file_path = "C:/Users/User/Documents/Беляш/VS_code/Lab4/aaddresses.txt" 

        address_book = AddressBook()
        file_handler = FileHandler(file_path)
        ui = UI(address_book, file_handler)

        choice = -1
        while choice != 0:
            print("\nMenu:")
            print("1. Load addresses from file")
            print("2. Add private house")
            print("3. Add appartment")
            print("4. Select addresses for mailing")
            print("5. Analyze addresses")
            print("0. Exit")

            try: 
                # Отримання вводу користувача
                user_input = input("Enter your choice: ").strip()
                
                # Перевірка, чи ввід є числом
                if not user_input.isdigit():
                    raise NotNumberError("Menu choice must be a number.")
                
                choice = int(user_input)
                
                # Перевірка, чи ввід є в межах допустимих чисел
                if choice not in [0, 1, 2, 3, 4, 5]:
                    raise WrongNumberError("Choice must be a number between 0 and 5.")
                
                # Обробка вибору
                if choice == 1:
                    ui.load_addresses()

                elif choice == 2:
                    try:
                        input_data = input("Enter city, street, building number (separated by spaces): ").split()
        
                        # Перевірка кількості введених даних
                        if len(input_data) != 3:
                            raise NotAddressFormatError("You must provide exactly three values: city, street, and building number.")
        
                        city, street, building_number = input_data

                        # Перевірка чи building_number є числом
                        if not building_number.isdigit():
                            raise NotAddressFormatError("Building number must be a valid integer.")
            
                        ui.add_private_address(city, street, building_number)

                    except NotAddressFormatError as e:
                        log_exception(e)  # Логування помилки
                        print(f"Wrong data format! Caught exception: {e}", file=sys.stderr)

                    except Exception as e:
                        log_exception(e)  # Логування помилки
                        print(f"An unexpected error occurred: {e}", file=sys.stderr)

                elif choice == 3:
                    
                    try:
                        input_data = input("Enter city, street, and building number and appartment number: ").split()
            
                        # Перевірка кількості введених даних
                        if len(input_data) != 4:
                            raise NotAddressFormatError("You must provide exactly four values: city, street, building number and appartment number.")
            
                        city, street, building_number, apartment_number = input_data

                        # Перевірка чи building_number є числом
                        if not building_number.isdigit():
                            raise NotAddressFormatError("Building number must be a valid integer.")
                        # Перевірка чи appartment_number є числом
                        if not apartment_number.isdigit():
                            raise NotAddressFormatError("Appartment number must be a valid integer.")
            
                        ui.add_appartment_address(city, street, building_number, apartment_number)

                    except NotAddressFormatError as e:
                        log_exception(e)  # Логування помилки
                        print(f"Wrong data format! Caught exception: {e}", file=sys.stderr)

                    except Exception as e:
                        log_exception(e)  # Логування помилки
                        print(f"An unexpected error occurred: {e}", file=sys.stderr) 

                elif choice == 4:
                    ui.select_addresses_for_mailing()
                elif choice == 5:
                    ui.analyze_addresses()
                
            except NotNumberError as e:
                log_exception(e)  # Логування помилки
                print(f"Wrong input format! Caught exception: {e}", file=sys.stderr)

            except WrongNumberError as e:
                log_exception(e)  # Логування помилки
                print(f"Wrong input format! Caught exception: {e}", file=sys.stderr)

            except Exception as e:
                log_exception(e)  # Логування помилки
                print(f"An unexpected error occurred: {e}", file=sys.stderr)