# text_file_age_extractor.py

def extract_ages_from_file(filename="data.txt"):
    total_age = 0
    print("\n--- Parsed Age Data ---")

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().rsplit(" ", 1)
            if len(parts) == 2 and parts[1].isdigit():
                name, age = parts[0], int(parts[1])
                print(f"{name}, Age: {age}")
                total_age += age

    print("Total sum of ages:", total_age)

def main():
    extract_ages_from_file()

if __name__ == "__main__":
    main()
