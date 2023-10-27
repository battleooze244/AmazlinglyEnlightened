import fileinput
import subprocess


def update_executable_path():
  # Run the shell command and capture the output
  output = subprocess.check_output(["which",
                                    "chromedriver"]).decode("utf-8").strip()

  return output
  # Modify the "executable_path" variable in the "main.py" file
  # with fileinput.FileInput("main.py", inplace=True) as file:
  #   for line in file:
  #     if "chromedriver_path" in line:
  #       # line = line.replace('"hi"', f'"{output}"')
  #       chromedriver_path = output  # Assign the updated path to chromedriver_path
        line = line.replace('update_executable_path()',
                            f'"{chromedriver_path}"')
      print(line, end='')
      # if "update_executable_path():" in line:
      #   remove = True
  print("Executable path updated successfully.")
