import os
from PyInstaller.__main__ import run

def convert_to_exe(script_path):
    # Get the absolute path of the script
    script_path = os.path.abspath(script_path)

    # Run PyInstaller programmatically to create the .exe file
    spec_file = f"{os.path.splitext(script_path)[0]}.spec"
    run([
        "--onefile",
        "--name=%s" % os.path.splitext(os.path.basename(script_path))[0],
        script_path
    ])

    # Get the output directory path
    output_dir = os.path.join(os.path.dirname(script_path), "dist")

    # Find the generated .exe file
    exe_file = None
    for file_name in os.listdir(output_dir):
        if file_name.endswith(".exe"):
            exe_file = os.path.join(output_dir, file_name)
            break

    if exe_file:
        print(f"Conversion successful. The .exe file is saved at: {exe_file}")
    else:
        print("Error: Failed to create the .exe file.")

if __name__ == "__main__":
    # Ask the user for the path of the GUI script
    gui_script_path = input("Enter the path of the GUI script you want to convert: ")

    if os.path.isfile(gui_script_path):
        convert_to_exe(gui_script_path)
    else:
        print("Error: The specified path is not a valid file.")
