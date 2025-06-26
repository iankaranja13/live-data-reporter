from astronauts import get_astronauts
from iss_tracker import get_iss_position
from news_or_stock import get_news,get_stock_price

def main():
    while True:
        print("\n==== Live Data Reporter ====")
        print("1. View astronauts currently in space")
        print("2. Get real-time ISS position")
        print("3. View top 3 U.S. business headlines")
        # Or: print("3. View IBM 5-minute stock price")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            get_astronauts()
        elif choice == '2':
            get_iss_position()
        elif choice == '3':
            get_stock_price()  # Or get_stock_price()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
