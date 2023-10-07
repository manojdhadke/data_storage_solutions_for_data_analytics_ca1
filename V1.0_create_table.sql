CREATE TABLE Account (
    account_id INT IDENTITY(1001, 1) NOT NULL PRIMARY KEY,
    account_length INT
);

CREATE TABLE InternationalPlan (
    international_plan_id INT IDENTITY(1000, 1) NOT NULL PRIMARY KEY,
    international_plan VARCHAR(3)
);

CREATE TABLE VoicemailPlan (
    voicemail_plan_id INT IDENTITY(1000, 1) NOT NULL PRIMARY KEY,
    voicemail_plan VARCHAR(3)
);

CREATE TABLE Voicemail (
    voicemail_id INT IDENTITY(1001, 1) NOT NULL PRIMARY KEY,
    account_id INT,
    voicemail_plan VARCHAR(10),
    number_vmail_messages INT
);

CREATE TABLE VoicemailPlan_Dim (
    voicemail_id INT IDENTITY(1001, 1) NOT NULL PRIMARY KEY,
    account_id INT,
    voicemail_plan VARCHAR(10),
    number_vmail_messages INT
);

CREATE TABLE Churn (
    churn_id INT IDENTITY(1000, 1) NOT NULL PRIMARY KEY,
    churn_status VARCHAR(3)
);

CREATE TABLE Date (
    date_id INT IDENTITY(1000, 1) NOT NULL PRIMARY KEY,
    date DATE,
    year INT,
    month INT,
    day INT,
    day_of_week VARCHAR(10)
);

CREATE TABLE Time (
    time_id INT IDENTITY(1000, 1) NOT NULL PRIMARY KEY,
    hour INT,
    minute INT,
    second INT
);

CREATE TABLE CallActivity (
    call_activity_id INT IDENTITY(1001, 1) NOT NULL PRIMARY KEY,
    account_id INT,
    date_id INT,
    time_id INT,
    international_plan_id INT,
    voicemail_plan_id INT,
    numbervmailmessages INT,
    totaldayminutes DECIMAL(10,2),
    totaldaycalls INT,
    totaldaycharge DECIMAL(10,2),
    totaleveminutes DECIMAL(10,2),
    totalevecalls INT,
    totalevecharge DECIMAL(10,2),
    totalnightminutes DECIMAL(10,2),
    totalnightcalls INT,
    totalnightcharge DECIMAL(10,2),
    totalintlminutes DECIMAL(10,2),
    totalintlcalls INT,
    totalintlcharge DECIMAL(10,2),
    numbercustomerservicecalls INT,
    churn_id INT
);
