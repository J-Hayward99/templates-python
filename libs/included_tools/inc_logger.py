# LEGAL AND DOCUMENTATION
# Copyright (c) 2023 James Hayward


# IMPORTS
# Official Modules
import sys

# Personal Modules



# CONSTANTS
# Initiation

# Values


# LOOK-UP TABLES


# HASHMAPS
# Initiation


# Hard-coded Hashmaps
_name_to_level = {
    "EXIT"      : ["EXIT", 60],                                                     # Used for System Exits
    "CRITICAL"  : ["CRIT", 50],                                                     # Used for Critical Errors: Basically exit without sys.exit
    "ERROR"     : ["ERRO", 40],                                                     # Used for Errors
    "WARNING"   : ["WARN", 30],                                                     # Used for Warnings 
    "INFO"      : ["INFO", 20],                                                     # Used for Additional Info
    "DEBUG"     : ["DBUG", 10],                                                     # Used for Debug Messages
    "CHECK"     : ["CHCK", 4 ],                                                     # Used for the Check sequence
    "MAIN"      : ["MAIN", 3 ],                                                     # Used for the Main sequence
    "BOOT"      : ["BOOT", 2 ],                                                     # Used for the Boot sequence
    "PROGRAM"   : ["PROG", 1 ],                                                     # Used for the Program Sequence
    "NOTSET"    : ["NONE", 0 ]                                                      # Default case
}                                                                                   # "LEVEL":str : ["BOOTCODE":str, NUMERICAL_LEVEL:int]


# GLOBAL VARIABLES



# FUNCTIONS
# Main Functions


# UTILITY FUNCTIONS
def _build_text(text, level="NOTSET"):
    # INITATION
    prefix = _name_to_level[level][1] + ": "
    
    # CONDITIONS
    if level == "NOTSET":
        prefix = ""

    # FUNCTION PROPER
    return prefix + text
