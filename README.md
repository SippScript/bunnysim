# Bunny Allele Simulator

My goal with this project was to make a game that could recreate one of the labs we did in my biology course.
I aimed to make the code simple enough to mess with should an operator want more complexity in their sim.  

---
# Release 
a copy of an executable for Windows, Mac, and Linux will all be availbe under release 1.0.0.

If I get to adding onto the program, I will update the release as well!  

---
Build Instructions
! Note ! These build instructions are made people people who know how to setup a project environment for Python
1. Create a directory on your machine and `cd` into it:
    ```bash
    mkdir project_directory
    cd project_directory
    ```

2. Clone the repository:
    ```bash
    git clone https://github.com/SippScript/bunnysim.git
    ```
        
3. Install pyinstaller:
    ```bash
    pip install pyinstaller
    ```

4. Navigate to the "src" directory:
    ```bash
    cd project_directory/src
    ```

5. Build the project using pyinstaller:
    ```bash
    pyinstaller main.py
    ```

6. To create a single executable file, use:
    ```bash
    pyinstaller -F main.py
    ```

The executable will be created in the "dist" directory.
