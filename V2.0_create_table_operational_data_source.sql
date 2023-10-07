CREATE DATABASE Customers;

GO

CREATE TABLE Churn_Customers (
    account_id INT IDENTITY(1001, 1) NOT NULL PRIMARY KEY,
    churn VARCHAR(10),
    account_length INT,
    international_plan VARCHAR(10),
    voicemail_plan VARCHAR(10)
);

-- 
CREATE DATABASE Churn_CallActivity;

GO

CREATE TABLE CallDetails (
    call_id INT IDENTITY(1001, 1) NOT NULL PRIMARY KEY,
    account_id INT,
    number_vmail_messages INT,
    total_day_minutes DECIMAL(10, 2),
    total_day_calls INT,
    total_day_charge DECIMAL(10, 2),
    total_eve_minutes DECIMAL(10, 2),
    total_eve_calls INT,
    total_eve_charge DECIMAL(10, 2),
    total_night_minutes DECIMAL(10, 2),
    total_night_calls INT,
    total_night_charge DECIMAL(10, 2),
    number_customer_service_calls INT
);

CREATE TABLE InternationalCalls (
    international_call_id INT IDENTITY(2001, 1) NOT NULL PRIMARY KEY,
    account_id INT FOREIGN KEY REFERENCES CallDetails(account_id),
    total_intl_minutes DECIMAL(10, 2),
    total_intl_calls INT,
    total_intl_charge DECIMAL(10, 2)
);

CREATE TABLE Voicemail (
    voicemail_id INT IDENTITY(1001, 1) NOT NULL PRIMARY KEY,
    customer_id INT,
    number_vmail_messages INT
);
