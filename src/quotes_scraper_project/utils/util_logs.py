import inspect
import logging
import os
from quotes_scraper_project.config.settings import debug_config

# =========================================================================================
#                                         CONFIG.
# =========================================================================================
LOG_LEVELS = {"debug", "info", "warning", "error", "critical"}
MAX_LOG_MESSAGE_LENGTH = 500  # Maximum size for log messages
DEBUG_MODE = debug_config.debug_mode # default 'true'
# =========================================================================================
#                                        FUNCTIONS
# =========================================================================================
def add_console_handler_to_logger(logger: logging.Logger, formatter: logging.Formatter):
    ## Create console handler 
    stream_handler = logging.StreamHandler()
    ## Set formatter to the console handler
    stream_handler.setFormatter(formatter) 
    ## Add the console handler to the logger
    logger.addHandler(stream_handler) 

def add_file_handler_to_logger(logger: logging.Logger, formatter: logging.Formatter, log_dir:str, log_file_name:str):
    ## Construct log file path
    log_file_path = os.path.join(log_dir, log_file_name)
    ## Create file handler
    file_handler = logging.FileHandler(log_file_path)
    ## Set formatter to the file handler
    file_handler.setFormatter(formatter) 
    ## Add the file handler to the logger
    logger.addHandler(file_handler)  

def write_log(log_level:str, log_msg:str, write_log_in_file:bool=None, log_dir:str=None,log_file_name:str=None):
    """
    Write a log message to the console and /or a log file, depending on the specified parameters.
    - Parameters:

    log_level : str
        The severity of the log message. Common log levels include 'debug', 'info', 'warning', 'error', 'critical'.
        This determines the type of message being logged and can influence the log output format.
    
    log_msg : str
        The message to be logged. This is the actual content that will be written to the log.
    
    write_log_in_file : bool, optional
        If set to True, the log message will be written to a log file. If None, the default behavior is 
        to log only to the console (standard output). If False, it will not write to the file.
    
    log_dir : str, optional
        The directory where the log file should be created or appended to. This argument is required if `write_log_in_file` is True.
        If not, log_dir must not be set (or must be equals None).
    
    log_file_name : str, optional
        The name of the log file (without extension) where the log message should be saved. This argument is required 
        if `write_log_in_file` is True. If not, log_file_name must not be set (or must be equals None).

    - Returns:
    None
        The function does not return any value. It performs logging actions based on the provided arguments.
    """
    # ========================== Create a logger ===========================
    logger = logging.getLogger('my_logger')
        
    # ========= Configure environment logging based on debug_mode ==========
    if DEBUG_MODE == "true":
        logger.setLevel(logging.DEBUG) 
    else:
        logger.setLevel(logging.INFO) 

    # =========================== Set Formatter ============================
    formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')

    try:
        # ============================ Check inputs ============================
        # ===== log_level:
        ## value
        if log_level not in LOG_LEVELS:
            raise ValueError(f"log level must be one of this list {LOG_LEVELS}")
        # ===== log_msg:
        ## type
        if not isinstance(log_msg, str):
            raise TypeError(f"log message must be a string not {type(log_msg)}")
        ## value
        if log_msg.strip() == "":
            raise ValueError("log message must not be empty")
        ## length
        if len(log_msg) > MAX_LOG_MESSAGE_LENGTH:
            log_msg = log_msg[:MAX_LOG_MESSAGE_LENGTH]+ '... (message truncated)'
        # ===== write_log_in_file & log_dir & log_file_name:
        if write_log_in_file != None:
            ## type
            if not isinstance(write_log_in_file, bool):
                raise TypeError(f"write_log_in_file value must be a boolean not {type(write_log_in_file)}")
            if write_log_in_file == True:
                ## check log_dir 
                #- type
                if not isinstance(log_dir, str):
                    raise TypeError(f"write_log_in_file is True => log dir must be a string not {type(log_dir)}")
                #- existance
                if not os.path.isdir(log_dir):
                    raise FileNotFoundError(f"write_log_in_file is True => log dir not found: '{log_dir}'")
                ## check log_file_name
                #- type
                if not isinstance(log_file_name, str):
                    raise TypeError(f"write_log_in_file is True => log file name must be a string not {type(log_file_name)}")
                #- value
                if log_file_name.strip() == "":
                    raise ValueError("write_log_in_file is True => log file name must not be empty")
            else:
                ## check log_dir
                if log_dir != None:
                    raise ValueError("write_log_in_file is False => log dir must not be set (or must equals None)")
                ## check log_file_name
                if log_file_name != None:
                    raise ValueError("write_log_in_file is False => log file name must not be set (or must equals None)")
        else:
            ## check log_dir
            if log_dir != None:
                raise ValueError("write_log_in_file is None => log dir must not be set (or must equals None)")
            ## check log_file_name
            if log_file_name != None:
                raise ValueError("write_log_in_file is None => log file name must not be set (or must equals None)")
 
        # ================ Console: write logs (automatically) =================
        add_console_handler_to_logger(logger, formatter)

        # ======================== Log file: write logs ========================
        if write_log_in_file:
            add_file_handler_to_logger(logger, formatter, log_dir, log_file_name)

        # ===== Write log message (on console or on both console and file) =====
        ## Get the current stack frame
        frame = inspect.stack()[1]  # [1] gets the caller frame (0 would be the current function)
        ## Extract the file name and line number
        file_name = frame.filename
        line_number = str(frame.lineno)
        ## Write log msg
        if log_level == "debug": 
            log_msg = log_msg + " - [file:" + file_name + ", line:" + line_number + "]."
            logger.debug(log_msg)
        if log_level == "info":
            logger.info(log_msg)
        if log_level == "warning":
            logger.warning(log_msg)
        if log_level == "error":
            logger.error(log_msg) 
        if log_level == "critical":
            logger.critical(log_msg)

    except Exception as e:
        # ===== Create log msg based on debug mode
        log_msg = f"logging module failure: {e}"

        if DEBUG_MODE == "true":
            ## Get the current stack frame
            frame = inspect.stack()[1]  # [1] gets the caller frame (0 would be the current function)
            ## Extract the file name and line number
            file_name = frame.filename
            line_number = str(frame.lineno)
            ## Construct log msg
            log_msg = log_msg + " - [file:" + file_name + ", line:" + line_number + "]."

        # ===== Console: write logs (automatically) 
        add_console_handler_to_logger(logger, formatter)

        # ===== Write log
        logger.error(log_msg)



if __name__ == "__main__":
    print("-> in ztest.py\n")

    write_log("warning", "message log", None, None, "toto")


