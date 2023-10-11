<h1>Serverless Data Processing and Automation with AWS Services</h1>


<p><h3>Architecture</h3>
<img src="https://github.com/MithileshSanam/AWS/blob/main/files/Project_architecture.jpg?raw=true alt="Search for S3">
</p>

<p><h3>Description</h3>

Designed and executed a comprehensive serverless data processing and automation project leveraging a suite of AWS services. The project entailed the following key steps:
<ol>
<li>Developed an end-to-end data processing automation workflow using AWS services to perform below activities:
<ul>

<li>convert JSON file to CSV by applying transformation using lambda.</li>
<li>Crawling data from CSV into glue tables.</li>
<li>Running glue job to convert data from glue table into parquet format and store in S3.</li>
<li>Email Notification using SNS.</li>

</ul>
</li>
<li>Utilized SQS queue as a trigger for AWS Lambda and established event notification from S3 to SQS.</li>
<li>Utilized AWS Lambda for JSON-to-CSV transformation, with CloudWatch logs for monitoring and troubleshooting and for running Glue crawler to catalog and prepare the data for querying.</li>
<li>Validated the process using Amazon Athena to run SQL queries on the data.</li>
<li>Integrated AWS EventBridge to automate the conversion of data to Parquet format, stored in S3 through Lambda function calling Glue Job for the same.</li>
<li>Monitored the entire process with CloudWatch logs for Lambda and Glue jobs.</li>
<li>Implemented an EventBridge email notification rule, triggering an SNS notification for success email alerts.</li>

</ol></p>

<p><h3>Tools used</h3>
<ul>
<li>S3</li>
<li>Lambda</li>
<li>SQS</li>
<li>Event Bridge</li>
<li>CloudWatch Logs</li>
<li>SNS</li>
<li>Glue Crawler</li>
<li>Glue Job</li>
<li>Athena</li>
<li>IAM</li>
</ul>
</p>
