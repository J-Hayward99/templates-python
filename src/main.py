# LEGAL AND DOCUMENTATION
# Copyright (c) 2023 James Hayward

# ============================================================================ #
#   IMPORTS
# ============================================================================ #
# INCLUDED MODULES
import libs.jimsuite.jimsuite_utils as jim_tools
import libs.jimsuite.jimsuite_logger as jim_log


# OFFICIAL MODULES


# PERSONAL MODULES


# ============================================================================ #
#   SETUP
# ============================================================================ #
# LOAD SETTINGS
jim_tools.set_config_location("./src/configurations/config.ini")
jim_tools.set_checks_location("./src/configurations/.checks")
jim_log.change_threshold_level()



# ============================================================================ #
#   CONSTANTS
# ============================================================================ #
# INCLUDED
PROJECT_NAME        = jim_tools.get_config_value("Metadata", "project_name")        # What is the title of the program
PROJECT_AUTHOR      = jim_tools.get_config_value("Metadata", "project_author")      # Who made the file
PROJECT_YEAR        = jim_tools.get_config_value("Metadata", "project_year")        # What is the current year

PROJECT_VERSION     = jim_tools.get_config_value("Metadata", "project_version")     # What is the current version


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
    jim_log.none(f"=== {PROJECT_NAME.upper()} ===")                                     #   # Program name
    jim_log.none(f"Written by {PROJECT_AUTHOR}, {PROJECT_YEAR}\n")                      #   # Program details
    jim_log.boot(f"Version -> {PROJECT_VERSION}")                                       #   # Program version

    
    # CHECK PIPELINE
    check_pipeline()                                                                #   # This is used to check, leave as pass if not needed

    
    # PROGRAM PIPELINE
    program_pipeline()
    

    # SCRIPT SHUTDOWN
    jim_log.main("Program Finished")


def check_pipeline():                                                               # This is the pipeline that runs checks if required
    # INITIALISE
    jim_log.check("Running Checks")

    # CHECK FILES
    jim_tools.run_file_check()                                                      #   # Ensures all files and folders are present


def program_pipeline():                                                             # Runs the program proper
    # INITIATION
    # Prompt
    jim_log.main("Running Program")


    # GUARD CLAUSES


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
