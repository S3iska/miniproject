# pylint: disable=invalid-name

from repositories.ref_repository import get_refs
from app import app
from config import db

class RefLibrary:
    def __init__(self):
        pass

    def get_refs_from_database(self, **filters):
        """
        Fetch refs based on the provided filter criteria.

        Args:
            filters: Keyword arguments to filter refs (e.g., author="John Doe").

        Returns:
            list: List of dictionaries representing refs.
        """
        with app.app_context():
            refs = get_refs(db, **filters)
            # Convert Ref objects into dictionaries for use in Robot Framework
            return [vars(ref) for ref in refs]
