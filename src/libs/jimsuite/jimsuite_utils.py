"""
This folder is used to hold the code that's inherent to the project

"""

# ============================================================================ #
#   IMPORTS
# ============================================================================ #
# OFFICIAL MODULES
import configparser                                                                 # For the config function
import os                                                                           # Checking existence of files


# PERSONAL MODULES
import libs.jimsuite.jimsuite_logger as jim_log

CONFIG_LOCATION = ""
CHECKS_LOCATION = ""

# ============================================================================ #
#   CODE
# ============================================================================ #
def run_file_check() -> None:                                                       # Checks the list of files to ensure all are there
    # INITIALISE
    flag_missing_files = False                                                      #   # Flag that triggers if there's a missing file
    list_missing_files = []                                                         #   # Archives a list of missing files

    # OPEN FILE
    with open(CHECKS_LOCATION, "r") as file:
        # LINES TO LIST
        file_lines = file.readlines()

        # CHECK LINES
        for line in file_lines:
            # REMOVE NEWLINE SPECIAL CHARACTER
            line = line.strip("\n")
            
            # CONDITIONS
            # If the Line is Empty
            if line == "":
                continue

            # If the Line is a Comment
            if line.strip().startswith("#"):                                        #   # Removes whitespace then checks if the first is #
                continue
            
            # GET EXISTENCE
            existence = os.path.exists(line)                                        #   # Checks the existence of the file

            # FLAG TRIGGER OF MISSING FILES
            if not existence:                                                       #   # If the files are missing
                flag_missing_files = True
                list_missing_files.append(line)

            
            # PRINT THE EXISTANCE OF FILE
            if get_config_value("Included", "show_checks") == "True":
                jim_log.check(f"Existence of \"{line}\" -> {existence}")
        
        # MISSING TRIGGER
        if flag_missing_files:
            # STATE ISSUE
            jim_log.check("Failed Check -> Missing Files")
            
            # LIST FILE
            for file in list_missing_files:
                jim_log.check(f"Missing File -> \"{file}\"")
            
            # SHUTS DOWN PROGRAM
            jim_log.exit("Stopping Program")
        
        jim_log.check("Checks Passed")




def get_config_value(section:str, value:str) -> str:                                # Streamlines the config value acquisition
    # CONFIG INITIATION
    config = configparser.ConfigParser()                                            #   # Initiates Parser
    config.read(CONFIG_LOCATION)                                                    #   # Hardcoded config.ini file

    # RETURN
    return config[section][value].strip("\"")                                       #   # Removes un-needed ""

def set_config_location(location:str) -> None:
    if not isinstance(location, str):
        location = str(location)
    
    if not os.path.isfile(location):
        jim_log.error("Config location does not exist -> " + location)
    
    global CONFIG_LOCATION
    CONFIG_LOCATION = location
    jim_log.boot(f"Set config.ini location to '{location}'")

def set_checks_location(location:str) -> None:
    if not isinstance(location, str):
        location = str(location)
    
    if not os.path.isfile(location):
        jim_log.error(".checks location does not exist -> " + location)
    
    global CHECKS_LOCATION
    CHECKS_LOCATION = location
    jim_log.boot(f"Set .checks location to '{location}'")

def convert_config_type(section:str, value:str, new_type:str):
    # INITIATE
    config_value        = get_config_value(section, value)
    data_types          = ["str", "int", "float", "bool"]
    
    # CHECK    
    if new_type not in data_types:
        jim_log.error("\"convert_config_type\" "
                 + f"-> Type is not Valid Type -> type=\"{new_type}\"")

    # CONVERT
    try:
        if new_type == "str":
            return str(config_value)
        
        if new_type == "int":
            return int(config_value)
        
        if new_type == "float":
            return float(config_value)
        
        if new_type == "bool":
            return bool(config_value)
    
    except TypeError:
        jim_log.error("\"convert_config_type\" -> Invalid Type Conversion "
                 + f"-> \"{config_value}\" cannot be \"{new_type}\"")

