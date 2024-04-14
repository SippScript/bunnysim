# Bunny Allele Simulator

My goal with this project was to make a game that could recreate one of the labs we did in my biology course.
I aimed to make the code simple enough to mess with should an operator want more complexity in their sim.
---
# Release 
a copy of an executable for Windows, Mac, and Linux will all be availbe under release 1.0.0
If I get to adding onto the program, I will update the release as well!
---
# Build Instructions
1. Create a directory on your machine and `cd` into it:
    ```bash
    mkdir project_directory
    cd project_directory
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/SippScript/bunnysim.git
    ```

3. Create a virtual environment for the project:
    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment (commands may vary based on your operating system):
    - For Unix/Linux/macOS:
        ```bash
        source venv/bin/activate
        ```
    - For Windows:
        ```bash
        .\venv\Scripts\activate
        ```

5. Install pyinstaller:
    ```bash
    pip install pyinstaller
    ```

6. Navigate to the "src" directory:
    ```bash
    cd bunnysim/src
    ```

7. Build the project using pyinstaller:
    ```bash
    pyinstaller main.py
    ```

8. To create a single executable file, use:
    ```bash
    pyinstaller -F main.py
    ```

9. The executable will be created in the "dist" directory.
