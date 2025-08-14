from os import path


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(f"Bad line detected at line {line_number}: {line_string}")
        self.line_number = line_number
        self.line_string = line_string


class FileEmpty(StudentsDataException):
    def __init__(self, message):
        super().__init__(message)


def process_file(file_path):
    students = {}

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise FileEmpty("The file is empty.")

            for line_number, line in enumerate(lines, start=1):
                parts = line.split()
                if len(parts) != 3:
                    raise BadLine(line_number, line.strip())

                first_name, last_name, points_str = parts
                try:
                    points = float(points_str)
                except ValueError:
                    raise BadLine(line_number, line.strip())

                full_name = f"{first_name} {last_name}"
                if full_name in students:
                    students[full_name] += points
                else:
                    students[full_name] = points

        return {student: round(points, 1) for student, points in sorted(students.items())}

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    except StudentsDataException as e:
        raise e


if __name__ == "__main__":
    fname = input("Specify file name: ")
    script_dir = path.dirname(path.abspath(__file__))
    file_dir = path.join(script_dir, "res")
    file_path = path.join(file_dir, fname)

    try:
        results = process_file(file_path)
        for student, points in results.items():
            print(f"{student:<15} {points:.1f}")
    except Exception as e:
        print(f"Error: {e}")