<h1>End to End Testing</h1>

<p><h3>Steps</h3>
<ol>
  <li>Navigate to source S3 bucket (demo-1)</li>
  <li>Upload json file in raw folder. Sample file in <a href="https://github.com/MithileshSanam/AWS/blob/main/files/sales_records.json">here</a></li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/1.png?raw=true alt="testing">

  <li>Navigate to SQS queue. Messages available shows no of messages available in queue (before polling). Messages in Flight shows no. of messages currently being polled. Since Lambda automatically polls from SQS, quickly it reverts to zero.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/2.png?raw=true alt="testing">
  <li>Navigate to Lambda function-1 (json to csv function). </li>
  <li>In Monitor tab, click on View Cloudwatch logs. Lambda has access to create and view logs in Cloudwatch</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/3.png?raw=true alt="testing">

  <li>In Cloudwatch, it is navigated to log group created for the lambda function. New entry is appeared in logstream. Click on the same.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/4.png?raw=true alt="testing">

  <li>Verify the logs for creating csv file in demo-2 bucket and starting crawler.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/5.png?raw=true alt="testing">

  <li>Navigate to demo-2 S3 to verify newly created csv file</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/6.png?raw=true alt="testing">

  <li>Navigate to glue crawler to verify new entry in crawler run</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/7.png?raw=true alt="testing">

  <li>Navigate to glue table to verify table creation</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/8.png?raw=true alt="testing">

  <li>Click on Table data for the table to navigate to Athena. Or search for Athena in search box.</li>
  <li>Click manage settings in Athena. Enter S3 path for Athena</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/9.png?raw=true alt="testing">

  <li>Run query in Athena to validate the result</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/10.png?raw=true alt="testing">
  <li>Glue crawler creates event for EventBridge which triggers second lambda function which runs glue job to convert data from glue catalog table to parquet and stores in S3</li>
  <li>Navigate to second lambda function and click on view Cloudwatch logs button in Monitor section. Click on new entry in log stream</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/11.png?raw=true alt="testing">
  <li>Verify logs for any errors</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/12.png?raw=true alt="testing">
  <li>Navigate to Glue job. Click on job. In Runs tab, check for status in new entry</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/13.png?raw=true alt="testing">
  <li>Navigate to S3 path for parquet provided in Glue Job. parquet file shall be created.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/14.png?raw=true alt="testing">
  <li>EventBridge email notification rule triggers SNS which sends an email to email address</li>
  <li>Same can be verified in email</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/End_to_End_Testing/images/15.png?raw=true alt="testing">
</ol>
</p>
