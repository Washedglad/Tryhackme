## Splunk: Data Manipulation

# How many Python scripts are present in the ~/Downloads/scripts directory?
      3
<img width="472" height="107" alt="image" src="https://github.com/user-attachments/assets/cf6b3fce-58b1-4f83-a6e6-41ccde33f51b" />

Step 1: Understand the Data Format

First, you need to understand the data format you want to parse. Splunk supports various data formats, such as CSV, JSON, XML, syslog, and more. Determine the format of your data source and the relevant fields you want to extract.

Step 2: Identify the Sourcetype

In Splunk, the sourcetype represents the format of the data being indexed. It helps Splunk apply the appropriate parsing rules. If your data source does not have a pre-defined sourcetype, you can create a custom one in Splunk.

Step 3: Configure props.conf

The props.conf file defines data parsing settings for specific sourcetypes or data sources. It resides in the $SPLUNK_HOME/etc/system/local directory. Here’s an example of how you can configure props.conf:

[source::/path/to/your/data] 

sourcetype = your_sourcetype

In this example, /path/to/your/data is the path to your data source, and your_sourcetype is the name of the sourcetype you want to assign to that data.

Step 4: Define Field Extractions

You can define regular expressions or use pre-built extraction techniques to parse fields from the data. Here’s an example of defining field extractions in props.conf:

[your_sourcetype] 

EXTRACT-fieldname1 = regular_expression1 
EXTRACT-fieldname2 = regular_expression2

Replace your_sourcetype with the actual sourcetype name you defined. fieldname1 and fieldname2 represent the names of the fields you want to extract, while regular_expression1 and regular_expression2 are the regular expressions used to match and extract the desired values.

Step 5: Save and Restart Splunk

After making changes to props.conf, save the file, and restart Splunk to apply the new configurations. You can do this using the Splunk web interface or by using the command line.

Step 6: Verify and Search the Data

Once Splunk restarts, you can search and verify that the data is being parsed correctly. You can use the extracted fields to filter and analyze the data effectively.

In the next task, we will explore important configuration files.

Splunk uses several configuration files to control various data processing and indexing aspects. Let’s explore some of the key configuration files in Splunk, along with examples of their usage:

inputs.conf

