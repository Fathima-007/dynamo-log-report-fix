There is an Apache-style access log at /app/access.log. Parse it and write a JSON summary report to /app/report.json.

The report.json file must be a valid JSON object with exactly these fields:

1. total_requests (integer) — the total number of log entries in the file.
2. unique_ips (integer) — the number of distinct client IP addresses that made requests.
3. top_path (string) — the URL path that was requested most often (e.g. "/index.html").

Save the completed report as valid JSON to /app/report.json.