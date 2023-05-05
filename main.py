# LEGAL AND DOCUMENTATION
# Copyright (c) 2023 James Hayward

# ============================================================================ #
#   IMPORTS
# ============================================================================ #
# INCLUDED MODULES
import libs.included_tools.inc_utils as inc_tools
import libs.included_tools.inc_logger as inc_logger


# OFFICIAL MODULES


# PERSONAL MODULES



# ============================================================================ #
#   CONSTANTS
# ============================================================================ #
# INCLUDED
PROJECT_NAME        = inc_tools.get_config_value("Metadata", "project_name")        # What is the title of the program
PROJECT_AUTHOR      = inc_tools.get_config_value("Metadata", "project_author")      # Who made the file
PROJECT_YEAR        = inc_tools.get_config_value("Metadata", "project_year")        # What is the current year

PROJECT_VERSION     = inc_tools.get_config_value("Metadata", "project_version")     # What is the current version


# DEFINITIONS


# PATHS


# VALUES



# ============================================================================ #
#   LOOK-UP TABLES 
# ============================================================================ #



# ============================================================================ #
#   HASHMAPS
# ============================================================================ #
# INITIATION


# HARD-CODED HASHMAPS



# ============================================================================ #
#   GLOBAL VARIABLES
# ============================================================================ #



# ============================================================================ #
#   MAIN PIPELINE
# ============================================================================ #
def main_pipeline():                                                                # This is the main pipeline of what the code runs
    # INITIATE PROGRAM
    print(f"=== {PROJECT_NAME.upper()} ===")                                        #   # Program name
    print(f"Written by {PROJECT_AUTHOR}, {PROJECT_YEAR}")                           #   # Program details
    print()
    print(f"BOOT: Version -> {PROJECT_VERSION}")                                    #   # Program version

    
    # CHECK PIPELINE
    check_pipeline()                                                                #   # This is used to check, leave as pass if not needed

    
    # PROGRAM PIPELINE
    program_pipeline()
    

    # SCRIPT SHUTDOWN
    print("MAIN: Program Finished")


def check_pipeline():                                                               # This is the pipeline that runs checks if required
    # INITIALISE
    print("CHCK: Running Checks")

    # CHECK FILES
    inc_tools.run_file_check(".checks")                                             #   # Ensures all files and folders are present


def program_pipeline():                                                             # Runs the program proper
    # INITIATION
    # Prompt
    print("MAIN: Running Program")


    # PROGRAM PROPER


    # PROGRAM SHUTDOWN



# ============================================================================ #
#   CLASSES
# ============================================================================ #



# ============================================================================ #
#   FUNCTIONS
# ============================================================================ #
# PIPELINE FUNCTIONS


# UTILITY FUNCTIONS



# ============================================================================ #
#   MAIN
# ============================================================================ #
if __name__ == '__main__':
   main_pipeline()                                                                  # Runs the main pipeline
