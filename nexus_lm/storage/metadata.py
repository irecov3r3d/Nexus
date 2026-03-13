import sqlite3
import json
from typing import Dict, Any, Optional

class MetadataStore:
    """
    Local-first SQLite metadata persistence.
    """
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._initialize_schema()

    def _initialize_schema(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                report_data TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_report(self, report: Dict[str, Any]):
        self.cursor.execute(
            'INSERT INTO reports (report_data) VALUES (?)',
            (json.dumps(report),)
        )
        self.conn.commit()

    def get_latest_report(self) -> Optional[Dict[str, Any]]:
        self.cursor.execute(
            'SELECT report_data FROM reports ORDER BY id DESC LIMIT 1'
        )
        row = self.cursor.fetchone()
        if row:
            return json.loads(row[0])
        return None

    def clear_all(self):
        self.cursor.execute('DELETE FROM reports')
        self.conn.commit()

    def __del__(self):
        self.conn.close()
