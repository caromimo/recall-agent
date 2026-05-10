import duckdb
import os

# Initialize DuckDB
connection = duckdb.connect()

# Define tool to count recalls from April 2026
def count_April_2026_recalls() -> int:
    """
    Filter and count all recalls from April 2026
    """
    return connection.execute(
        """
        SELECT COUNT(*) as "Total Recalls in Period" FROM 'recall_agent/data/HCRSAMOpenData.csv'
        WHERE "Last updated" >= $period_start
        AND "Last updated" < $period_end
        """,
        {"period_start": "2026-04-01", "period_end": "2026-05-01"}
    ).fetchone()[0]
