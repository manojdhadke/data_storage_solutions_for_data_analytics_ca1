-- 1. what is the overall churn rate of customers?

CREATE VIEW Overall_Churn_Rate AS
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND((SUM(CASE WHEN churn_status = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)), 2) AS churn_rate
FROM
    Churn_Dim;


-- Customer Churn Patterns and Trends

CREATE VIEW Churn_Patterns_Trends AS
SELECT
    d.[date],
    COUNT(*) AS churn_count
FROM
    CallActivity_Fact c
INNER JOIN
    Date_Dim d ON c.date_id = d.date_id
WHERE
    c.churn_id IS NOT NULL
GROUP BY
    d.[date];


-- Customer churn rate based on customer tenure and loyalty
CREATE VIEW Churn_Rate_Tenure AS
SELECT
    CASE
        WHEN a.account_length <= 90 THEN '0-3 months'
        WHEN a.account_length <= 180 THEN '3-6 months'
        WHEN a.account_length <= 365 THEN '6-12 months'
        ELSE 'Over 12 months'
    END AS customer_tenure,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN ch.churn_status = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND((SUM(CASE WHEN ch.churn_status = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*)), 2) AS churn_rate
FROM
    CallActivity_Fact c
JOIN
    Account_Dim a ON c.account_id = a.account_id
LEFT JOIN
    Churn_Dim ch ON c.churn_id = ch.churn_id
GROUP BY
    CASE
        WHEN a.account_length <= 90 THEN '0-3 months'
        WHEN a.account_length <= 180 THEN '3-6 months'
        WHEN a.account_length <= 365 THEN '6-12 months'
        ELSE 'Over 12 months'
    END;

-- Plan Utilization

CREATE VIEW Plan_Utilization AS
SELECT
    ip.international_plan,
    vp.voicemail_plan,
    AVG(cf.totaldayminutes) AS avg_day_minutes_churned,
    AVG(cf.totalnightminutes) AS avg_night_minutes_churned,
    AVG(cf.totalintlminutes) AS avg_intl_minutes_churned
FROM
    CallActivity_Fact cf
JOIN
    InternationalPlan_Dim ip ON cf.international_plan_id = ip.international_plan_id
JOIN
    VoicemailPlan_Dim vp ON cf.voicemail_plan_id = vp.voicemail_id
WHERE
    cf.churn_id IS NOT NULL
GROUP BY
    ip.international_plan,
    vp.voicemail_plan;
