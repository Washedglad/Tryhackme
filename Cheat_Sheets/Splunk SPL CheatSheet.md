# Splunk SPL (Search Processing Language) Cheat Sheet

A comprehensive reference guide for Splunk Query Language commands and syntax.

## Table of Contents
- [Basic Search Syntax](#basic-search-syntax)
- [Search Commands](#search-commands)
- [Field Extraction & Manipulation](#field-extraction--manipulation)
- [Statistical Commands](#statistical-commands)
- [Transforming Commands](#transforming-commands)
- [Time Modifiers](#time-modifiers)
- [Comparison & Logical Operators](#comparison--logical-operators)
- [Eval Functions](#eval-functions)
- [Common Use Cases](#common-use-cases)

---

## Basic Search Syntax

### Simple Search
```spl
index=main error
```

### Boolean Operators
```spl
index=main (error OR failed OR exception)
index=main error NOT warning
index=main error AND status=500
```

### Wildcards
```spl
index=main error*
index=main status=5*
index=main host=web*.example.com
```

### Field Search
```spl
index=main status=404
index=main user="john.doe"
index=main ip_address=192.168.1.*
```

---

## Search Commands

### `search`
Filters events from the search results.
```spl
index=main | search status=200
```

### `where`
Filters results using eval expressions.
```spl
index=main | where status>=400 AND status<500
index=main | where len(username)>10
```

### `fields`
Includes or excludes fields from results.
```spl
index=main | fields status, user, response_time
index=main | fields - _raw, _time
```

### `table`
Displays results in a table format.
```spl
index=main | table _time, host, status, user
```

### `rename`
Renames fields.
```spl
index=main | rename src_ip as "Source IP", dest_ip as "Destination IP"
```

### `dedup`
Removes duplicate events.
```spl
index=main | dedup user
index=main | dedup user, host keepempty=true
```

### `head` / `tail`
Returns first/last N results.
```spl
index=main | head 10
index=main | tail 20
```

### `sort`
Sorts results by specified fields.
```spl
index=main | sort -response_time
index=main | sort +user, -_time
```

---

## Field Extraction & Manipulation

### `rex`
Extract fields using regular expressions.
```spl
index=main | rex field=_raw "user=(?<username>\w+)"
index=main | rex mode=sed "s/old_value/new_value/g"
```

### `extract` / `kv`
Automatically extract key-value pairs.
```spl
index=main | kv
index=main | extract pairdelim=",", kvdelim="="
```

### `eval`
Create or modify fields using expressions.
```spl
index=main | eval duration=end_time-start_time
index=main | eval status_category=if(status<400,"success","error")
```

### `lookup`
Enrich data with lookup tables.
```spl
index=main | lookup users.csv username OUTPUT email, department
```

---

## Statistical Commands

### `stats`
Calculate statistics on fields.
```spl
index=main | stats count by status
index=main | stats avg(response_time) as avg_time by host
index=main | stats sum(bytes) as total_bytes, dc(user) as unique_users
```

### `chart`
Create charts with statistical data.
```spl
index=main | chart count by status, host
index=main | chart avg(response_time) over _time by host
```

### `timechart`
Statistical aggregation over time.
```spl
index=main | timechart span=1h count by status
index=main | timechart span=5m avg(response_time)
```

### `top` / `rare`
Find most/least common values.
```spl
index=main | top limit=10 user
index=main | rare host showperc=true
```

### `eventstats`
Add aggregate statistics as fields to each event.
```spl
index=main | eventstats avg(response_time) as avg_resp_time by host
```

### `streamstats`
Calculate streaming statistics.
```spl
index=main | streamstats count as event_number
index=main | streamstats window=10 avg(response_time) as moving_avg
```

---

## Transforming Commands

### `transaction`
Group events into transactions.
```spl
index=main | transaction session_id maxspan=30m
index=main | transaction startswith="login" endswith="logout"
```

### `spath`
Extract fields from JSON or XML.
```spl
index=main | spath input=json_field output=extracted_value path=data.user.name
```

### `mvexpand`
Expand multi-value fields into separate events.
```spl
index=main | mvexpand user_list
```

### `makemv`
Convert a field into multi-value.
```spl
index=main | makemv delim="," tags
```

### `append`
Append results from a subsearch.
```spl
index=main | append [search index=backup]
```

### `join`
Join results from two searches.
```spl
index=main | join user [search index=users | fields user, email]
```

### `bin` / `bucket`
Group numeric or time values into discrete bins.
```spl
index=main | bin response_time span=100
index=main | bin _time span=1h
```

---

## Time Modifiers

### Relative Time
```spl
earliest=-24h latest=now
earliest=-7d@d latest=@d
earliest=-1h@h latest=now
```

### Absolute Time
```spl
earliest="01/01/2024:00:00:00" latest="01/31/2024:23:59:59"
```

### Time Formatting
```spl
index=main | eval readable_time=strftime(_time, "%Y-%m-%d %H:%M:%S")
index=main | eval hour=strftime(_time, "%H")
```

### Common Time Ranges
- `-15m` = Last 15 minutes
- `-1h` = Last hour
- `-24h` = Last 24 hours
- `-7d` = Last 7 days
- `-30d@d` = Last 30 days, snapped to day boundary
- `@w0` = Beginning of week (Sunday)
- `@mon` = Beginning of month

---

## Comparison & Logical Operators

### Comparison
```spl
= (equals)
!= (not equals)
< (less than)
> (greater than)
<= (less than or equal)
>= (greater than or equal)
```

### Logical
```spl
AND / OR / NOT
```

### Examples
```spl
index=main status>=400 AND status<500
index=main (status=200 OR status=201) NOT user=admin
```

---

## Eval Functions

### Mathematical
```spl
| eval result=x+y
| eval result=x*y/z
| eval result=round(value, 2)
| eval result=abs(value)
| eval result=sqrt(value)
| eval result=pow(base, exponent)
```

### String Functions
```spl
| eval result=upper(field)
| eval result=lower(field)
| eval result=substr(field, 1, 5)
| eval result=len(field)
| eval result=trim(field)
| eval result=replace(field, "old", "new")
| eval result=split(field, ",")
| eval result=mvjoin(multivalue_field, ",")
```

### Conditional
```spl
| eval result=if(condition, true_value, false_value)
| eval result=case(condition1, value1, condition2, value2, 1=1, default_value)
| eval result=coalesce(field1, field2, "default")
```

### Date/Time
```spl
| eval result=now()
| eval result=strftime(_time, "%Y-%m-%d")
| eval result=strptime(date_string, "%m/%d/%Y")
| eval result=relative_time(now(), "-1d")
```

### Validation
```spl
| eval result=isnotnull(field)
| eval result=isnull(field)
| eval result=isnum(field)
| eval result=typeof(field)
```

### Cryptographic
```spl
| eval result=md5(field)
| eval result=sha1(field)
| eval result=sha256(field)
```

---

## Common Use Cases

### Error Monitoring
```spl
index=main error OR exception OR failed
| stats count by error_type, host
| where count > 10
```

### Response Time Analysis
```spl
index=web
| stats avg(response_time) as avg_time, max(response_time) as max_time, perc95(response_time) as p95 by endpoint
| sort -avg_time
```

### Failed Login Attempts
```spl
index=security action=login status=failed
| stats count by user, src_ip
| where count > 5
| sort -count
```

### Traffic Analysis by Hour
```spl
index=web
| eval hour=strftime(_time, "%H")
| chart count by hour, status
```

### Top Talkers by Bandwidth
```spl
index=network
| stats sum(bytes) as total_bytes by src_ip
| eval total_mb=round(total_bytes/1024/1024, 2)
| sort -total_mb
| head 10
```

### User Session Duration
```spl
index=main
| transaction user maxspan=30m
| eval duration=round(duration, 2)
| stats avg(duration) as avg_session, max(duration) as longest_session by user
```

### Detect Anomalies
```spl
index=main
| timechart span=1h count as event_count
| eventstats avg(event_count) as avg_count, stdev(event_count) as stdev_count
| eval anomaly=if(event_count > avg_count + (2*stdev_count), "YES", "NO")
| where anomaly="YES"
```

### Data Volume by Source
```spl
index=*
| eval size_mb=len(_raw)/1024/1024
| stats sum(size_mb) as total_mb by index, sourcetype
| sort -total_mb
```

---

## Tips & Best Practices

1. **Use index and time range**: Always specify `index=` and use appropriate time ranges to improve performance
2. **Filter early**: Place filtering commands at the beginning of your search
3. **Limit fields**: Use `fields` command to reduce data processing
4. **Avoid wildcards at the start**: `*error` is slower than `error*`
5. **Use stats over transaction**: When possible, use `stats` instead of `transaction` for better performance
6. **Test with sample data**: Use `head` to test queries on smaller datasets first
7. **Save common searches**: Create saved searches or reports for frequently used queries

---

## Additional Resources

- [Splunk Documentation](https://docs.splunk.com)
- [Splunk Search Reference](https://docs.splunk.com/Documentation/Splunk/latest/SearchReference)
- [Splunk Quick Reference Guide](https://www.splunk.com/pdfs/solution-guides/splunk-quick-reference-guide.pdf)

---

**Version**: 1.0  
**Last Updated**: 2025

Feel free to contribute or suggest improvements!
