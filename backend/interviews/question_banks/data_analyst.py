"""
Data Analyst Question Bank - 25 distinct technical questions.
Covers SQL analysis, statistics, data cleaning, A/B testing, cohort retention, KPI tracking, and visualization principles.
"""

DATA_ANALYST_QUESTIONS = [
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "statistics",
        "difficulty": "easy",
        "question_text": "What is the difference between Mean and Median, and when should a data analyst report the median instead of the mean for metrics like customer income or order value?",
        "expected_answer": "The mean is the arithmetic average and is sensitive to extreme outliers. The median is the middle value in a sorted distribution and is robust against skewness and outliers. When analyzing metrics with heavy right skew (such as customer salary, home values, or transaction amounts with whale spenders), median provides a more accurate representation of typical user behavior.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you calculate the interquartile range (IQR) to detect outliers?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "ab_testing",
        "difficulty": "medium",
        "question_text": "Explain the concept of statistical significance and p-value in an A/B test. If p = 0.03 at alpha = 0.05, what conclusion can you draw, and what does it NOT mean?",
        "expected_answer": "A p-value measures the probability of observing results at least as extreme as the experiment data, assuming the null hypothesis (no real difference) is true. At alpha = 0.05, p = 0.03 is statistically significant, so we reject the null hypothesis. It does NOT mean there is a 97% chance variant B is better, nor does it guarantee practical business significance.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the danger of 'peeking' at test results before reaching the planned sample size?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "sql_metrics",
        "difficulty": "medium",
        "question_text": "Write a SQL query to perform a Monthly User Retention / Cohort Analysis: calculate what percentage of users who signed up in month M returned to make a purchase in month M+1.",
        "expected_answer": "Extract the signup month as the cohort month. Join the activity/purchases table on user_id, calculate the difference in months between purchase date and signup date. Group by cohort month and month_offset, counting distinct active users divided by initial cohort size.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle users who made multiple purchases in the same month?",
        "code_snippet": "WITH CohortUsers AS (\n    SELECT user_id, DATE_TRUNC('month', signup_date) AS cohort_month\n    FROM users\n),\nUserActivity AS (\n    SELECT c.cohort_month,\n           DATE_PART('month', AGE(DATE_TRUNC('month', o.order_date), c.cohort_month)) AS month_number,\n           COUNT(DISTINCT o.user_id) AS active_users\n    FROM orders o\n    JOIN CohortUsers c ON o.user_id = c.user_id\n    GROUP BY 1, 2\n)\nSELECT cohort_month, month_number, active_users FROM UserActivity;"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "data_cleaning",
        "difficulty": "easy",
        "question_text": "How do you detect, evaluate, and handle missing (null) values in a dataset? When is row deletion appropriate versus mean/median imputation or forward filling?",
        "expected_answer": "Detect using isnull().sum() or WHERE col IS NULL. Evaluate whether data is Missing Completely at Random (MCAR), Missing at Random (MAR), or Missing Not at Random (MNAR). Delete rows if missing data is negligible (<2%) and MCAR. Impute with median/mode for numerical/categorical data when retaining row volume is important. Use forward/backward fill for continuous time-series sensor data.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why does mean imputation artificially reduce variance in the dataset?",
        "code_snippet": "# Pandas handling:\ndf['income'] = df['income'].fillna(df['income'].median())\ndf['temperature'] = df['temperature'].ffill()"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "business_metrics",
        "difficulty": "medium",
        "question_text": "Define Customer Acquisition Cost (CAC) and Lifetime Value (LTV). What does an LTV:CAC ratio of 3:1 indicate compared to 1:1 or 8:1?",
        "expected_answer": "CAC is total marketing and sales expenditure divided by the number of new customers acquired in that period. LTV is the total gross profit contribution expected from a customer over their relationship lifespan. An LTV:CAC ratio of 3:1 is considered healthy and sustainable. 1:1 means acquiring customers is unprofitable after operational expenses. 8:1 suggests the company is under-investing in marketing and missing growth opportunities.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does churn rate affect customer lifetime value calculation?",
        "code_snippet": "LTV = (Average Order Value * Purchase Frequency * Gross Margin) / Churn Rate"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "sql_metrics",
        "difficulty": "medium",
        "question_text": "Write a query to calculate the funnel conversion rates for an e-commerce checkout funnel: Page View -> Add to Cart -> Initiate Checkout -> Purchase.",
        "expected_answer": "Count distinct user sessions at each step using conditional aggregation or CASE WHEN statements. Then calculate the step-to-step dropoff percentage and total end-to-end conversion rate (Purchases / Page Views).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you ensure actions occurred in chronological order within the same user session?",
        "code_snippet": "SELECT \n    COUNT(DISTINCT session_id) AS total_visitors,\n    COUNT(DISTINCT CASE WHEN step = 'cart' THEN session_id END) AS cart_count,\n    COUNT(DISTINCT CASE WHEN step = 'checkout' THEN session_id END) AS checkout_count,\n    COUNT(DISTINCT CASE WHEN step = 'purchase' THEN session_id END) AS purchase_count,\n    ROUND(COUNT(DISTINCT CASE WHEN step = 'purchase' THEN session_id END)::numeric / COUNT(DISTINCT session_id) * 100, 2) AS overall_conversion_pct\nFROM funnel_events;"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "statistics",
        "difficulty": "medium",
        "question_text": "Explain Simpson's Paradox with a concrete example. How can an overall trend reverse or disappear when data is segmented by a confounding variable?",
        "expected_answer": "Simpson's Paradox occurs when a trend apparent in different subgroups disappears or reverses when the groups are aggregated. For example, Treatment A might have higher recovery rates than Treatment B in both mild cases and severe cases individually. However, if Treatment A was given mostly to severe patients while Treatment B was given mostly to mild patients, Treatment B appears better overall due to the confounding disease severity.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do analysts identify and control for confounding variables in observational studies?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "data_cleaning",
        "difficulty": "medium",
        "question_text": "How do you identify duplicate records in SQL and remove all duplicates while keeping only the most recently updated record?",
        "expected_answer": "Use a CTE with ROW_NUMBER() partitioned by the natural unique key columns (e.g. email or transaction_id) ordered by updated_at DESC. Records with row_num > 1 are duplicates. In a DELETE statement, delete records where row_num > 1.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between exact duplicates across all columns versus business key duplicates?",
        "code_snippet": "WITH RankedRecords AS (\n    SELECT ctid, ROW_NUMBER() OVER (\n        PARTITION BY email ORDER BY updated_at DESC\n    ) AS rn\n    FROM customer_leads\n)\nDELETE FROM customer_leads\nWHERE ctid IN (SELECT ctid FROM RankedRecords WHERE rn > 1);"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "visualization",
        "difficulty": "easy",
        "question_text": "Which chart type would you choose to visualize: 1. Relationship between marketing spend and conversions, 2. Distribution of delivery times, 3. Revenue trends over 3 years, 4. Market share among 4 competitors?",
        "expected_answer": "1. Relationship: Scatter plot (shows correlation and clusters). 2. Distribution: Histogram or Box plot (shows median, spread, skew, outliers). 3. Trends over time: Line chart (continuous time series). 4. Market share: Bar chart or Donut chart (bar chart is preferred for accurate visual comparison of lengths).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why do data visualization experts recommend avoiding 3D pie charts?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "statistics",
        "difficulty": "hard",
        "question_text": "What is the Central Limit Theorem (CLT), and why is it fundamental to conducting hypothesis testing on sample means even when population data is not normally distributed?",
        "expected_answer": "The CLT states that the distribution of sample means approaches a normal (Gaussian) distribution as sample size N increases (typically N >= 30), regardless of the underlying population distribution shape. This allows analysts to compute standard errors, construct confidence intervals, and apply parametric tests (Z-tests, T-tests) to non-normal real-world data like purchase values.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between standard deviation and standard error of the mean?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "pandas_analysis",
        "difficulty": "medium",
        "question_text": "In Python Pandas, explain the difference between df.groupby().agg() and df.pivot_table(). Write code to compute total sales and median order value by region and product category.",
        "expected_answer": "groupby().agg() groups rows by specified columns and aggregates target columns into a multi-index series or dataframe. pivot_table() reshapes the output into a 2D matrix layout with columns as secondary dimensions and handles fill_value and margins automatically. Both perform aggregations, but pivot_table is designed for tabular cross-tabulation.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you flatten multi-level column indexes after groupby().agg()?",
        "code_snippet": "summary = df.pivot_table(\n    index='region',\n    columns='category',\n    values='order_value',\n    aggfunc={'order_value': ['sum', 'median']},\n    fill_value=0\n)"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "ab_testing",
        "difficulty": "hard",
        "question_text": "What are Type I and Type II errors in hypothesis testing? How does Sample Size Calculation prevent false positives and underpowered experiments?",
        "expected_answer": "Type I error (False Positive, alpha): Rejecting the null hypothesis when it is actually true (declaring a winning variant when there is no real effect). Type II error (False Negative, beta): Failing to reject null hypothesis when a real effect exists. Statistical Power (1 - beta) is the probability of detecting a true effect. Pre-calculating sample size using Minimum Detectable Effect (MDE), variance, alpha (0.05), and power (0.80) prevents underpowered tests.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What happens to the required sample size if you want to detect a 1% lift instead of a 10% lift?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "data_modeling",
        "difficulty": "medium",
        "question_text": "What is the difference between Fact Tables and Dimension Tables in a Star Schema data warehouse? Give examples from a retail business.",
        "expected_answer": "Fact tables contain quantitative metrics, foreign keys, and measurement events of business processes (e.g. sales_transactions with order_id, date_key, customer_key, product_key, quantity, revenue, discount). Dimension tables provide context, descriptors, and filtering attributes (e.g. dim_customer with name, country, age group; dim_product with category, brand).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is the difference between a Star Schema and a Snowflake Schema?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "business_metrics",
        "difficulty": "medium",
        "question_text": "How do you calculate Monthly Recurring Revenue (MRR), Churn Rate, and Net Revenue Retention (NRR) for a SaaS subscription business?",
        "expected_answer": "MRR is the predictable normalized subscription revenue per month. Churn Rate is lost customers (or lost MRR) divided by total starting customers in that month. NRR measures revenue retained from existing customers over time, including expansions/upgrades minus downgrades and churn: ((Starting MRR + Expansion - Contraction - Churn) / Starting MRR) * 100. NRR > 100% means organic expansion exceeds churn.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why can customer churn rate be low while revenue churn rate is high?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "data_transformation",
        "difficulty": "medium",
        "question_text": "Explain the difference between Wide format data and Long (Tidy) format data. How do you unpivot wide quarterly columns (Q1, Q2, Q3, Q4) into long rows in SQL or Pandas?",
        "expected_answer": "In wide format, each metric or time period has its own column (e.g. Company, Q1, Q2, Q3). In long format, each row represents a single observation with an attribute and value column (Company, Quarter, Revenue). Long format is standard for tidy data and BI tools. In SQL, unpivot using CROSS JOIN LATERAL or UNPIVOT; in Pandas, use pd.melt().",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is long format preferred for feeding BI visualization tools like Tableau or PowerBI?",
        "code_snippet": "df_long = pd.melt(df_wide, id_vars=['company'], value_vars=['Q1', 'Q2', 'Q3', 'Q4'], var_name='quarter', value_name='revenue')"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "correlation_causation",
        "difficulty": "easy",
        "question_text": "What is the Pearson correlation coefficient (r)? If two variables have a correlation of r = 0.85, can you conclude that variable X causes variable Y? Explain why or why not.",
        "expected_answer": "Pearson's r measures the strength and direction of linear relationship between two variables from -1 to +1 (0.85 indicates strong positive linear correlation). However, correlation does NOT imply causation. The correlation could be caused by reverse causality, coincidental spurious correlation, or a third lurking confounding variable (e.g. ice cream sales and drowning rates both correlate with temperature).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is Spearman's rank correlation and when is it preferred over Pearson?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "sql_metrics",
        "difficulty": "hard",
        "question_text": "Write a query to calculate customer Lifetime Value (LTV) deciles (dividing customers into 10 equal buckets by spending) and summarize the revenue contribution of the top 10% versus bottom 10%.",
        "expected_answer": "Sum total revenue per customer. Use NTILE(10) OVER (ORDER BY total_spend DESC) to assign deciles 1 through 10. Then group by decile to calculate customer count, total revenue, average spend, and percentage of overall revenue.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How does this analysis validate the Pareto principle (80/20 rule)?",
        "code_snippet": "WITH CustomerSpend AS (\n    SELECT user_id, SUM(amount) AS total_spend\n    FROM orders GROUP BY user_id\n),\nDeciles AS (\n    SELECT user_id, total_spend,\n           NTILE(10) OVER (ORDER BY total_spend DESC) AS spend_decile\n    FROM CustomerSpend\n)\nSELECT spend_decile, COUNT(*) AS users, SUM(total_spend) AS revenue,\n       ROUND(SUM(total_spend) / SUM(SUM(total_spend)) OVER () * 100, 2) AS revenue_share_pct\nFROM Deciles GROUP BY spend_decile ORDER BY spend_decile;"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "anomaly_detection",
        "difficulty": "medium",
        "question_text": "How do you detect anomalies and outliers in time-series transaction volume using rolling Z-scores or IQR bounds in Python or SQL?",
        "expected_answer": "Compute the rolling mean and rolling standard deviation over a window (e.g. 30 days). The Z-score for a day's value is (value - rolling_mean) / rolling_std. If |Z-score| > 3, it is flagged as an outlier (beyond 99.7% of expected variation). Alternatively, use rolling 1.5 * IQR bounds from Q1 and Q3.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do seasonal spikes (like Black Friday) need to be adjusted before outlier scoring?",
        "code_snippet": "rolling_mean = df['sales'].rolling(window=30).mean()\nrolling_std = df['sales'].rolling(window=30).std()\ndf['z_score'] = (df['sales'] - rolling_mean) / rolling_std\ndf['is_anomaly'] = df['z_score'].abs() > 3"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "data_governance",
        "difficulty": "medium",
        "question_text": "What is data lineage and data cataloging? Why is establishing a 'Single Source of Truth' critical when different departments report conflicting revenue figures?",
        "expected_answer": "Data lineage tracks the lifecycle, origin, dependencies, and transformation steps of data from raw capture through pipelines to dashboard reporting. Conflicting revenue figures occur when sales, accounting, and product teams apply different business logic (e.g. gross bookings vs net GAAP revenue vs cash collections). A Single Source of Truth standardizes centralized KPI definitions in a semantic layer.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do tools like dbt (data build tool) document models and tests?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "sql_metrics",
        "difficulty": "medium",
        "question_text": "Write a query to calculate the Rolling 30-Day Active Users (DAU/MAU ratio) to evaluate user engagement stickiness.",
        "expected_answer": "For each day, count distinct users active on that day (DAU). Use a join or window subquery to count distinct users active in the preceding 30 days (MAU). Calculate DAU/MAU * 100. A high ratio (e.g. 50%+) indicates high habit-forming product stickiness (e.g. social or messaging apps).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "Why is DAU/MAU an unsuitable metric for infrequently used platforms like tax filing software?",
        "code_snippet": "SELECT \n    d.activity_date,\n    COUNT(DISTINCT d.user_id) AS dau,\n    (SELECT COUNT(DISTINCT m.user_id) \n     FROM logins m \n     WHERE m.activity_date BETWEEN d.activity_date - INTERVAL '29 days' AND d.activity_date) AS mau\nFROM logins d\nGROUP BY d.activity_date;"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "statistics",
        "difficulty": "medium",
        "question_text": "What is regression analysis? How do you interpret the R-squared value and the p-value of a regression coefficient in a linear regression model?",
        "expected_answer": "Linear regression models the relationship between dependent variable Y and independent predictor variables X. R-squared (coefficient of determination) indicates the proportion of variance in Y explained by predictors (e.g. R²=0.72 means 72% explained). The p-value of a coefficient tests the null hypothesis that the slope is zero; p < 0.05 indicates the predictor has a statistically significant linear effect on Y.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is multicollinearity and how does Variance Inflation Factor (VIF) detect it?",
        "code_snippet": "import statsmodels.api as sm\nX = sm.add_constant(df[['marketing_spend', 'ad_clicks']])\nmodel = sm.OLS(df['sales'], X).fit()\nprint(model.summary())"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "rfm_segmentation",
        "difficulty": "hard",
        "question_text": "Explain RFM (Recency, Frequency, Monetary) customer segmentation. How do you construct RFM scores in SQL to identify Champions, Loyal Customers, and At-Risk customers?",
        "expected_answer": "RFM scores customers on: Recency (days since last transaction), Frequency (total count of transactions), Monetary (total revenue spent). In SQL, compute each metric, then use NTILE(5) OVER(...) to assign scores 1-5 for R, F, and M. Combine them (e.g. R=5, F=5, M=5 = Champions; R=1, F=5, M=5 = At-Risk high-value customers who haven't returned recently).",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What targeted marketing action should be taken for the 'Can't Lose Them' segment?",
        "code_snippet": "SELECT user_id,\n       NTILE(5) OVER (ORDER BY MAX(order_date) ASC) AS r_score,\n       NTILE(5) OVER (ORDER BY COUNT(*) DESC) AS f_score,\n       NTILE(5) OVER (ORDER BY SUM(amount) DESC) AS m_score\nFROM orders GROUP BY user_id;"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "sql_metrics",
        "difficulty": "easy",
        "question_text": "How do you calculate year-over-year (YoY) revenue growth in SQL using CASE WHEN or window functions?",
        "expected_answer": "Aggregate sales by year. Use LAG(annual_revenue, 1) OVER (ORDER BY sale_year) to access previous year revenue. Calculate (current_revenue - prior_revenue) / prior_revenue * 100.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you handle incomplete calendar years when comparing YoY?",
        "code_snippet": "WITH AnnualSales AS (\n    SELECT EXTRACT(year FROM order_date) AS yr, SUM(amount) AS revenue\n    FROM orders GROUP BY 1\n)\nSELECT yr, revenue,\n       ROUND((revenue - LAG(revenue) OVER (ORDER BY yr)) / LAG(revenue) OVER (ORDER BY yr) * 100, 2) AS yoy_growth\nFROM AnnualSales;"
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "dashboarding",
        "difficulty": "easy",
        "question_text": "What are the core design principles for building an executive dashboard in Power BI or Tableau that busy stakeholders can understand in 5 seconds?",
        "expected_answer": "Core principles: 1. Visual hierarchy (top KPIs with bold numbers and sparklines/trends at top left). 2. Minimize cognitive load (limit to 5-7 key charts, eliminate chartjunk). 3. Consistent color palette (use neutral colors for baseline, single highlight color for alerts/targets). 4. Clear interactive filters (date ranges, regions) and explicit tooltips with contextual definitions.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "How do you conduct user acceptance testing (UAT) with business stakeholders for dashboard sign-off?",
        "code_snippet": None
    },
    {
        "role": "Data Analyst",
        "technology": "data_analysis",
        "category": "data_ethics",
        "difficulty": "easy",
        "question_text": "What data privacy obligations (such as GDPR or CCPA) must data analysts respect when analyzing customer transaction records or building user profiles?",
        "expected_answer": "Analysts must respect Personally Identifiable Information (PII) protections: anonymize or pseudonymize customer records (hash emails, remove SSN/addresses), aggregate data to prevent re-identification of individuals (k-anonymity), enforce role-based access control, respect user opt-out consent flags, and adhere to data retention and deletion schedules.",
        "rubric": {"accuracy": 35, "depth": 30, "problem_solving": 25, "clarity": 10},
        "follow_up_hint": "What is differential privacy and how does injecting controlled noise protect privacy in aggregate queries?",
        "code_snippet": None
    }
]
