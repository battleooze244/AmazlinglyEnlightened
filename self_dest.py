# import fileinput

# def remove_update_executable_path():
#   # Remove the update_executable_path() function and its associated code from the "main.py" file
#   with fileinput.FileInput("main.py", inplace=True) as file:
#     remove = False
#     for line in file:
#       if "def update_executable_path():" in line:
#         remove = True
#       elif remove and line.strip() == "":
#         remove = False
#         continue
#       elif remove:
#         continue
#       print(line, end='')

#   print("update_executable_path()  associated code removed successfully.")

#   if "update_executable_path():" in file:
#     remove = True
#   if "def update_executable_path():" in file:
#     remove = True

# Call the function to remove the update_executable_path() function and its associated code
import fileinput


def remove_update_executable_path():
  # Remove the update_executable_path() function and its associated code from the "main.py" file
  with fileinput.FileInput("main.py", inplace=True) as file:
    remove = False
    for line in file:
      if "def update_executable_path():" in line:
        remove = True
        continue
      elif remove and line.strip() == "":
        remove = False
        continue
      elif remove:
        continue
      elif "update_executable_path():" in line:
        continue
      elif "def update_executable_path():" in line:
        continue
      print(line, end='')

  print("update_executable_path() and associated code removed successfully.")


# remove_update_executable_path()
# import fileinput

# def remove_update_executable_path():
#   # Remove the update_executable_path() function and its associated code from the "main.py" file
#   with fileinput.FileInput("main.py", inplace=True) as file:
#     remove = False
#     for line in file:
#       if "def update_executable_path():" in line:
#         remove = True
#       elif remove and line.strip() == "":
#         remove = False
#         continue
#       elif remove:
#         continue
#       print(line, end='')

#   print("update_executable_path()  associated code removed successfully.")
#   # remove_remaining()

# def remove_remaining():
#   with fileinput.FileInput("main.py", inplace=True) as file:
#     remove = False
#     for line in file:
#       if "def update_executable_path():" in line:
#         remove = True

# elif "update_executable_path():" in file:
#   remove = True
