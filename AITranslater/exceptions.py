class TranslationError(Exception):
    """
    Exception raised for errors that occur during translation processes.

    Attributes:
        message (str): Explanation of the error encountered.
    """

    def __init__(self, message="An error occurred in the translation process"):
        super().__init__(message)
