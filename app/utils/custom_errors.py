# Standard Library imports

# Core Flask imports

# Third-party imports

# App imports


class Error(Exception):
    message = "Error"
    internal_error_code = 99999

    def __init__(self, value=""):
        if not hasattr(self, "value"):
            self.value = value

    def __str__(self):
        return repr(self.value)
