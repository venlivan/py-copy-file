import os


def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3 and parts[0] == "cp":
        _, file1, file2 = command.split()
        if file1 == file2:
            return
        if os.path.exists(file1):
            with (open(file1, "r") as input_file,
                  open(file2, "w") as output_file):
                for line in input_file:
                    output_file.write(line)
