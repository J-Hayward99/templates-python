# LEGAL AND DOCUMENTATION
# Copyright (c) 2023 James Hayward


# ============================================================================ #
#   IMPORTS
# ============================================================================ #
# OFFICIAL MODULES
import sys
import re

# PERSONAL MODULES



# ============================================================================ #
#   DEFINITIONS
# ============================================================================ #
# PUBLIC


# PRIVATE
_LEVELS_CODE    = 0
_LEVELS_VALUE   = 1

_CODE_LENGTH    = 4

# DEFAULTS
_DEFAULT_LEVEL_VALUE    = 20

# ============================================================================ #
#   LOOK-UP TABLES 
# ============================================================================ #



# ============================================================================ #
#   HASHMAPS
# ============================================================================ #
# INITIATION


# HARD-CODED HASHMAPS
_name_to_level  = {
    "EXIT"      : ["EXIT", 60],                                                     # Used for System Exits
    "CRITICAL"  : ["CRIT", 50],                                                     # Used for Critical Errors: Basically exit without sys.exit
    "ERROR"     : ["ERRO", 40],                                                     # Used for Errors
    "WARNING"   : ["WARN", 30],                                                     # Used for Warnings 
    "MAIN"      : ["MAIN", 24],                                                     # Used for the Main sequence
    "CHECK"     : ["CHCK", 23],                                                     # Used for the Check sequence
    "BOOT"      : ["BOOT", 22],                                                     # Used for the Boot sequence
    "PROGRAM"   : ["PROG", 21],                                                     # Used for the Program Sequence
    "INFO"      : ["INFO", 20],                                                     # Used for Additional Info
    "DEBUG"     : ["DBUG", 10],                                                     # Used for Debug Messages
    "NOTSET"    : ["NONE", 0 ]                                                      # Default case
}                                                                                   # "LEVEL":str : ["BOOTCODE":str, NUMERICAL_LEVEL:int]

_settings       = {
    "level_threshold"   : _DEFAULT_LEVEL_VALUE
}


# ============================================================================ #
#   FUNCTIONS
# ============================================================================ #
# MAIN FUNCTIONS
# Print Messages Block
def exit(message:str) -> None:
    sys.exit(_build_text(message, level="EXIT"))

def critical(message:str) -> None:
    _build_text(message, level="CRITICAL")

def error(message:str) -> None:
    sys.exit(_build_text(message, level="ERROR"))

def warning(message:str) -> None:
    _build_text(message, level="WARNING")

def info(message:str) -> None:
    (_build_text(message, level="INFO"))

def debug(message:str) -> None:
    _build_text(message, level="DEBUG")

def check(message:str) -> None:
    _build_text(message, level="CHECK")

def main(message:str) -> None:
    _build_text(message, level="MAIN")

def boot(message:str) -> None:
    _build_text(message, level="BOOT")

def program(message:str) -> None:
    _build_text(message, level="PROGRAM")

def none(message:str) -> None:
    _build_text(message, level="NOTSET")


# Level Handler Block
def change_threshold_level(new_level:str|int=_DEFAULT_LEVEL_VALUE):
    program(_change_threshold_level(new_level))

def change_threshold_level(new_level:str|int=_DEFAULT_LEVEL_VALUE):
    boot(_change_threshold_level(new_level))


# UTILITY FUNCTIONS
def _build_text(text:str, level:str="NOTSET") -> None:
    # INITATION
    prefix = _name_to_level[level][_LEVELS_CODE] + ": "                             #   # Appends the colon to complete the prefix
    
    # GUARD CLAUSES
    if level == "NOTSET":                                                           #   # NOTSET removes prefix
        prefix = ""

    text = str(text)

    # FUNCTION PROPER
    if _check_enabled_level(level):
        if level == "EXIT" or level == "ERROR":                                     #   # Checks that the level is exitable
            sys.exit(prefix + text)
        else:
            print(prefix + text)
    
def _update_settings(setting_name:str, value:int) -> str:
    # Guard Clauses
    if not isinstance(value, int):
        error("Bad Value -> Value is not int")
    
    if _settings.get(setting_name) == None:
        error("Bad Setting Name -> Name is not in Settings")
    
    # Change setting
    temp_setting_value = _settings[setting_name]
    
    _settings[setting_name] = value
    
    return (f"Setting '{setting_name}' changed from "
        + f"'{temp_setting_value}' to '{value}'")

def _check_enabled_level(level_to_check:str) -> bool:
    # INITATION
    level_value         = _name_to_level[level_to_check][_LEVELS_VALUE]
    settings_threshold  = _settings["level_threshold"]

    # BEHAVIOUR
    if level_value >= settings_threshold:                                           #   # Allows statement if it's above the threshold
        return True
    
    return False

def _change_threshold_level(new_level:str|int=_DEFAULT_LEVEL_VALUE):
    # Name Conversion
    if isinstance(new_level, str) and (new_level in _name_to_level):
        new_level = _name_to_level[new_level][1]

    # Guard Clauses
    if not isinstance(new_level, int):
        error("Threshold value not recognised -> Value is not an integer -> "
            + str(new_level))
    
    if new_level < 0:
        error("Bad threshold value -> Value is below zero -> " + str(new_level))
    
    return _update_settings("level_threshold", new_level)

