# LEGAL AND DOCUMENTATION
# Copyright (c) 2023 James Hayward


# ============================================================================ #
#   IMPORTS
# ============================================================================ #
# OFFICIAL MODULES
import sys


# PERSONAL MODULES



# ============================================================================ #
#   DEFINITIONS
# ============================================================================ #
# PUBLIC


# PRIVATE
_LEVELS_CODE    = 0
_LEVELS_VALUE   = 1

_CODE_LENGTH     = 4



# ============================================================================ #
#   LOOK-UP TABLES 
# ============================================================================ #



# ============================================================================ #
#   HASHMAPS
# ============================================================================ #
# INITIATION


# HARD-CODED HASHMAPS
_name_to_level = {
    "EXIT"      : ["EXIT", 60],                                                     # Used for System Exits
    "CRITICAL"  : ["CRIT", 50],                                                     # Used for Critical Errors: Basically exit without sys.exit
    "ERROR"     : ["ERRO", 40],                                                     # Used for Errors
    "CHECK"     : ["CHCK", 34],                                                     # Used for the Check sequence
    "MAIN"      : ["MAIN", 33],                                                     # Used for the Main sequence
    "BOOT"      : ["BOOT", 32],                                                     # Used for the Boot sequence
    "PROGRAM"   : ["PROG", 31],                                                     # Used for the Program Sequence
    "WARNING"   : ["WARN", 30],                                                     # Used for Warnings 
    "INFO"      : ["INFO", 20],                                                     # Used for Additional Info
    "DEBUG"     : ["DBUG", 10],                                                     # Used for Debug Messages
    "NOTSET"    : ["NONE", 0 ]                                                      # Default case
}                                                                                   # "LEVEL":str : ["BOOTCODE":str, NUMERICAL_LEVEL:int]



# ============================================================================ #
#   FUNCTIONS
# ============================================================================ #
# MAIN FUNCTIONS
# Print Messages Block
def exit(message:str) -> None:
    sys.exit(_build_text(message, level="EXIT"))

def critical(message:str) -> None:
    print(_build_text(message, level="CRITICAL"))

def error(message:str) -> None:
    sys.exit(_build_text(message, level="ERROR"))

def warning(message:str) -> None:
    print(_build_text(message, level="WARNING"))

def info(message:str) -> None:
    print(_build_text(message, level="INFO"))

def debug(message:str) -> None:
    print(_build_text(message, level="DEBUG"))

def check(message:str) -> None:
    print(_build_text(message, level="CHECK"))

def main(message:str) -> None:
    print(_build_text(message, level="MAIN"))

def boot(message:str) -> None:
    print(_build_text(message, level="BOOT"))

def program(message:str) -> None:
    print(_build_text(message, level="PROGRAM"))

def none(message:str) -> None:
    print(_build_text(message, level="NOTSET"))


# Level Handler Block
def add_level(level_name:str, level_code:str, level_value:int) -> None:
    # INITATION
    string_parameters = [level_name, level_code]

    # CONDITIONS
    # Type Check
    for parameter in string_parameters:
        if not isinstance(parameter, str):
            error(
                f"\"{parameter}\" is not a string -> "
                + f"level_name_type=\"{type(parameter)}\""
            )

    # Level Name Specific Checks
    if level_name.upper() != level_name:                                            #   # Enforces the string is uppercase
        level_name = level_name.upper()
    

    # Level Code Specific Checks
    if len(level_code) != _CODE_LENGTH:                                             #   # Checks that the code length is correct
        error(
            f"Code length is not \"{_CODE_LENGTH}\" characters long -> "
            + f"code=\"{level_code}\", code_length=\"{len(level_code)}\""
        )
    
    if level_code.upper() != level_code:                                            #   # Enforces the string is uppercase
        level_code = level_code.upper()

    # Level Value Specific Checks
    if not isinstance(level_value, int):
            error(
                f"\"{level_value}\" is not a integer -> "
                + f"level_name_type=\"{type(level_value)}\""
            )
    
    # Existence Check
    for level in _name_to_level:                                                    #   # Iterates through hashmap
        if level_name == level:
            error(f"Cannot add level -> \"{level_name}\" already exists")

        if level_code == _name_to_level[level][_LEVELS_CODE]:
            error(f"Cannot add level -> Code \"{level_code}\" already  "
                  + f"exists for level=\"{level}\""
            )

        if level_value == _name_to_level[level][_LEVELS_VALUE]:
            error(f"Cannot add level -> Value \"{level_value}\" already "
                  + f"exists for level=\"{level}\""
            )


    # FUNCTION PROPER

    # Informs that the entity is added
    info(
        "Added level -> "
         + f"\"{level_name}\" : [\"{level_code}\", {level_value}]"
    )


# UTILITY FUNCTIONS
def _build_text(text:str, level:str="NOTSET") -> str:
    # INITATION
    prefix = _name_to_level[level][_LEVELS_CODE] + ": "
    
    # CONDITIONS
    if level == "NOTSET":
        prefix = ""

    # FUNCTION PROPER
    return prefix + text
