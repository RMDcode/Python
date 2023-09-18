def find_string_in_file(file_name, search):
    found_lines = []

    file = None
    
    file = open(file_name, 'r')
    lines = file.readlines()

    for line in lines:
        if search in line:
           found_lines.append(line.strip())
    
    if file:
        file.close()

    return found_lines

def main():
    file_name = input("Enter the file name: ")
    search = input("Enter the string to search: ")

    found_lines = find_string_in_file(file_name, search)

    if found_lines is None:
        print(f"An error occurred while processing the file or the file ", file_name ," does not exist.")
    else:
        print(f"The string was found in the following lines:")
        for line in found_lines:
            print(line)

if __name__ == "__main__":
    main()
