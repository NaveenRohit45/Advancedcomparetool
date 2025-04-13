# tests/test_table_comparison.py

from document_comparator.table_comparison import compare_tables

def test_compare_tables():
    # Simulate table data (could be from a PDF or a CSV file)
    table_1 = [
        ["Name", "Age", "Occupation"],
        ["Alice", "30", "Engineer"],
        ["Bob", "25", "Designer"]
    ]

    table_2 = [
        ["Name", "Age", "Occupation"],
        ["Alice", "30", "Engineer"],
        ["Bob", "25", "Designer"]
    ]

    result = compare_tables(table_1, table_2)

    # Expecting True since the tables are the same
    assert result == True, "Table comparison failed!"

def test_compare_tables_with_diff():
    # Simulate tables with differences
    table_1 = [
        ["Name", "Age", "Occupation"],
        ["Alice", "30", "Engineer"],
        ["Bob", "25", "Designer"]
    ]

    table_2 = [
        ["Name", "Age", "Occupation"],
        ["Alice", "30", "Engineer"],
        ["Bob", "26", "Designer"]
    ]

    result = compare_tables(table_1, table_2)

    # Expecting False due to difference in the "Age" column
    assert result == False, "Table comparison failed!"
