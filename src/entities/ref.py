from dataclasses import dataclass

@dataclass
class Ref:
    id: int = None
    ref_type: str = None
    ref_name: str = None
    author: str = None
    title: str = None
    year: int = None
    publisher: str = None
