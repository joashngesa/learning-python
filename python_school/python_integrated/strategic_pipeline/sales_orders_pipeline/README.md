PIPELINE DRILL EXERCISES

🚫Data Has the Following Errors:
    negative unit_cost
    zero quantity
    duplicate order_id + supplier_id
    missing supplier_name
    invalid unit_cost
    missing quantity

🗺️pipeline map:
    1. Load config from .env
    2. Read and parse raw supplier orders
    3. Convert unit_cost and quantity
    4. Split valid and invalid records
    5. Extract duplicate records
    6. Transform valid records by adding total_cost
    7. Summarize total_cost by supplier_name and category
    8. Write clean, invalid, duplicate, and summary CSV files
    9. Print final pipeline report

