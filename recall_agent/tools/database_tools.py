import duckdb
import os

# Initialize DuckDB
connection = duckdb.connect()

# Define tool to count recalls for a specific month and year
def count_recalls_by_month_and_year(year: int, month_name: str) -> int:
    """
    Filter and count all recalls for a specific month and year.
    
    Args:
        year: The year to query (e.g., 2026)
        month_name: The name of the month to query (e.g., "May", "January")
    """
    month_map = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }
    
    month_num = month_map.get(month_name.lower().strip())
    if not month_num:
        raise ValueError("Invalid month name provided.")

    return connection.execute(
        """
        SELECT COUNT(*) as "Total Recalls in Period" FROM 'recall_agent/data/HCRSAMOpenData.csv'
        WHERE EXTRACT(year FROM CAST("Last updated" AS DATE)) = $year
        AND EXTRACT(month FROM CAST("Last updated" AS DATE)) = $month
        """,
        {"year": year, "month": month_num}
    ).fetchone()[0]
