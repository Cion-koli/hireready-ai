"""
SQL Developer Question Bank - 25 distinct technical questions.
Covers complex query construction, window functions, indexing strategies, execution plans, transactions, normalization, and performance tuning.
"""

SQL_DEVELOPER_QUESTIONS = [
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "window_functions",
        "difficulty": "medium",
        "question_text": "Explain the difference between ROW_NUMBER(), RANK(), and DENSE_RANK(). Write a query to find the top 3 highest-earning employees per department, handling ties without skipping rank numbers.",
        "expected_answer": "ROW_NUMBER() assigns sequential distinct integers regardless of ties. RANK() assigns the same rank to ties and skips subsequent numbers (e.g. 1, 2, 2, 4). DENSE_RANK() assigns the same rank to ties without skipping subsequent numbers (e.g. 1, 2, 2, 3). For top 3 without skipping, use DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) in a CTE and filter WHERE rank_val <= 3.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the performance implication of partitioning large tables by low-cardinality columns?",
        "code_snippet": "WITH RankedSalaries AS (\n    SELECT emp_id, dept_id, salary,\n           DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rnk\n    FROM employees\n)\nSELECT * FROM RankedSalaries WHERE rnk <= 3;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "window_functions",
        "difficulty": "medium",
        "question_text": "How do LAG() and LEAD() window functions work? Write a query to compute the month-over-month percentage revenue growth for each store.",
        "expected_answer": "LAG() accesses data from a previous row in the partition at a given offset, while LEAD() accesses a subsequent row without requiring self-joins. To calculate MoM growth: calculate (current_month_revenue - LAG(current_month_revenue, 1) OVER (PARTITION BY store_id ORDER BY month)) / LAG(...) * 100.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle division by zero or NULL when calculating percentage growth?",
        "code_snippet": "SELECT store_id, sale_month, revenue,\n    ROUND(((revenue - LAG(revenue, 1) OVER (PARTITION BY store_id ORDER BY sale_month)) \n           / NULLIF(LAG(revenue, 1) OVER (PARTITION BY store_id ORDER BY sale_month), 0)) * 100, 2) AS mom_growth_pct\nFROM monthly_sales;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "cte_recursive",
        "difficulty": "hard",
        "question_text": "What is a Recursive Common Table Expression (CTE)? Write a recursive CTE to traverse an organizational hierarchy table (emp_id, manager_id, name) and find all subordinates under a specific manager along with their depth level.",
        "expected_answer": "A recursive CTE consists of an anchor member query (the base case) unioned with a recursive member query that references the CTE itself until an empty result set is produced. It is used to query hierarchical and tree structures like org charts, BOMs, or graph networks.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you prevent infinite loops if cyclical references exist in the data?",
        "code_snippet": "WITH RECURSIVE OrgHierarchy AS (\n    SELECT emp_id, name, manager_id, 1 AS level\n    FROM employees WHERE emp_id = :manager_id\n    UNION ALL\n    SELECT e.emp_id, e.name, e.manager_id, o.level + 1\n    FROM employees e\n    INNER JOIN OrgHierarchy o ON e.manager_id = o.emp_id\n)\nSELECT * FROM OrgHierarchy;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "indexing",
        "difficulty": "medium",
        "question_text": "What is a Covering Index (Index with INCLUDED columns), and how does it prevent expensive bookmark lookups (key / RID lookups)?",
        "expected_answer": "A Covering Index contains all the columns referenced in a query (SELECT, WHERE, JOIN, ORDER BY) either as index keys or non-key INCLUDE columns. When a query is covered, the database engine satisfies the query entirely from the B-tree leaf nodes without performing random I/O bookmark lookups on the base clustered table.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why not add all table columns to the index key instead of INCLUDE columns?",
        "code_snippet": "CREATE NONCLUSTERED INDEX idx_orders_customer_date\nON orders (customer_id, order_date)\nINCLUDE (total_amount, status);"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "query_tuning",
        "difficulty": "hard",
        "question_text": "Explain what an Index Seek versus Index Scan means in an execution plan. Under what conditions will an index on a column NOT be used even if an index exists?",
        "expected_answer": "Index Seek navigates the B-tree directly using the key value to find specific matching rows (O(log N)). Index Scan reads all or a significant range of leaf nodes in the index (O(N)). An index will not be used if: non-sargable functions wrap the column (e.g. WHERE YEAR(date) = 2024), leading wildcards in LIKE ('%term'), type conversions (implicit casting), or the optimizer determines low selectivity where a full table scan is cheaper.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does updating statistics affect whether the optimizer chooses a seek or a scan?",
        "code_snippet": "-- Non-sargable (triggers scan):\nWHERE SUBSTRING(customer_code, 1, 3) = 'USA'\n-- Sargable (enables seek):\nWHERE customer_code LIKE 'USA%'"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "joins",
        "difficulty": "medium",
        "question_text": "Compare the three internal physical join operators used by RDBMS query engines: Nested Loops Join, Hash Join, and Merge Join. When is each optimal?",
        "expected_answer": "Nested Loops Join iterates through an outer table and performs indexed lookups on the inner table; best when one table is small and the join column is indexed. Hash Join hashes the smaller table in memory and streams the larger table; best for large, unsorted, unindexed datasets. Merge Join steps through both inputs simultaneously; requires both inputs to be sorted on the join key, very fast for large sorted inputs.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What occurs when the memory grant for a Hash Join spills to tempdb / disk?",
        "code_snippet": None
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "transactions",
        "difficulty": "hard",
        "question_text": "Explain the four ANSI SQL Transaction Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, and Serializable. What read phenomena (dirty read, non-repeatable read, phantom read) does each prevent?",
        "expected_answer": "Read Uncommitted allows dirty reads (reading uncommitted changes). Read Committed prevents dirty reads using short shared locks or snapshots, but permits non-repeatable reads. Repeatable Read prevents dirty and non-repeatable reads by holding locks until transaction ends, but permits phantom reads (new rows inserted). Serializable prevents all three phenomena, ensuring transactions execute as if strictly serial.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does Multi-Version Concurrency Control (MVCC) in PostgreSQL/MySQL avoid read locks in Read Committed and Repeatable Read?",
        "code_snippet": "SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;\nBEGIN TRANSACTION;\n-- queries\nCOMMIT;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "concurrency",
        "difficulty": "hard",
        "question_text": "What is a Deadlock in relational databases? How does the database engine detect deadlocks, and what query design strategies eliminate or minimize them?",
        "expected_answer": "A deadlock occurs when two or more transactions hold locks that the other transactions need to proceed, creating a circular dependency where neither can continue. The engine uses a deadlock detection thread (wait-for graph) and kills one transaction as the deadlock victim. Prevention: access tables and rows in the exact same chronological order, keep transactions short, use fine-grained indexing, and use NOLOCK / read-committed snapshot.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do lock escalation thresholds (e.g. 5000 row locks -> table lock) trigger unexpected deadlocks?",
        "code_snippet": None
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "normalization",
        "difficulty": "medium",
        "question_text": "Explain 1st, 2nd, 3rd Normal Forms (1NF, 2NF, 3NF) and Boyce-Codd Normal Form (BCNF). When is intentional denormalization justified in production data systems?",
        "expected_answer": "1NF requires atomic values and unique records (primary key). 2NF requires 1NF and no partial dependencies (every non-key column depends on the whole composite primary key). 3NF requires 2NF and no transitive dependencies (non-key columns depend only on primary key). BCNF requires that for every functional dependency X -> Y, X must be a superkey. Denormalization is justified in OLAP / read-heavy reporting systems to eliminate costly multi-table joins.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What data anomaly risks are introduced when denormalizing tables?",
        "code_snippet": None
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "views",
        "difficulty": "medium",
        "question_text": "What is the difference between a Standard View and a Materialized View (Indexed View)? How and when are materialized views refreshed?",
        "expected_answer": "A standard view is a saved virtual query that executes dynamically every time it is referenced, storing no physical data. A materialized view computes the query and physically stores the result set on disk with its own indexes. They are refreshed either synchronously on underlying table commit or asynchronously on schedule / on-demand via REFRESH MATERIALIZED VIEW.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the storage and write penalty of maintaining materialized views on high-throughput OLTP tables?",
        "code_snippet": "CREATE MATERIALIZED VIEW mv_daily_sales AS\nSELECT sale_date, SUM(amount) AS total\nFROM sales GROUP BY sale_date;\n-- refresh\nREFRESH MATERIALIZED VIEW CONCURRENTLY mv_daily_sales;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "stored_procedures",
        "difficulty": "medium",
        "question_text": "Contrast Stored Procedures with User-Defined Functions (UDFs). Why can scalar UDFs inside WHERE or SELECT clauses severely degrade query performance?",
        "expected_answer": "Stored procedures can execute DDL, DML, transaction control (COMMIT/ROLLBACK), return multiple result sets, and output parameters. UDFs must return a single scalar or table, cannot modify database state, and cannot manage transactions. Scalar UDFs in SELECT/WHERE are executed row-by-row (RBAR - row by agonizing row), preventing vectorization and parallel execution plans.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do Inline Table-Valued Functions (iTVFs) avoid the row-by-row penalty?",
        "code_snippet": None
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "query_writing",
        "difficulty": "hard",
        "question_text": "Write an efficient SQL query to identify 'gaps and islands' in a sequence of user login dates, grouping consecutive days of logins into single streaks.",
        "expected_answer": "Use DATEADD/subtract ROW_NUMBER() from login_date to generate a constant date group key for consecutive dates. When partitioned by user_id and ordered by date, consecutive dates increment both date and row_number at the same rate, keeping the difference constant (the island). Group by user_id and this difference to find streak MIN(date), MAX(date), and COUNT(*).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How would you find missing date ranges (gaps) between streaks?",
        "code_snippet": "WITH RankedLogins AS (\n    SELECT user_id, login_date,\n           login_date - INTERVAL '1 day' * ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) AS streak_group\n    FROM user_logins\n)\nSELECT user_id, MIN(login_date) AS streak_start, MAX(login_date) AS streak_end, COUNT(*) AS streak_length\nFROM RankedLogins GROUP BY user_id, streak_group;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "partitioning",
        "difficulty": "hard",
        "question_text": "Explain Table Partitioning (Range, List, Hash). How does Partition Elimination (Partition Pruning) optimize query execution on billion-row tables?",
        "expected_answer": "Table partitioning splits large physical tables into smaller managed chunks based on a partition key (e.g. order_date range per month). Partition Elimination occurs when the query optimizer examines WHERE constraints on the partition key and skips reading entire partitions that cannot match the query filter, converting billion-row scans into bounded partition scans.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does partition pruning work when joining two partitioned tables (partition-wise joins)?",
        "code_snippet": "CREATE TABLE orders (\n    order_id INT, order_date DATE, amount NUMERIC\n) PARTITION BY RANGE (order_date);\n\nCREATE TABLE orders_2024_01 PARTITION OF orders\n    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "aggregation",
        "difficulty": "medium",
        "question_text": "What are GROUPING SETS, ROLLUP, and CUBE in SQL aggregation? Write a query using ROLLUP to produce department subtotals and grand totals in a single pass.",
        "expected_answer": "GROUPING SETS allows specifying multiple grouping dimensions in a single query. ROLLUP produces hierarchical aggregations from right to left plus a grand total (e.g. (A, B), (A), ()). CUBE produces all possible combinations of grouping sets (powerset). Using ROLLUP avoids running separate GROUP BY queries unioned with UNION ALL.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does the GROUPING() or GROUPING_ID() function distinguish NULL values in data from generated subtotal NULLs?",
        "code_snippet": "SELECT dept_id, job_title, SUM(salary) AS total_salary,\n       GROUPING(job_title) AS is_dept_subtotal,\n       GROUPING(dept_id) AS is_grand_total\nFROM employees\nGROUP BY ROLLUP (dept_id, job_title);"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "null_semantics",
        "difficulty": "easy",
        "question_text": "Explain Three-Valued Logic in SQL (TRUE, FALSE, UNKNOWN) and the danger of using NOT IN with a subquery that contains a NULL value.",
        "expected_answer": "SQL uses three-valued logic where comparisons with NULL yield UNKNOWN. If a subquery returns ANY row with a NULL value, WHERE id NOT IN (SELECT other_id ...) evaluates to UNKNOWN for all rows because (id <> NULL) is UNKNOWN and ANDed with other comparisons. Consequently, the entire NOT IN query returns zero rows. The safe alternative is NOT EXISTS.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does NOT EXISTS not suffer from this NULL pitfall?",
        "code_snippet": "-- Dangerous if subquery has NULLs:\nSELECT * FROM customers WHERE id NOT IN (SELECT customer_id FROM orders);\n-- Safe alternative:\nSELECT * FROM customers c WHERE NOT EXISTS (\n    SELECT 1 FROM orders o WHERE o.customer_id = c.id\n);"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "triggers",
        "difficulty": "medium",
        "question_text": "What is the difference between BEFORE and AFTER triggers, and ROW-level versus STATEMENT-level triggers? What are the risks of business logic in triggers?",
        "expected_answer": "BEFORE triggers run prior to constraint checks and data writes (ideal for input validation or defaulting column values). AFTER triggers run after modifications and constraints succeed (ideal for auditing or syncing other tables). ROW-level fires once per affected row (accessing OLD and NEW); STATEMENT-level fires once per SQL command. Risks: hidden cascading logic, hard to debug, overhead on bulk DML.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is an INSTEAD OF trigger and where is it commonly applied?",
        "code_snippet": None
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "performance",
        "difficulty": "hard",
        "question_text": "What is Parameter Sniffing in stored procedures? How does it cause intermittent catastrophic query performance degradation, and how do you resolve it?",
        "expected_answer": "Parameter sniffing occurs when the query optimizer compiles an execution plan based on the parameter values passed during the first execution. If those values represent an outlier (e.g. status='FAILED' matching 2 rows vs status='SUCCESS' matching 20 million rows), the cached plan (e.g. Index Seek with Nested Loops) becomes catastrophic for normal values. Fixes: OPTIMIZE FOR (@val = value), RECOMPILE hint, or local variable assignment.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the trade-off of using WITH RECOMPILE on high-frequency stored procedures?",
        "code_snippet": "CREATE PROCEDURE GetOrdersByStatus @Status VARCHAR(20)\nAS\nBEGIN\n    SELECT * FROM orders WHERE status = @Status\n    OPTION (RECOMPILE);\nEND"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "json_handling",
        "difficulty": "medium",
        "question_text": "How do modern SQL engines handle semi-structured JSON data (e.g. JSONB in PostgreSQL or JSON_VALUE in SQL Server / MySQL)? What are the pros and cons of JSON columns?",
        "expected_answer": "Engines provide native JSON types and operators (e.g. ->, ->>, JSON_EXTRACT) and support indexing paths using GIN or functional B-tree indexes. Pros: schema flexibility for polymorphic metadata, rapid prototyping. Cons: lacks strict foreign keys, larger storage footprint, slower updates (full document rewriting), and complex analytics compared to relational columns.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you create an expression index on a specific JSON attribute in PostgreSQL?",
        "code_snippet": "SELECT id, user_data->>'email' AS email\nFROM users\nWHERE user_data->'preferences'->>'theme' = 'dark';\n-- GIN index:\nCREATE INDEX idx_users_jsonb ON users USING GIN (user_data);"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "query_writing",
        "difficulty": "hard",
        "question_text": "Write a query to calculate the cumulative sum (running total) and 7-day moving average of daily sales using SQL window frames.",
        "expected_answer": "Use SUM(amount) OVER (ORDER BY sale_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) for cumulative sum. For 7-day moving average, use AVG(amount) OVER (ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between ROWS BETWEEN and RANGE BETWEEN in window frames?",
        "code_snippet": "SELECT sale_date, daily_revenue,\n    SUM(daily_revenue) OVER (\n        ORDER BY sale_date \n        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW\n    ) AS cumulative_revenue,\n    AVG(daily_revenue) OVER (\n        ORDER BY sale_date \n        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW\n    ) AS moving_avg_7d\nFROM daily_metrics;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "data_manipulation",
        "difficulty": "medium",
        "question_text": "Explain the MERGE statement (UPSERT). Write a MERGE query that synchronizes a staging table with a production target table by inserting new records, updating existing records, and marking missing records as inactive.",
        "expected_answer": "MERGE joins target and source tables on a key and executes WHEN MATCHED THEN UPDATE, WHEN NOT MATCHED BY TARGET THEN INSERT, and optionally WHEN NOT MATCHED BY SOURCE THEN UPDATE (or DELETE) in a single atomic SQL statement.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What concurrency and locking bugs can occur with MERGE without HOLDLOCK / SERIALIZABLE hints?",
        "code_snippet": "MERGE INTO target_products AS target\nUSING staging_products AS source\nON target.sku = source.sku\nWHEN MATCHED THEN \n    UPDATE SET target.price = source.price, target.updated_at = NOW()\nWHEN NOT MATCHED THEN\n    INSERT (sku, price, is_active) VALUES (source.sku, source.price, TRUE);"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "indexing",
        "difficulty": "hard",
        "question_text": "What is a Filtered / Partial Index, and how does it save disk space and improve query throughput on skewed columns (e.g. status='FAILED')?",
        "expected_answer": "A Filtered (or Partial) Index includes only rows satisfying a WHERE predicate defined in the index creation. For columns where 99% of rows are 'COMPLETED' and 1% are 'FAILED', indexing only WHERE status = 'FAILED' creates a tiny index that speeds up failed-order lookups without maintaining entries for millions of completed orders.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why must query WHERE clauses exactly match the filtered index predicate?",
        "code_snippet": "CREATE INDEX idx_orders_unprocessed \nON orders (order_date)\nWHERE status = 'PENDING';"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "cardinality_statistics",
        "difficulty": "medium",
        "question_text": "What role do Database Statistics and Histograms play in cardinality estimation, and why do stale statistics cause poor execution plan selection?",
        "expected_answer": "Statistics describe the distribution of data values in columns and indexes using density and histograms. The query optimizer consults these histograms to estimate cardinality (number of rows matched). If stats are stale after massive inserts or deletions, the optimizer misestimates row counts, selecting inappropriate join types or index scans.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you manually recompute statistics in your database (e.g. ANALYZE or UPDATE STATISTICS)?",
        "code_snippet": "-- PostgreSQL:\nANALYZE verbose customers;\n-- SQL Server:\nUPDATE STATISTICS customers WITH FULLSCAN;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "temp_storage",
        "difficulty": "medium",
        "question_text": "Compare Local Temporary Tables, Global Temporary Tables, and Table Variables / CTEs. When would you use each for intermediate calculations?",
        "expected_answer": "Local temp tables (#temp) exist within session scope, support indexes, and participate in statistics/recompiles. Global temp tables (##temp) are visible across all sessions until all referencing sessions disconnect. Table variables (@table) reside in memory/tempdb, lack distribution statistics, and are suited for tiny lookup sets. CTEs are query-scoped syntactic sugar.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why do table variables always report an estimated cardinality of 1 in older SQL Server versions?",
        "code_snippet": "CREATE TABLE #TempOrders (order_id INT PRIMARY KEY, total NUMERIC);\nINSERT INTO #TempOrders\nSELECT order_id, total FROM orders WHERE order_date >= '2024-01-01';"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "security",
        "difficulty": "medium",
        "question_text": "How does SQL injection occur via dynamic SQL, and what is the exact mechanism by which parameterized queries (Prepared Statements) prevent injection attacks?",
        "expected_answer": "SQL injection occurs when untrusted user input is concatenated into an SQL string, allowing input to alter the syntactic structure of the query command. Parameterized queries pre-compile the SQL statement structure first and transmit user values separately as typed data parameters, ensuring input is never parsed or executed as executable SQL code.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Can SQL injection occur inside dynamic SQL executed within stored procedures using EXEC() or EXECUTE IMMEDIATE?",
        "code_snippet": "-- Vulnerable:\nEXEC('SELECT * FROM users WHERE username = ''' + @user + '''');\n-- Safe:\nEXEC sp_executesql N'SELECT * FROM users WHERE username = @u', N'@u VARCHAR(50)', @u = @user;"
    },
    {
        "role": "SQL Developer",
        "technology": "sql",
        "category": "sharding_replication",
        "difficulty": "hard",
        "question_text": "Explain Read Replicas versus Database Sharding. How does replication lag affect application reads, and how do you handle read-after-write consistency?",
        "expected_answer": "Read replicas copy data asynchronously from a primary write node, scaling read throughput across multiple nodes. Sharding horizontally partitions table rows across distinct database clusters by a shard key to scale both writes and storage. Replication lag means replicas momentarily serve stale data. Solutions for read-after-write: route reads to the primary immediately after user mutations or use synchronous replication.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the two-phase commit (2PC) protocol used in distributed transactions across shards?",
        "code_snippet": None
    }
]
