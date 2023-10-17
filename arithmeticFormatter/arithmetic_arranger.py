from re import split

def arithmetic_arranger(problems, display_results=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists to store each line of the arranged problems
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    # Iterate through each problem
    for problem in problems:
        # Split the problem into its components
        split_problem = problem.split()
        num1, operator, num2 = split_problem[0], split_problem[1], split_problem[2]

        # Check if the operator is valid (must be '+' or '-')
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        # Check if the numbers are valid (only contain digits)
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if the numbers are too long (more than four digits)
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the width of each line based on the length of the numbers
        width = max(len(num1), len(num2)) + 2

        # Add the components of the problem to their respective lines
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        third_line.append('-' * width)

        # If display_results is True, calculate and add the result to the fourth line
        if display_results:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            fourth_line.append(result.rjust(width))

    # Join the lines with spaces and add them to a list
    lines = [
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(third_line)
    ]

    # If display_results is True, add the fourth line
    if display_results:
        lines.append("    ".join(fourth_line))

    # Join the lines with newline characters to form the final arranged problems
    arranged_problems = "\n".join(lines)

    return arranged_problems
