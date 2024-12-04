from dataclasses import dataclass, fields
from typing import Optional


def get_required_fields(dataclass_obj):
    required_fields = []
    for field in fields(dataclass_obj):
        if ( field.default is None and
            field.default_factory is field.default_factory ):
            continue  # Skip optional fields
        required_fields.append(field.name)
    return required_fields


def get_optional_fields(dataclass_obj):
    optional_fields = []
    for field in fields(dataclass_obj):
        if ( field.default is not None or
            field.default_factory is not field.default_factory ):
            continue  # Skip required fields
        optional_fields.append(field.name)
    return optional_fields


@dataclass
class Article:
    author: str
    title: str
    journal: str
    year: int
    volume: Optional[int] = None
    number: Optional[int] = None
    pages: Optional[str] = None
    month: Optional[str] = None
    note: Optional[str] = None


@dataclass
class Book:
    title: str
    publisher: str
    year: int
    author: Optional[str] = None
    editor: Optional[str] = None
    volume: Optional[int] = None
    number: Optional[int] = None
    series: Optional[str] = None
    address: Optional[str] = None
    edition: Optional[str] = None
    month: Optional[str] = None
    note: Optional[str] = None


@dataclass
class InProceedings:
    author: str
    title: str
    booktitle: str
    year: int
    editor: Optional[str] = None
    volume: Optional[int] = None
    number: Optional[int] = None
    series: Optional[str] = None
    pages: Optional[str] = None
    address: Optional[str] = None
    month: Optional[str] = None
    organization: Optional[str] = None
    publisher: Optional[str] = None
    note: Optional[str] = None