Purpose: Defines data inputs and how to collect data from different sources.
Example: Suppose you want to monitor a specific log file. You can configure inputs.conf as follows:
[monitor:///path/to/logfile.log]
sourcetype = my_sourcetype
props.conf

Purpose: Specifies parsing rules for different sourcetypes to extract fields and define field extractions.
Example: Suppose you have a custom sourcetype named my_sourcetype and want to extract fields using regular expressions. You can define them in props.conf.
[my_sourcetype] EXTRACT-field1 = regular_expression1 
EXTRACT-field2 = regular_expression2
transforms.conf

Purpose: Allows you to define field transformations and enrichments on indexed events.
Example: Suppose you want to add a new event field based on existing field values. You can use transforms.conf.
[add_new_field] REGEX = existing_field=(.*) FORMAT = new_field::$1
indexes.conf

Purpose: Manages the configuration of indexes in Splunk, including storage, retention policies, and access control.
Example: Suppose you want to create a new index named my_index with specific settings. You can configure indexes.conf.

[my_index] homePath = $SPLUNK_DB/my_index/db 
coldPath = $SPLUNK_DB/my_index/colddb 
thawedPath = $SPLUNK_DB/my_index/thaweddb 
maxTotalDataSizeMB = 100000
outputs.conf

Purpose: Specifies the destination and settings for sending indexed data to various outputs, such as remote Splunk instances or third-party systems.
Example: Suppose you want to forward your indexed data to a remote Splunk indexer. You can configure outputs.conf.
[tcpout] defaultGroup = my_indexers 
[tcpout:my_indexers] 
server = remote_indexer:9997
authentication.conf

Purpose: Manages authentication settings and user authentication methods.
Example: Suppose you want to enable LDAP authentication for Splunk users. You can configure authentication.conf.
[authentication] 
authSettings = LDAP 
[authenticationLDAP] 
SSLEnabled = true
These are just a few examples of the various configuration files used in Splunk. Each file serves a specific purpose and allows you to customize Splunk’s behavior based on your data sources, parsing requirements, indexing settings, output destinations, and more.

STANZAS in Splunk Configurations
Splunk configurations contain various stanza configurations that define how data is processed and indexed. These stanzas have a certain purpose, and it's important to understand what these are and how they are used. A brief summary of the common stanzas are explained below:

Stanza	Explanation	Example
[sourcetype]	Specifies the configuration for a specific sourcetype. It allows you to define how the data from that sourcetype should be parsed and indexed.	[apache:access] - Configures parsing and indexing settings for Apache access logs.
TRANSFORMS	Applies field transformations to extracted events. You can reference custom or pre-defined field transformation configurations to modify or create new fields based on the extracted data.	TRANSFORMS-mytransform = myfield1, myfield2 - Applies the transformation named “mytransform” to fields myfield1 and myfield2.
REPORT	Defines extraction rules for specific fields using regular expressions. It associates a field name with a regular expression pattern to extract desired values. This stanza helps in parsing and extracting structured fields from unstructured or semi-structured data.	REPORT-field1 = pattern1 - Extracts field1 using pattern1 regular expression.
EXTRACT	Defines extraction rules for fields using regular expressions and assigns them specific names. It is similar to the REPORT stanza, but it allows more flexibility in defining custom field extractions.	EXTRACT-field1 = (?<fieldname>pattern1) - Extracts field1 using pattern1 regular expression and assigns it to fieldname.
TIME_PREFIX	Specifies the prefix before the timestamp value in events. This stanza is used to identify the position of the timestamp within the event.	TIME_PREFIX = \[timestamp\] - Identifies the prefix [timestamp] before the actual timestamp in events.
TIME_FORMAT	Defines the format of the timestamp present in the events. It allows Splunk to correctly extract and parse timestamps based on the specified format.	TIME_FORMAT = %Y-%m-%d %H:%M:%S - Specifies the timestamp format as YYYY-MM-DD HH:MM:SS.
LINE_BREAKER	Specifies a regular expression pattern that identifies line breaks within events. This stanza is used to split events into multiple lines for proper parsing and indexing.	LINE_BREAKER = ([\r\n]+) - Identifies line breaks using the regular expression [\r\n]+.
SHOULD_LINEMERGE	Determines whether lines should be merged into a single event or treated as separate events. It controls the behavior of line merging based on the specified regular expression pattern in the LINE_BREAKER stanza.	SHOULD_LINEMERGE = false - Disables line merging, treating each line as a separate event.
BREAK_ONLY_BEFORE	Defines a regular expression pattern that marks the beginning of an event. This stanza is used to identify specific patterns in the data that indicate the start of a new event.	BREAK_ONLY_BEFORE = ^\d{4}-\d{2}-\d{2} - Identifies the start of a new event if it begins with a date in the format YYYY-MM-DD.
BREAK_ONLY_AFTER	Specifies a regular expression pattern that marks the end of an event. It is used to identify patterns in the data that indicate the completion of an event.	BREAK_ONLY_AFTER = \[END\] - Marks the end of an event if it contains the pattern [END].
KV_MODE	Specifies the key-value mode used for extracting field-value pairs from events. The available modes are: auto, none, simple, multi, and json. This stanza determines how fields are extracted from the events based on the key-value pairs present in the data. It helps in parsing structured data where fields are represented in a key-value format.	KV_MODE = json - Enables JSON key-value mode for parsing events with JSON formatted fields.
These examples demonstrate the usage of each stanza in props.conf and provide a better understanding of how they can be applied to configure data parsing behavior in Splunk.

# Creating a Simple Splunk App

We have explored the importance and usage of various configuration files and the purpose-based stanzas within those configuration files. We will be using them extensively in the coming tasks. For now, let’s create a simple Splunk app using the following steps and generate our first sample event using inputs.conf file.

Start Splunk
Splunk is installed in the /opt/splunk directory. Go to this directory and run the following command bin/splunk start to start the Splunk instance with root privileges. Use the following credentials to log in to the Splunk Interface:

Username: splunk

Password: splunk123

Once it is done, open 10.201.11.49:8000 in the browser.

About Splunk Apps
Splunk apps are pre-packaged software modules or extensions that enhance the functionality of the Splunk platform. The purpose of Splunk apps is to provide specific sets of features, visualizations, and configurations tailored to meet the needs of various use cases and industries.

Create a simple App

<img width="1093" height="1016" alt="image" src="https://github.com/user-attachments/assets/53980834-6c10-4e45-abe9-ebbddbbf56c4" />


Next, fill in the details about the new app that we want to create. The new app will be placed in the /opt/splunk/etc/apps directory as highlighted below:

<img width="1210" height="62" alt="image" src="https://github.com/user-attachments/assets/84c6f8c4-bf5c-45eb-9cfc-c7e40b3e765d" />


Go to the app directory /opt/splunk/etc/apps , where we can locate our newly created app DataApp, as shown below:

<img width="762" height="388" alt="image" src="https://github.com/user-attachments/assets/1fc4a3cf-ead1-4398-ace2-4eb1b0a38178" />

As we learned that the bin directory contains the scripts required by the app, let's go to the bin directory and create a simple Python script using the command nano samplelogs.py, copy the following line in the file, and save.
<img width="928" height="281" alt="image" src="https://github.com/user-attachments/assets/cf4caf74-7565-4df7-b3a1-f120428dcc43" />

<img width="783" height="166" alt="image" src="https://github.com/user-attachments/assets/e5a485dd-25f5-4968-9cf9-daf557003114" />

## Creating Inputs.conf

In the default directory, we will create all necessary configuration files like inputs.conf, transform.conf, etc. For now, let’s create an inputs.conf using the command nano inputs.conf add the following content into the file and save.

<img width="729" height="188" alt="image" src="https://github.com/user-attachments/assets/dc356842-4fa4-4667-a48c-adf5cb8efbcd" />

The above configuration picks the output from the script samplelogs.py and sends it to Splunk with the index main every 5 seconds.

Restart Splunk using the command /opt/splunk/bin/splunk restart.

<img width="774" height="137" alt="image" src="https://github.com/user-attachments/assets/f3245f11-5328-4305-8a83-842d9de8e769" />

<img width="986" height="548" alt="image" src="https://github.com/user-attachments/assets/39047134-066a-4ed3-bfbb-1bf9eed533a6" />


# Generating Events

Our first task is to configure Splunk to ingest these VPN logs. Copy the vpnlogs script into the bin directory, open the inputs.conf , and write these lines:

<img width="746" height="46" alt="image" src="https://github.com/user-attachments/assets/e2a79e4c-f9e7-4450-a48b-36064bc3ed64" />

[script:///opt/splunk/etc/apps/DataApp/bin/vpnlogs]
index = main
source = vpn
sourcetype = vpn_logs
interval = 5

<img width="760" height="266" alt="image" src="https://github.com/user-attachments/assets/a42a53ce-0b86-4720-bae0-bde36a9b3052" />


# Restart Splunk
Save the file and restart Splunk using the command /opt/splunk/bin/splunk restart. Open the Splunk instance at 10.201.11.49:8000 and navigate to the search head.

Search Head
Select the time range  All time (Real-time) and use the following search query to see if we are getting the logs.
Search Query: index=main sourcetype=vpn_logs

Search Head
Select the time range  All time (Real-time) and use the following search query to see if we are getting the logs.
Search Query: index=main sourcetype=vpn_logs

 Shows search head result showing VPN logs in real-time

Identifying the problem
Excellent, we are getting the VPN logs after every 5 seconds. But can you observe the problem? It's evident that Splunk cannot determine the boundaries of each event and considers multiple events as a single event. By default, Splunk breaks the event after carriage return.
<img width="1012" height="524" alt="image" src="https://github.com/user-attachments/assets/42ab62fb-56d9-4898-b456-aef9bbc28000" />

Fixing the Event Boundary
We need to fix the event boundary. To configure Splunk to break the events in this case, we have to make some changes to the props.conf file. First, we will create a regex to determine the end of the event. The sample events are shown below:

We will use reg101.com to create a regex pattern. If we look closely, all events end with the terms DISCONNECT or CONNECT. We can use this information to create a regex pattern (DISCONNECT|CONNECT) , as shown below:

<img width="811" height="388" alt="image" src="https://github.com/user-attachments/assets/96d739fe-f8a9-4a7c-9222-42a490d31029" />

Now, let’s create a props.conf in the default directory within the DataApp and add the following lines:

[vpn_logs]
SHOULD_LINEMERGE = true
MUST_BREAK_AFTER = (DISCONNECT|CONNECT)
This configuration tells Splunk to take the sourcetype to merge all lines and it must break the events when you see the pattern matched in the mentioned regex.


<img width="787" height="187" alt="image" src="https://github.com/user-attachments/assets/d42a53a7-5a66-48c2-8fa9-cd396483f550" />

Restart Splunk
Save the file and restart Splunk using the command /opt/bin/splunk restart. Open the Splunk instance at 10.201.11.49:8000 and navigate to the search head.

That’s it. We can see that with a few changes in the props.conf file, we changed how Splunk broke these VPN logs generated by the custom vpn_server.

In the next task, we will look at a different case study.

<img width="980" height="581" alt="image" src="https://github.com/user-attachments/assets/ea6b7051-1c18-472f-9289-fca365507ff6" />


As we know, different log sources have their own ways of generating logs. What if, a log source generates event logs that comprise of multi-lines? One such example is Windows Event logs. In order to understand how multi-line events can be handled in Splunk, we will use the event logs generated from the script authentication_logs. The sample event log is shown below:

[Authentication]:A login attempt was observed from the user Michael Brown and machine MAC_01
at: Mon Jul 17 08:10:12 2023 which belongs to the Custom department. The login attempt looks suspicious.
As it is clearly shown, the event contains multiple lines. Let’s update the inputs.conf file to include this script and see if Splunk is able to break the event as intended.

Copy the authentication_logs script from the ~/Downloads/scripts directory into the bin folder of the DataApp and add the following lines in inputs.conf, save the file, and restart Splunk:

<img width="781" height="89" alt="image" src="https://github.com/user-attachments/assets/298f8a97-c6ac-4983-a5d8-4a8fe5aa0148" />
<img width="689" height="234" alt="image" src="https://github.com/user-attachments/assets/acfc577a-ff6d-402d-920e-faaacf2fd5b2" />

[script:///opt/splunk/etc/apps/DataApp/bin/authentication_logs]
interval = 5
index = main
sourcetype= auth_logs
host = auth_server
Search Head
Let’s look at the Splunk Search head to see how these logs are reflected.

Search Query: index=main sourcetype = auth_logs

Identifying the problem

If we observe the events, we will see that Splunk is breaking the 2-line Event into 2 different events and is unable to determine the boundaries.

Fixing the Event Boundary
In order to fix this issue, we can use different stanzas in the props.conf file. If we run the script a few times to observe the output, we can see that each event starts with the term [Authentication], indicating the start of the event. We can use this as the regex pattern with the stanza BREAK_ONLY_BEFORE and see if it could fix this problem. Copy the following lines in props.conf file, save the file, and then restart Splunk to apply changes.

<img width="670" height="214" alt="image" src="https://github.com/user-attachments/assets/0c46bf17-8aa6-4ff9-acd5-8eaad9de0b34" />

<img width="787" height="122" alt="image" src="https://github.com/user-attachments/assets/3fa6cd04-e168-4cda-b88e-0d2b0f26974f" />


Search head
Go to Splunk Search head, and use the following search query.

Search Query: index=main sourcetype = auth_logs

<img width="1124" height="584" alt="image" src="https://github.com/user-attachments/assets/54dabee5-5f91-435d-bb59-f212e6ea2626" />

<img width="1263" height="253" alt="image" src="https://github.com/user-attachments/assets/37c33688-0a5b-402b-afc8-7dbb6652931f" />

# Masking Sensitive Data

Masking sensitive fields, such as credit card numbers, is essential for maintaining compliance with standards like PCI DSS (Payment Card Industry Data Security Standard) and HIPAA (Health Insurance Portability and Accountability Act). Splunk provides features like field masking and anonymization to protect sensitive data. Here’s an example of credit card numbers being populated in the Event logs generated by the script purchase-details present in the ~/Downloads/scripts directory.
Sample Output

User William made a purchase with credit card 3714-4963-5398-4313.
User John Boy made a purchase with credit card 3530-1113-3330-0000.
User Alice Johnson made a purchase with credit card 6011-1234-5678-9012.
User David made a purchase with credit card 3530-1113-3330-0000.
User Bob Williams made a purchase with credit card 9876-5432-1098-7654.
Copy this script file into the bin folder of the DataApp and configure the inputs.conf file to ingest these logs into Splunk. To do so, add the following lines in the inputs.conf file.

<img width="764" height="168" alt="image" src="https://github.com/user-attachments/assets/ff2d30df-5e3b-4952-b7fb-d31b8248284e" />

[script:///opt/splunk/etc/apps/DataApp/bin/purchase-details]
interval = 5
index = main
source = purchase_logs
sourcetype= purchase_logs
host = order_server

This configuration tells Splunk to get the output from the purchase-details script, and index into the main index every 5 seconds, with sourcetype  purchase_logs and host as order_server. Now, save the file and restart Splunk. Log on to Splunk and apply the following search query: Search Query: index=main sourcetype=purchase_logs

<img width="656" height="137" alt="image" src="https://github.com/user-attachments/assets/e1bb6617-6057-47be-bed8-39760750c985" />

It looks like we have two problems to address. We need to hide the credit card information that is being added to each event and also need to fix the event boundaries.

<img width="999" height="531" alt="image" src="https://github.com/user-attachments/assets/019f0d0c-b7bd-4101-a17b-f08be2d0df9e" />


Fixing Event Boundaries
We will use regex101.com to create a regex pattern to identify the end boundary of each event, as shown below:

<img width="983" height="302" alt="image" src="https://github.com/user-attachments/assets/8d0bdb70-aff1-4f7a-a38b-a4778207ec04" />

Masking CC Information

Let’s now use the above knowledge gain to create a regex that replaces the credit card number with something like this -> 6011-XXXX-XXXX-XXXX., as shown below:

 Shows Regex pattern matching results

Now, our task is to use this s/OLD_VALUE>/<NEW_VALUE>/g regex in sedcmd to replace the credit card numbers with XXXX-XXXX-XXXX. The final sedcmd value will become s/-\d{4}-\d{4}-\d{4}/-XXXX-XXXX-XXXX/g

Our configuration in the props.conf would look like this:
<img width="715" height="226" alt="image" src="https://github.com/user-attachments/assets/2cd24b1a-d4c8-42da-9e2f-24ddd46d5be5" />


Restart Splunk and check Splunk Instance to see how our changes are reflected in the logs.

<img width="847" height="412" alt="image" src="https://github.com/user-attachments/assets/31302786-9629-4065-ae03-2e194feff53d" />


<img width="1255" height="247" alt="image" src="https://github.com/user-attachments/assets/c6e77887-8366-4d53-a306-a4b8014d5a32" />


# Extracting Custom Fields

From a SOC analyst’s point of view, we would often encounter logs either custom log sources, where not all fields are extracted by the SIEM automatically, or we are required to extract custom fields to improve the analysis. In that case, we need a way to extract custom fields from the logs. To demonstrate this with an example, let’s go back to our vpn_logs case. The output we are getting in Splunk is, as shown below:

<img width="1050" height="616" alt="image" src="https://github.com/user-attachments/assets/af1d64e0-05bf-4d3a-b87e-e8c717b30d02" />

It's clear that none of the fields are extracted automatically, and we can not perform any analysis on these events until fields like username, server, and action are extracted.

Extracting Username
Let’s first go through the process of extracting the usernames and putting them under the field as Username, and then we can follow the same steps to extract other fields as well.

Creating Regex Pattern
Our first task would be to create a regex pattern to capture the username values we are trying to capture. Sample event logs look like this:

User: John Doe, Server: Server C, Action: CONNECT
User: John Doe, Server: Server A, Action: DISCONNECT
User: Emily Davis, Server: Server E, Action: CONNECT
User: Emily Davis, Server: Server D, Action: DISCONNECT
User: Michael Brown, Server: Server A, Action: CONNECT
User: Alice Smith, Server: Server C, Action: CONNECT
User: Emily Davis, Server: Server C, Action: DISCONNECT
User: John Doe, Server: Server C, Action: CONNECT
User: Michael Brown, Server: Server A, Action: DISCONNECT
User: John Doe, Server: Server D, Action: DISCONNECT

By creating a regex pattern as: User:\s([\w\s]+) and creating a capturing group, we have successfully captured all the usernames that we want to extract.


# Creating and Updating transforms.conf

Now, let’s create a transforms.conf in the default folder of the DataApp directory, and put the following configurations in it as it is.


<img width="919" height="230" alt="image" src="https://github.com/user-attachments/assets/dd218819-549c-4e52-a626-e23a7e4a7ba4" />

# Updating props.conf

We need to update the props.conf to mention the recent updates we did in transforms.conf. Here, we are appending the configuration for sourcetype vpn_logs with the line TRANSFORM-vpn = vpn_custom_fields, as shown below:

<img width="628" height="302" alt="image" src="https://github.com/user-attachments/assets/6a666e1b-8fd6-4a44-a8ca-486965be0411" />

# Creating and Updating fields.conf

The next step would be to create fields.conf and mention the field we are going to extract from the logs, which is Username. INDEXED = true means we are telling Splunk to extract this field at the indexed time.

<img width="708" height="154" alt="image" src="https://github.com/user-attachments/assets/c07108f2-3fcd-4557-b535-cbfc1267af06" />

# Restart Splunk

That’s all we need in order to extract the custom fields. Now, restart the Splunk instance so that the changes we have made are committed. Go to the Splunk instance and use the search query index=main sourcetype=vpn_logs



