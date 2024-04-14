import time
import random
import os
import platform

"""
Programer Notes
- created in a way to enable a outside user to add more alleles if they wanted.
- clearly labeled survival and mutation chances to further customize simulation environment
- added support for 3 operating systems. this does not mean one ".exe" file will work on all 3. the program would need to be 
"""


# Logic

# Class
class Rabbit:
    def __init__(self, allele):
        self.allele = allele
        
        
# Functions        
def generate_starting_rabbit_count(num_rabbits):
    population = [] # save location for starting number of rabbits
    for i in range(num_rabbits): # loop to assign random allele to preselected number of rabbits
        allele = random.choice(["WW", "Ww", "ww"])
        rabbit = Rabbit(allele)
        population.append(rabbit)
    return population # returns a number of rabbits and their starting alleles

def count_alleles(population):
    allele_counts = {"WW": 0, "Ww": 0, "ww": 0} # will display out on the screen the total number of rabbits
    for rabbit in population:
        allele_counts[rabbit.allele] += 1
    return allele_counts

def simulate_generation(population):
    # Select rabbits to remove (simulate death)
    surviving_rabbits = []
    has_WW = any(rabbit.allele == "WW" for rabbit in population)
    has_Ww = any(rabbit.allele == "Ww" for rabbit in population)
    has_ww = any(rabbit.allele == "ww" for rabbit in population)

    for rabbit in population:
        # survival rates
        if rabbit.allele == "Ww": # This next line lowers the survival chance of just "Ww" rabbits as during testing, they seemed to explode in poulation
            if random.random() < 0.3:  # chance of survival for "Ww" rabbits
                surviving_rabbits.append(rabbit)
        else:
            if random.random() < 0.4:  # 40% chance of survival for all other rabbits
                surviving_rabbits.append(rabbit)

    # Ensure at least two rabbits remain alive, prevents program from creating new rabbits if all had died
    while len(surviving_rabbits) < 2:
        new_rabbit_allele = random.choice(["WW", "Ww", "ww"])
        if new_rabbit_allele == "WW" and not has_WW:
            surviving_rabbits.append(Rabbit(new_rabbit_allele))
            has_WW = True
        elif new_rabbit_allele == "ww" and not has_ww:
            surviving_rabbits.append(Rabbit(new_rabbit_allele))
            has_ww = True
        elif new_rabbit_allele == "Ww" and not has_Ww:
            surviving_rabbits.append(Rabbit(new_rabbit_allele))
            has_Ww = True

    # Reproduce and create offspring with a limit, this was implemented as the population seemed to explode exponentially anytime it got bigger than 30
    offspring_limit = 50  # Limit can be adjusted here
    offspring = []
    for _ in range(min(len(surviving_rabbits) * 3, offspring_limit)):
        parent = random.choice(surviving_rabbits)
        # Introduce mutation with a small probability
        if random.random() < 0.07:  # chance of mutation
            offspring_allele = random.choice(["WW", "Ww", "ww"]) # adds random alleles back into the population to increase perceived randomness
        else:
            offspring_allele = random.choice([parent.allele, parent.allele])
        offspring.append(Rabbit(offspring_allele))

    return offspring



def create_results_file():
    # Create a random number for the file name
    random_number = random.randint(1, 1000)
    
    # Determine the path to the "Downloads" directory based on the operating system
    if platform.system() == "Windows":
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    elif platform.system() == "Darwin":  # macOS
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    elif platform.system() == "Linux":  # Linux
        downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        print("Unsupported operating system.")
        return

    # Create the file path
    file_name = f"rabbit_simulation_{random_number}.csv"
    file_path = os.path.join(downloads_dir, file_name)

    # Create the file
    with open(file_path, "w") as file:
        file.write("Generation,WW,Ww,ww\n")

    return file_path

def define_rules():
    print("Phases: \n 1. When prompted, enter the starting number of Rabbits.\n 2. The program will display the mix of alleles your rabbits have\n 3. Everytime you hit enter, 3 copies of the Rabbits will be made from the previous generation. then they will all have a coin flipped to see if they perish.\n 4. The program repeats from phase 2 at this point.\n 5. A \".csv\" file will be created in your \"Downloads\" folder. The results of your experiments will be saved there.\n The naming schema will be the addition of a random number from 1-1000 appeneded a file named \"bunny_simulation...\".")



# Program entry point
def main():
    define_rules()
    # "try" blocks will test input for bad data. if someone types in a non number or decimal we will raise an exception and ask them to try again
    # this will prevent the program from panicking and closing out
    try: 
        get_starting_num_rabbits = int(input("Enter starting number of Rabbits: "))
    except:
        print("Error: Value entered is not a number or is a decimal value. Try again")
        get_starting_num_rabbits = int(input("Enter starting number of Rabbits: "))
        
    population = generate_starting_rabbit_count(get_starting_num_rabbits)
    
    # main while loop program runs in
    generations_data = []

    results_file = create_results_file()


    # here is where most of the program will run. The "while true" is a loop that continues the sim until you exit it
    while True:
        # presents starting rabbit count allele generation to user
        allele_counts = count_alleles(population)
        print("Allele counts:")
        print(allele_counts)

        # append generation data
        generations_data.append(allele_counts)

        # Write allele counts to the file
        with open(results_file, "a") as file:
            generation_data = f"{len(generations_data)+1},{allele_counts['WW']},{allele_counts['Ww']},{allele_counts['ww']}\n"
            file.write(generation_data)

        # Simulate generation
        population = simulate_generation(population)

        # Check if the "W" allele is extinct
        if allele_counts["WW"] == 0 and allele_counts["Ww"] == 0:
            print("The 'W' allele is extinct!") # simulation ends when "W" is extinct
            break

        # Prompt user to continue or stop
        user_input = input("Press Enter to continue or type 'exit' to stop: ")
        if user_input.lower() == "exit": # simulation ends if user exits program
            break
        
        # artificial wait. thought it would be nice.
        print("Randomly selecting Rabbits to die off...\n")
        time.sleep(1)
        # debug area
        
            
    

if __name__ == "__main__":
    main()
