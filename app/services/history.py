# app/services/history.py

import json

from datetime import datetime

from pathlib import Path


class History:

    def __init__(self):

        self.data_directory = (
            Path.home()
            / ".transcriberx"
        )

        self.data_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.history_file = (
            self.data_directory
            / "history.json"
        )

    # =========================================================
    # Load History
    # =========================================================

    def load_history(self):

        if not self.history_file.exists():

            return []

        try:

            with open(
                self.history_file,
                "r",
                encoding="utf-8",
            ) as file:

                data = json.load(
                    file
                )

                if isinstance(
                    data,
                    list,
                ):

                    return data

                return []

        except (
            json.JSONDecodeError,
            OSError,
        ):

            return []

    # =========================================================
    # Save History
    # =========================================================

    def save_history(
        self,
        history,
    ):

        with open(
            self.history_file,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                history,
                file,
                ensure_ascii=False,
                indent=4,
            )

    # =========================================================
    # Add Record
    # =========================================================

    def add_record(
        self,
        file_name,
        transcript,
    ):

        history = self.load_history()

        record = {
            "id": datetime.now().strftime(
                "%Y%m%d%H%M%S%f"
            ),

            "file_name": file_name,

            "date_time": datetime.now().astimezone().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "transcript": transcript,
        }

        history.insert(
            0,
            record,
        )

        self.save_history(
            history
        )

        return record

    # =========================================================
    # Get All
    # =========================================================

    def get_all(self):

        return self.load_history()

    # =========================================================
    # Get Record
    # =========================================================

    def get_record(
        self,
        record_id,
    ):

        history = self.load_history()

        for record in history:

            if record.get("id") == record_id:

                return record

        return None

    # =========================================================
    # Delete Record
    # =========================================================

    def delete_record(
        self,
        record_id,
    ):

        history = self.load_history()

        new_history = [
            record
            for record in history
            if record.get("id") != record_id
        ]

        self.save_history(
            new_history
        )