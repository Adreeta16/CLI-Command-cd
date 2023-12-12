# Change Directory Script

This Python script (`cd.py`) allows you to change the current working directory using command-line arguments.

## Usage

1. **Requirements:**
   - Python 3.x
   - Libraries: `os`, `argparse`

2. **Instructions:**

   - **Running the Script:**
     - Open a terminal or command prompt.
     - Navigate to the directory containing the `cd.py` file.
     - Execute the script using Python and provide the desired directory path as an argument.

     ```bash
     python cd.py /path/to/directory
     ```

   - **Note:** Ensure the provided path exists, otherwise, you'll receive a "Directory not found" error.

3. **Functionality:**

   - The script `cd.py` takes a single argument: the path to the directory you want to change to.
   - It attempts to change the current working directory to the specified path.
   - Upon successful change, it displays the new working directory.
   - If the specified directory doesn't exist, it prints "Directory not found."

4. **Example:**

   - Changing directory to `/Users/username/Documents`:

     ```bash
     python cd.py /Users/username/Documents
     ```
     Output:
     ```
     Changed directory to: /Users/username/Documents
     ```

---

Feel free to adjust the content based on the specific details of your script and its usage. This README provides an overview of what the script does, how to use it, and an example scenario.
