from flask import current_app
from repositories.ref_repository import get_selected_refs
from app import app

class RefLibrary:
    def __init__(self):
        pass
    
    def get_refs(self, **filters):
        """
        Fetch refs based on the provided filter criteria.

        Args:
            filters: Keyword arguments to filter refs (e.g., author="John Doe").

        Returns:
            list: List of dictionaries representing refs.
        """
        with app.app_context():
            refs = get_selected_refs(**filters)
            # Convert Ref objects into dictionaries for easier assertion in Robot Framework
            return [vars(ref) for ref in refs]