def read_file(file_path):
    with open(file_path) as file:
        return file.readlines()


def read_file_into_array(file_path):
    with open(file_path) as file:
        return [line.strip(",") for line in file]
