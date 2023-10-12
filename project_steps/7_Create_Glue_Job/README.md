<h1>7. Create Glue Job</h1>
<p><h3>Tools used</h3>
<ul>
<li>Glue</li>
<li>IAM</li>
</ul>
</p>

<p><h3>Steps</h3>
<ol>

  <li>Enter Glue in search bar to find and click Glue in the result.</li>
  <li>Click on Visual ETL. Select Visual with a source and target. Select source as AWS Glue Catalog and target as Amazon S3. Click create</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/7_Create_Glue_Job/images/7.1.png?raw=true alt="Create Glue Job">

  <li>Click on Plus icon at top left of Visual section to add node. Select change schema</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/7_Create_Glue_Job/images/7.2.png?raw=true alt="Create Glue Job">
  <li>Click on Data source node. Enter node name, select glue database and glue table</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/7_Create_Glue_Job/images/7.3.png?raw=true alt="Create Glue Job">
  <li>Click on Transform change schema node. Enter node name, select parent as source node and update schema as required</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/7_Create_Glue_Job/images/7.4.png?raw=true alt="Create Glue Job">
  <li>Click on Data target node. Enter node name, select parent as transform change schema node, select format as parquet and enter output S3 path</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/7_Create_Glue_Job/images/7.5.png?raw=true alt="Create Glue Job">
  <li>In Script tab, <a href="https://github.com/MithileshSanam/AWS/blob/main/code/glue_script.py">python script</a> is generated based visual ETL nodes.</li>
  <li>Select Job details tab. Select same IAM role as provided for glue crawler.</li>
  <li>Click Save</li>

</ol>
</p>
