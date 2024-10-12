import kaitaistruct
from kaitaistruct import KaitaiStream
from exapunks_solution import ExapunksSolution  # Import your generated class here

# Ask the user for the file name
file_name = input("Please enter the binary file name to parse: ")

try:
    # Open the binary file in binary mode
    with open(file_name, "rb") as f:
        # Create a KaitaiStream object from the file
        stream = KaitaiStream(f)
        
        # Pass the stream to the ExapunksSolution class for parsing
        solution = ExapunksSolution(stream)

    # Now you can access the parsed attributes, for example:
    print(f"Magic bytes: {solution.magic}")
    print(f"File ID: {solution.file_id.string}")
    print(f"Name: {solution.name.string}")
    print(f"Competition Wins: {solution.competition_wins}")

    # Loop through EXA instances
    for exa in solution.exa_instances:
        print(f"EXA Name: {exa.name.string}")
        print(f"EXA Code: {exa.code.string}")

except FileNotFoundError:
    print(f"File '{file_name}' not found. Please check the file path and try again.")
except kaitaistruct.ValidationNotEqualError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
