class FactoryError(ValueError):
    """Exception raised for errors in the factory create"""

    def __init__(self, factory_key: str) -> None:
        self.factory_key = factory_key
        super().__init__(f"Invalid factory key: {factory_key}!")
