import json
from pathlib import Path
from logging import getLogger
from typing import Any
from uuid import uuid4
from typing import Dict, Optional
from fastapi.encoders import jsonable_encoder
from codingchallenge_qa_service.measure import Clock
from contextlib import contextmanager

logger = getLogger(name=__name__)


class Transaction:

    def __init__(self):
        self.transaction_id: str = str(uuid4())
        self.transaction_data = {}
        self.should_store = False
        self.should_update = False
        self.time_request: Optional[Clock] = None  # Add the time_request attribute
        # Load mapping from a JSON file
        current_file_path = Path(__file__).resolve()
        parent_directory = current_file_path.parent
        mapping_file_path = parent_directory / "config" / "transaction_mapping.json"
        with open(mapping_file_path, "r") as file:
            self.MAPPING = json.load(file)

    @contextmanager
    def record(self, field_update: Dict):
        """Updates the transaction nested dictionary on the first two levels.
        * If the Value is a dictionary, it doesn't replace Level 2 dictionary.
          It either replaces old values on Level 2 or creates new entries.
        * If the Value is a string, it replaces the old or creates a new entry on Level 1

        :param field_update: a dictionary contains -to be recorded- updates to the transaction data
        """
        field_update = jsonable_encoder(field_update)
        # record all pairs of updates
        for key, value in field_update.items():
            # make sure each recorded key has a type mapping
            if key not in self.MAPPING["mappings"]["properties"]:
                raise TypeError(f"{key} does not have type mapping")

            # in case of nested objects, change or add values instead of overwriting
            if isinstance(value, dict):
                for nested_key, nested_value in value.items():
                    try:
                        self.transaction_data[key][nested_key] = nested_value
                    except KeyError:
                        self.transaction_data[key] = {}
                        self.transaction_data[key][nested_key] = nested_value
            else:
                # replace old value of the key or create a new key-value pair in the transaction
                self.transaction_data[key] = value

        yield self

    def record_exception(self, exception: Exception):
        """Records the exception in the transaction.

        :param exception: Exception to be recorded
        """
        self.record({"exception": str(exception)})

    def to_dict(self, include_id: bool = True) -> Dict:
        """Transforming all second level dictionaries to json formatted text

        :param include_id: boolean used to include the transaction id to the transaction
        :return: a dictionary with all second level dictionaries and lists serialized as json formatted text
        """
        transaction_dict: Dict[Any, Any] = {}
        if include_id:
            transaction_dict["transaction_id"] = (self.transaction_id,)
        for key in self.transaction_data.keys():
            transaction_dict[key] = (
                self.transaction_data[key].copy()
                if callable(getattr(self.transaction_data[key], "copy", None))
                else self.transaction_data[key]
            )
            if (
                isinstance(transaction_dict[key], dict)
                and self.MAPPING["mappings"]["properties"][key]["type"] == "text"
            ):
                logger.info(f"changing type of {key}")
                transaction_dict[key] = json.dumps(transaction_dict[key])

        return transaction_dict
