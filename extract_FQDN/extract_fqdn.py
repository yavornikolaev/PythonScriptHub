import re

def extract_user_fqdn(input_text):
    # Define the regular expression pattern for extracting username and FQDN
    user_fqdn_pattern = r'(\b\w+\b)@(\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b)'

    # Use re.findall to extract all username and FQDN pairs from the input text
    user_fqdns = re.findall(user_fqdn_pattern, input_text)

    return user_fqdns

def main():
    # Specify the path to your input text file
    input_file_path = '/home/b5zerk/jump-ssh-servers/extracted_users_fqdns'

    # Specify the path to the output file where username and FQDN pairs will be saved
    output_file_path = '/home/b5zerk/jump-ssh-servers/extracted_users_fqdns.txt'

    try:
        # Read the content of the input file
        with open(input_file_path, 'r') as file:
            input_text = file.read()

        # Extract username and FQDN pairs using the defined function
        user_fqdns = extract_user_fqdn(input_text)

        # Save the extracted username and FQDN pairs to the output file
        with open(output_file_path, 'w') as output_file:
            for user, fqdn in user_fqdns:
                output_file.write(f'{user}@{fqdn}\n')

        print(f'Usernames and FQDNs extracted and saved to {output_file_path}')

    except FileNotFoundError:
        print(f'File not found: {input_file_path}')

if __name__ == "__main__":
    main()
