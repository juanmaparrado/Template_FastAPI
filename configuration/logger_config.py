import logging
from datetime import datetime

# define ANSI color codes for different log levels
LEVEL_COLORS = {
    "DEBUG": "\033[94m",  # Blue
    "INFO": "\033[92m",   # Green
    "WARNING": "\033[93m", # Yellow
    "ERROR": "\033[91m",   # Red
    "CRITICAL": "\033[95m" # Magenta
}
RESET_COLOR = "\033[0m"

# define a custom log formatter
class CustomFormatter(logging.Formatter):
    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt

    def format(self, record):
        # get the log level name and apply color
        level_name = record.levelname
        level_color = LEVEL_COLORS.get(level_name, "")
        level_colored = f"{level_color}{level_name}{RESET_COLOR}"

        # format the current time in HH:MM:SS
        current_time = datetime.now().strftime("%H:%M:%S")

        # replace placeholders with custom values
        log_message = self.fmt.format(
            level=level_colored,
            time=current_time,
            message=record.getMessage()
        )

        # return the formatted message
        return log_message

# ------------------------------------------------------------------------

# declare custom formatter instance
custom_format = "{level} | {time}:\t{message}"
formatter = CustomFormatter(custom_format)

# configure handler
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# configure logger
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# avoid message duplication
logger.propagate = False
