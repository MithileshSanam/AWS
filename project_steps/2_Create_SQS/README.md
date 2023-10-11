<h1>2. Create and configure SQS Queue</h1>
<p><h3>Tools used</h3>
<ul>
<li>S3</li>
<li>SQS</li>
</ul>
</p>

<p><h3>Steps</h3>
<ol>
  <li>Enter SQS in search bar to find and click SQS in the result.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.1.png?raw=true alt="Create SQS">
  <li>Click create queue.</li>
  <li>Select standard and enter queue name. Click on create queue</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.2.png?raw=true alt="Create SQS">
  <li>Click Edit button. Navigate to access policy and copy Resource arn (line 12). Click policy generator</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.3.png?raw=true alt="Create SQS">
  <li>In policy generator, <ol>
  <li>enter principal as *</li>
  <li>Select All Actions check box</li>
  <li>Paste ARN of SQS service copied before (step 4) in ARN text box</li>
  </ol>
  click on Add Conditions (Optional)</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.4.png?raw=true alt="Create SQS">
  <li>Navigate to S3 demo1 bucket. In properties section, copy ARN</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.5.png?raw=true alt="Create SQS">
  <li>Navigate back to policy generator. Select condition as ArnEquals (appears as default). Select sourceARN as key. Paste S3 bucket ARN in value. Click Add condition.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.6.png?raw=true alt="Create SQS">
  <li>Click on Add statement and click on Generate policy. Copy the entire policy JSON</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.7.png?raw=true alt="Create SQS">
  <li>Navigate to Edit Queue page. In access policy section, replace entire JSON policy with policy copied before</li>
  <li>Click Save</li>
  <li>Navigate back to S3 demo-1 bucket. In properties section, click on create Event Notification</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.8.png?raw=true alt="Create SQS">
  <li>Enter event name. Enter raw/ as prefix (this is the folder inside demo-1 bucket). Select checkbox of all object create events.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.9.png?raw=true alt="Create SQS">
  <li>In destination section, select SQS and choose SQS queue. Click save changes</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/2_Create_SQS/images/2.10.png?raw=true alt="Create SQS">
</ol>
</p>
