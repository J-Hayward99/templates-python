# LEGAL AND DOCUMENTATION
# Copyright (c) 2023 James Hayward


# IMPORTS
# Official Modules


# Personal Modules
import libs.included_tools as inc_tools


# CONSTANTS
# Included
PROJECT_NAME        = inc_tools.get_config_value("Metadata", "project_name")        # What is the title of the program
PROJECT_AUTHOR      = inc_tools.get_config_value("Metadata", "project_author")      # Who made the file
PROJECT_YEAR        = inc_tools.get_config_value("Metadata", "project_year")        # What is the current year

PROJECT_VERSION     = inc_tools.get_config_value("Metadata", "project_version")     # What is the current version

# Program


# LOOK-UP TABLES


# GLOBAL VARIABLES


# MAIN PIPELINE
def main_pipeline():                                                                # This is the main pipeline of what the code runs
    # INITIATE PROGRAM
    print(f"=== {PROJECT_NAME.upper()} ===")                                        #   # Program name
    print(f"Written by {PROJECT_AUTHOR}, {PROJECT_YEAR}")                           #   # Program details
    print()
    print(f"BOOT: Version -> {PROJECT_VERSION}")                                    #   # Program version

    # CHECK PIPELINE
    check_pipeline()                                                                #   # This is used to check, leave as pass if not needed

    # PROGRAM START
    #

    # SHUT DOWN



def check_pipeline():                                                               # This is the pipeline that runs checks if required
    # INITIALISE
    print("CHCK: Running Checks")

    # CHECK FILES
    inc_tools.run_file_check(".checks")                                             #   # Ensures all files and folders are present


# CLASSES


# FUNCTIONS
# Pipeline Functions


# Utility Functions


# MAIN
if __name__ == '__main__':
   main_pipeline()                                                                  # Runs the main pipeline


# DESCRIPTION
"""
    _summary_


"""


# NOTES
"""
    _notes_

"""


# PLAN
"""
    _plan_

"""


