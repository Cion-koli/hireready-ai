"""
Software Engineer Question Bank - SQL Technology
25 distinct technical questions covering query writing, joins, subqueries, window functions, indexing, and ACID.
"""

SOFTWARE_ENGINEER_SQL_QUESTIONS = [
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "database_basics",
        "difficulty": "easy",
        "question_text": "Explain the difference between a Primary Key and a Unique Key in relational databases. Can a table have multiple Unique Keys or multiple Primary Keys?",
        "expected_answer": "A Primary Key uniquely identifies each row in a table and cannot contain NULL values; a table can have only one Primary Key (which can be composite). A Unique Key also enforces uniqueness across rows but permits NULL values (usually one or more depending on RDBMS); a table can have multiple Unique Keys.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is a Foreign Key constraint, and what happens when ON DELETE CASCADE is configured?",
        "code_snippet": "CREATE TABLE users (\n  id SERIAL PRIMARY KEY,\n  email VARCHAR(255) UNIQUE NOT NULL\n);"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "filtering_and_grouping",
        "difficulty": "easy",
        "question_text": "Explain the difference between the WHERE clause and the HAVING clause in SQL. Why can't aggregate functions like COUNT() or AVG() be placed directly in a WHERE clause?",
        "expected_answer": "WHERE filters individual rows before grouping and aggregation takes place. HAVING filters grouped rows after the GROUP BY clause and aggregation have been evaluated. Aggregates cannot be in WHERE because the groups have not yet been formed when WHERE is processed in the SQL logical query processing pipeline.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the logical query processing order (FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT)?",
        "code_snippet": "SELECT department_id, COUNT(*) as emp_count\nFROM employees\nWHERE salary > 50000\nGROUP BY department_id\nHAVING COUNT(*) > 5;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "joins",
        "difficulty": "medium",
        "question_text": "Explain the four primary SQL JOIN types: INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, and FULL OUTER JOIN. What happens to unmatched rows in each?",
        "expected_answer": "INNER JOIN returns only rows with matching values in both tables. LEFT JOIN returns all rows from the left table, with NULLs for unmatched right table columns. RIGHT JOIN returns all rows from the right table, with NULLs for unmatched left columns. FULL OUTER JOIN returns all rows from both tables, filling with NULL where matches don't exist.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is a CROSS JOIN (Cartesian product), and how many rows does it return when joining a table of N rows with M rows?",
        "code_snippet": "SELECT u.name, o.order_id\nFROM users u\nLEFT JOIN orders o ON u.id = o.user_id;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "null_handling",
        "difficulty": "easy",
        "question_text": "How does SQL handle NULL values in three-valued logic (TRUE, FALSE, UNKNOWN)? Why must you use 'IS NULL' instead of '= NULL', and what does COALESCE() do?",
        "expected_answer": "NULL represents an unknown or absent value. Any equality comparison with NULL (e.g. col = NULL) evaluates to UNKNOWN, which evaluates as false in WHERE clauses; therefore 'IS NULL' or 'IS NOT NULL' must be used. COALESCE(val1, val2, ...) returns the first non-null argument in its list.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do aggregate functions like COUNT(column_name) handle NULLs compared to COUNT(*)?",
        "code_snippet": "SELECT id, COALESCE(phone_number, 'N/A') as contact\nFROM customers\nWHERE deleted_at IS NULL;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "subqueries",
        "difficulty": "medium",
        "question_text": "What is a Correlated Subquery in SQL, how does it differ from a standard independent subquery, and why can it become a performance bottleneck?",
        "expected_answer": "A standard subquery executes once independently and passes its results to the outer query. A correlated subquery references columns from the outer query table, requiring the database engine to re-evaluate the inner query row-by-row for every candidate row evaluated in the outer query, leading to O(N*M) execution unless optimized by the query planner into a JOIN.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How can you rewrite a correlated subquery using an INNER JOIN or a window function?",
        "code_snippet": "SELECT e1.name, e1.salary, e1.department_id\nFROM employees e1\nWHERE e1.salary > (\n  SELECT AVG(e2.salary)\n  FROM employees e2\n  WHERE e2.department_id = e1.department_id\n);"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "common_table_expressions",
        "difficulty": "medium",
        "question_text": "What is a Common Table Expression (CTE) defined with the 'WITH' clause? How does it improve query readability over nested subqueries, and what is a Recursive CTE?",
        "expected_answer": "A CTE defines a temporary named result set within the execution scope of a single SELECT, INSERT, UPDATE, or DELETE statement. It replaces deeply nested subqueries with readable, modular logic. A Recursive CTE references itself, allowing traversal of hierarchical or graph data structures (e.g. organizational manager-employee hierarchies, categories, bill of materials).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does a recursive CTE prevent infinite loops (termination condition)?",
        "code_snippet": "WITH RegionalSales AS (\n  SELECT region, SUM(amount) as total_sales\n  FROM sales GROUP BY region\n)\nSELECT region, total_sales FROM RegionalSales WHERE total_sales > 100000;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "window_functions_ranking",
        "difficulty": "hard",
        "question_text": "Explain the differences between ROW_NUMBER(), RANK(), and DENSE_RANK() window functions in SQL when ranking identical tie values.",
        "expected_answer": "ROW_NUMBER() assigns a unique sequential integer (1, 2, 3, 4) to every row regardless of ties. RANK() assigns the same rank to identical values, but skips subsequent ranks for the count of ties (e.g. ties at 2 lead to 1, 2, 2, 4). DENSE_RANK() assigns identical ranks to ties without skipping subsequent numbers (1, 2, 2, 3).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you write a query to find the 2nd highest salary using DENSE_RANK()?",
        "code_snippet": "SELECT name, salary,\n  ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num,\n  RANK() OVER (ORDER BY salary DESC) as rnk,\n  DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rnk\nFROM employees;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "window_functions_aggregation",
        "difficulty": "medium",
        "question_text": "How do window functions differ from GROUP BY aggregations? Explain the 'OVER (PARTITION BY ... ORDER BY ...)' clause.",
        "expected_answer": "GROUP BY collapses multiple rows into a single summary row, losing access to individual row attributes. Window functions compute aggregate or ranking calculations across a defined set of rows ('window') while retaining the individual identity and output of every single row. PARTITION BY defines the sub-groups; ORDER BY defines the sequence within each partition for cumulative running totals or ranking.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do LAG() and LEAD() window functions allow comparing the current row with prior or subsequent rows?",
        "code_snippet": "SELECT date, amount,\n  SUM(amount) OVER (PARTITION BY account_id ORDER BY date) as running_balance\nFROM transactions;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "case_expressions",
        "difficulty": "easy",
        "question_text": "How does the CASE expression work in SQL? Write a query that categorizes employee salaries into 'Low', 'Medium', and 'High' tiers.",
        "expected_answer": "CASE evaluates conditions sequentially and returns the corresponding THEN expression on the first truthy condition, or the ELSE value if no conditions match. It can be used anywhere an expression is valid (SELECT, WHERE, ORDER BY, GROUP BY).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between a simple CASE (CASE expr WHEN val ...) and a searched CASE (CASE WHEN condition ...)?",
        "code_snippet": "SELECT name, salary,\n  CASE\n    WHEN salary < 50000 THEN 'Low'\n    WHEN salary BETWEEN 50000 AND 100000 THEN 'Medium'\n    ELSE 'High'\n  END as salary_tier\nFROM employees;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "indexing_fundamentals",
        "difficulty": "hard",
        "question_text": "How does a B-Tree index work in a relational database? What is the difference between a Clustered Index and a Non-Clustered (Secondary) Index?",
        "expected_answer": "A B-Tree (balanced tree) index maintains sorted key-value pairs, enabling O(log N) lookups, range scans, and sorting. A Clustered Index dictates the physical on-disk storage order of the actual table rows (a table can have only one clustered index, often the primary key). A Non-Clustered index is a separate B-Tree structure storing the indexed column values and row locators (pointers) pointing back to the clustered index or heap data row.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is a 'Covering Index' and how does it prevent expensive bookmark/table lookups?",
        "code_snippet": "CREATE INDEX idx_users_email ON users(email);\nCREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date);"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "acid_properties",
        "difficulty": "medium",
        "question_text": "Explain the ACID properties of database transactions: Atomicity, Consistency, Isolation, and Durability. Give a concrete banking example where failure of any property causes catastrophic error.",
        "expected_answer": "Atomicity: All-or-nothing (if debit succeeds but credit fails during transfer, entire transaction rolls back). Consistency: Transactions transition the database from one valid state to another, enforcing all schema constraints. Isolation: Concurrent transactions execute without interfering with each other's uncommitted intermediate state. Durability: Once committed, updates survive server crashes or power loss via write-ahead logging (WAL).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does a Write-Ahead Log (WAL) guarantee durability before data pages are flushed to disk?",
        "code_snippet": "BEGIN TRANSACTION;\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\nCOMMIT;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "transaction_isolation",
        "difficulty": "hard",
        "question_text": "Explain the four standard ANSI SQL Transaction Isolation Levels and the concurrency phenomena they prevent: Dirty Read, Non-Repeatable Read, and Phantom Read.",
        "expected_answer": "1) Read Uncommitted: allows Dirty Reads (reading uncommitted data). 2) Read Committed: prevents Dirty Reads; allows Non-Repeatable Reads (reading changed data committed by another tx mid-way). 3) Repeatable Read: prevents Dirty and Non-Repeatable Reads; allows Phantom Reads (new rows inserted by another tx appearing in range scans). 4) Serializable: strictest isolation, prevents all phenomena via locking or serializable snapshot isolation (SSI).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does Multi-Version Concurrency Control (MVCC) in PostgreSQL enable readers to not block writers?",
        "code_snippet": "SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "normalization",
        "difficulty": "medium",
        "question_text": "Explain Database Normalization through 1NF, 2NF, and 3NF. Why do database designers sometimes intentionally denormalize tables in production reporting systems?",
        "expected_answer": "1NF: Atomic column values (no arrays or repeating groups) and a primary key. 2NF: In 1NF and no partial dependencies (every non-key column depends on the whole candidate key). 3NF: In 2NF and no transitive dependencies (non-key columns depend only on the primary key, not on other non-key columns). Denormalization is used in read-heavy analytics/data warehouses to reduce expensive multi-table joins and optimize query read throughput.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Boyce-Codd Normal Form (BCNF)?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "query_optimization",
        "difficulty": "hard",
        "question_text": "How do you analyze a slow SQL query using EXPLAIN or EXPLAIN ANALYZE? What does a Sequential Scan (Table Scan) vs Index Scan indicate, and what are common causes of index suppression?",
        "expected_answer": "EXPLAIN displays the execution plan cost and operation tree; EXPLAIN ANALYZE executes the query to return actual execution times and row counts. Sequential scan reads all disk pages sequentially, slow for large tables unless retrieving a large fraction of the table. Index suppression occurs when: applying functions on indexed columns (WHERE YEAR(created_at) = 2026), type mismatch forcing implicit casting, or leading wildcards (LIKE '%text').",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does a composite index on (A, B) fail to help queries that only filter on column B (Leftmost Prefix Rule)?",
        "code_snippet": "EXPLAIN ANALYZE\nSELECT * FROM orders\nWHERE customer_id = 42\nORDER BY created_at DESC\nLIMIT 10;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "views_and_materialized_views",
        "difficulty": "medium",
        "question_text": "What is the difference between a standard SQL View and a Materialized View? How does REFRESH MATERIALIZED VIEW work?",
        "expected_answer": "A standard View is a saved virtual query; it stores no physical data on disk and re-runs its underlying query every time it is referenced. A Materialized View physically caches and persists the query results on disk like a table, providing ultra-fast read performance for heavy aggregate queries. However, it must be periodically updated with REFRESH MATERIALIZED VIEW to synchronize with underlying table changes.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between REFRESH MATERIALIZED VIEW and REFRESH MATERIALIZED VIEW CONCURRENTLY?",
        "code_snippet": "CREATE MATERIALIZED VIEW monthly_sales_summary AS\nSELECT date_trunc('month', sale_date) as month, SUM(amount) as total\nFROM sales GROUP BY 1;\n\nREFRESH MATERIALIZED VIEW CONCURRENTLY monthly_sales_summary;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "upsert_patterns",
        "difficulty": "medium",
        "question_text": "How do you perform an UPSERT (Insert or Update if already exists) in modern SQL? Compare PostgreSQL 'ON CONFLICT DO UPDATE' with MySQL 'ON DUPLICATE KEY UPDATE'.",
        "expected_answer": "An UPSERT inserts a new record, but if a unique constraint or primary key collision occurs, it atomically updates the existing record instead of throwing an error. PostgreSQL uses 'INSERT INTO table VALUES (...) ON CONFLICT (key) DO UPDATE SET col = EXCLUDED.col'. MySQL uses 'INSERT INTO table VALUES (...) ON DUPLICATE KEY UPDATE col = VALUES(col)'.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the standard ANSI SQL MERGE INTO statement?",
        "code_snippet": "INSERT INTO user_scores (user_id, score)\nVALUES (42, 95)\nON CONFLICT (user_id)\nDO UPDATE SET score = EXCLUDED.score, updated_at = NOW();"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "stored_procedures_triggers",
        "difficulty": "medium",
        "question_text": "Compare Stored Procedures and User-Defined Functions (UDFs) in SQL. What is a Database Trigger and when should business logic be kept in the application layer instead?",
        "expected_answer": "UDFs calculate and return a value (scalar or table) and can be invoked inside SELECT statements, but generally cannot execute transaction control (COMMIT/ROLLBACK). Stored Procedures perform procedural batch logic and can manage transactions. Triggers automatically execute in response to events (INSERT, UPDATE, DELETE). Complex business logic is often preferred in application code for easier version control, automated unit testing, and horizontal scaling.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is an AFTER INSERT trigger versus a BEFORE INSERT trigger?",
        "code_snippet": "CREATE TRIGGER update_audit_log\nAFTER UPDATE ON accounts\nFOR EACH ROW\nEXECUTE FUNCTION log_account_change();"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "practical_query_second_highest",
        "difficulty": "medium",
        "question_text": "Write a query to find the second highest salary from an Employee table. Ensure the query gracefully returns NULL if there is only one employee or all salaries are equal.",
        "expected_answer": "Option 1 (Subquery): SELECT MAX(salary) FROM Employee WHERE salary < (SELECT MAX(salary) FROM Employee); Option 2 (Window function with IFNULL / subquery): SELECT (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1) as SecondHighestSalary.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does wrapping the query in an outer SELECT (SELECT ...) ensure NULL is returned if OFFSET 1 yields zero rows?",
        "code_snippet": "SELECT MAX(salary) AS SecondHighestSalary\nFROM Employee\nWHERE salary < (SELECT MAX(salary) FROM Employee);"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "practical_query_duplicate_detection",
        "difficulty": "easy",
        "question_text": "Write a query to find all duplicate email addresses in a Person table with columns (id, email).",
        "expected_answer": "SELECT email FROM Person GROUP BY email HAVING COUNT(email) > 1;",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you delete all duplicate email rows while keeping only the one with the smallest id?",
        "code_snippet": "SELECT email\nFROM Person\nGROUP BY email\nHAVING COUNT(*) > 1;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "practical_query_top_n_per_group",
        "difficulty": "hard",
        "question_text": "Write a query using a window function to find the top 3 highest-earning employees in EACH department from an Employee table (id, name, salary, department_id).",
        "expected_answer": "Use a CTE with DENSE_RANK() or ROW_NUMBER() partitioned by department_id and ordered by salary descending, then filter where rank <= 3 in the outer query.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why cannot window function results be filtered directly in the WHERE clause of the same SELECT statement?",
        "code_snippet": "WITH RankedEmployees AS (\n  SELECT name, salary, department_id,\n    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rnk\n  FROM Employee\n)\nSELECT name, salary, department_id\nFROM RankedEmployees\nWHERE rnk <= 3;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "set_operations",
        "difficulty": "easy",
        "question_text": "Explain the difference between UNION and UNION ALL in SQL. Which one is faster and why?",
        "expected_answer": "UNION combines the result sets of two queries and performs an implicit DISTINCT operation (sorting and removing duplicate rows). UNION ALL combines the result sets without checking for duplicates, preserving all rows. UNION ALL is significantly faster because it avoids expensive memory/disk sorting and deduplication.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What are INTERSECT and EXCEPT / MINUS set operations in SQL?",
        "code_snippet": "SELECT customer_id FROM online_orders\nUNION ALL\nSELECT customer_id FROM store_orders;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "database_locking",
        "difficulty": "hard",
        "question_text": "Explain Shared Locks (S-Locks), Exclusive Locks (X-Locks), and Deadlocks in relational databases. How does a database detect and resolve a deadlock?",
        "expected_answer": "Shared Locks (read locks) allow concurrent reads; multiple transactions can hold shared locks on the same resource. Exclusive Locks (write locks) prevent all other transactions from reading or writing until released. A Deadlock occurs when Tx1 holds resource A and waits for B, while Tx2 holds B and waits for A. Databases detect deadlocks using a Wait-For Graph (cycle detection) and resolve it by terminating/rolling back the transaction with the lowest cost (the deadlock victim).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does ordering database updates consistently in code prevent deadlocks?",
        "code_snippet": "SELECT * FROM inventory WHERE item_id = 10 FOR UPDATE;"
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "sharding_and_replication",
        "difficulty": "hard",
        "question_text": "Explain the architectural difference between Read-Replica Database Replication and Horizontal Database Sharding. What trade-offs exist with cross-shard queries?",
        "expected_answer": "Read-Replica replication copies the entire database from a primary read/write node to secondary read-only nodes, scaling read throughput and offering failover. Sharding partitions table rows across independent database servers based on a shard key (e.g. tenant_id or user_id hash). Trade-offs: Sharding scales writes horizontally, but makes cross-shard JOINs, distributed transactions (two-phase commit), and global foreign keys complex and expensive.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is replication lag and how does it cause read-your-own-writes inconsistencies?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "schema_migrations",
        "difficulty": "medium",
        "question_text": "How do you safely perform zero-downtime schema migrations on a high-traffic production table (e.g. renaming a column or adding a NOT NULL column with a default)?",
        "expected_answer": "For renaming: 1) Add new column with NULLable default; 2) Dual-write in application layer to both old and new columns; 3) Backfill historical rows in small batches; 4) Switch application reads to new column; 5) Remove writes to old column and drop old column in a later release. Never run 'ALTER TABLE ADD COLUMN NOT NULL' on billions of rows without checking if your RDBMS locks the whole table.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What tools (Flyway, Liquibase, Django migrations) manage schema version history?",
        "code_snippet": ""
    },
    {
        "role": "Software Engineer",
        "technology": "sql",
        "category": "practical_query_consecutive_records",
        "difficulty": "hard",
        "question_text": "Write a query to find all numbers that appear at least three times consecutively in a table Logs (id, num), assuming ids are sequential.",
        "expected_answer": "Option 1 (Self-joins): SELECT DISTINCT l1.num as ConsecutiveNums FROM Logs l1 JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num JOIN Logs l3 ON l1.id = l3.id - 2 AND l1.num = l3.num; Option 2 (Window functions): Use LAG() and LEAD() to compare current row with previous and next row.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How would you handle non-consecutive id gaps using ROW_NUMBER() differences (Islands and Gaps problem)?",
        "code_snippet": "SELECT DISTINCT l1.num AS ConsecutiveNums\nFROM Logs l1\nJOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num\nJOIN Logs l3 ON l1.id = l3.id - 2 AND l1.num = l3.num;"
    }
]
