<h1>3. Create and configure Lambda function for JSON to CSV</h1>
<p><h3>Tools used</h3>
<ul>
<li>Lambda</li>
<li>SQS</li>
<li>IAM</li>
</ul>
</p>

<p><h3>Steps</h3>
<ol>
  <li>Enter lambda in search bar to find and click lambda in the result.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/3_Create_Lambda_1/images/3.1.png?raw=true alt="Create Lambda">
  <li>Click create function.</li>
  <li>Enter function name. Select Python as runtime.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/3_Create_Lambda_1/images/3.2.png?raw=true alt="Create Lambda">
  <li>Under permissions, click create new role from AWS policy templates. Search for SQS and select the role. Click create function</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/3_Create_Lambda_1/images/3.3.png?raw=true alt="Create Lambda">

  <li>Navigate to IAM. (Search for IAM in search bar) </li>
  <li>Navigate to recently created role. Click add permissions and then attach policy. Select AmazonS3FullAccess, AWSGlueServiceRole. Click create permissions</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/3_Create_Lambda_1/images/3.4.png?raw=true alt="Create Lambda">

  <li>Navigate to lambda function created before. Click on Add trigger</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/3_Create_Lambda_1/images/3.5.png?raw=true alt="Create Lambda">

  <li>Select SQS. Select SQS queue. Click on add</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/3_Create_Lambda_1/images/3.6.png?raw=true alt="Create Lambda">

  <li>Trigger is created. Same can be verified in SQS queue lambda trigger section as well.</li>
  <li>In code, enter code in <a href='https://github.com/MithileshSanam/AWS/blob/main/code/lambda_function_1.py'>Lambda function-1</a></li>

</ol>
</p>
