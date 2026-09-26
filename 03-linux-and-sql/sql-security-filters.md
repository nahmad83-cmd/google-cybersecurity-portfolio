# SQL Security Filters

## Project Description

I used SQL filters to investigate login activity and identify employee computers requiring security updates.

## Security Queries Performed

### After-Hours Failed Logins
Filtered login records for attempts after 18:00 where authentication was unsuccessful. This used `WHERE` with conditions combined using `AND`.

### Activity on Specific Dates
Investigated login activity on two dates associated with a suspicious event using `OR` to retrieve records matching either date.

### Login Attempts Outside Mexico
Used `NOT` with `LIKE 'Mex%'` to exclude country values beginning with `Mex`, allowing investigation of activity originating elsewhere.

### Marketing Employees in the East Building
Combined department and office-location criteria with `AND`, using `LIKE 'East%'` to match East-building office values.

### Finance or Sales Employees
Used `OR` to identify employees belonging to either Finance or Sales. The results identified **71 workstations** requiring the specified security update.

### Employees Outside Information Technology
Used `NOT` to exclude employees in the Information Technology department because they had already received a different update.

## Key Takeaway

SQL filtering can support security investigations by narrowing large datasets to the records that matter. Logical operators and pattern matching make it possible to investigate suspicious access and target remediation efficiently.

## Skills Demonstrated

SQL, `SELECT`, `WHERE`, `AND`, `OR`, `NOT`, `LIKE`, wildcards, login investigation, and security-update targeting.
