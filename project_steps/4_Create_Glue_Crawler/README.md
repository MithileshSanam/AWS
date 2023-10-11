<h1>4. Create Glue Crawler</h1>
<p><h3>Tools used</h3>
<ul>
<li>Glue Crawler</li>
<li>IAM</li>
</ul>
</p>

<p><h3>Steps</h3>
<ol>
  <li>Navigate to IAM</li>
  <li>Create role. Enter AWS service as Glue. Click next.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.3.png?raw=true alt="Create glue crawler">
  <li>Add below permissions and enter role name and click create role.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.4.png?raw=true alt="Create glue crawler">


  <li>Enter glue in search bar to find and click glue in the result.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.1.png?raw=true alt="Create glue crawler">
  <li>Navigate to crawler and click on create crawler</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.2.png?raw=true alt="Create glue crawler">

  <li>In step-1, enter crawler name (should be same as provided in lambda function code previously) and click next</li>
  <li>In step-2, Click add data source</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.5.png?raw=true alt="Create glue crawler">
  <li>Enter data source as S3. Provide S3 as your demo-1 bucket. include raw/ as well. Click add data source.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.6.png?raw=true alt="Create glue crawler">

  <li>In Step-3, Select IAM role created before.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.7.png?raw=true alt="Create glue crawler">

  <li>In Step-4, click add database</li>

  <li>Enter database name. Click create database</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.8.png?raw=true alt="Create glue crawler">
  <li>Navigate back to create crawler page, refresh and select database. Click Next.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/4_Create_Glue_Crawler/images/4.9.png?raw=true alt="Create glue crawler">
  <li>In Step-5, click review and create</li>
</ol>
</p>
