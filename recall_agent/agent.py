from google.adk.agents.llm_agent import Agent
import duckdb
import os

# initialize DuckDB
connection = duckdb.connect();

# define tool to count recalls from April 2026
def count_April_2026_recalls() -> int:
    """
    Filter and count all recalls from April 2026
    """
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'HCRSAMOpenData.csv')
    return connection.execute(
        f"""
        SELECT COUNT(*) as "Total Recalls in April 2026" FROM '{data_path}'
        WHERE "Last updated" >= '2026-04-01'
        AND "Last updated" < '2026-05-01'
        """).fetchone()[0]


# define the agent
root_agent = Agent(
    model='gemini-2.5-flash',
    name='recall_agent',
    description='A helpful assistant to explore the recalls, advisories and safety alerts from Health Canada.',
    instruction='Answer user questions using the tools provided to you. If you do not have the tools to answer the question, politely let the user know that you cannot answer the question.',
    tools=[count_April_2026_recalls],
)
