from pydantic import BaseModel, Field, field_validator
import re
from typing import ClassVar

class Example(BaseModel):
    example: str = Field(
        ..., 
        title="Ejemplo de ", 
        description="Descripcion de ejemplo", 
        min_length=1, 
        max_length=1000
    )

    # Pattern of permitted characters
    ALLOWED_CHARS_PATTERN: ClassVar[re.Pattern] = re.compile(r"^[a-zA-Z0-9_()\[\]{}<>.,:;+'\"\\|&*!@#^%$=\s-]*$")
    

    @field_validator("example")
    def check_allowed_characters(cls, value: str) -> str:
        """
        Verifica que solo se utilicen caracteres permitidos en el str.
        """
        if not cls.ALLOWED_CHARS_PATTERN.fullmatch(value):
            raise ValueError("El ejemplo contiene caracteres no permitidos.")
        return value
