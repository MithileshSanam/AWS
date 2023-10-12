<h1>5. Create Lambda-2</h1>
<p><h3>Tools used</h3>
<ul>
<li>Lambda</li>
<li>IAM</li>
</ul>
</p>

<p><h3>Steps</h3>
<ol>

  <li>Enter glue in search bar to find and click glue in the result.</li>
  <li>Create a lambda function. Follow steps as <a href="https://github.com/MithileshSanam/AWS/tree/main/project_steps/3_Create_Lambda_1">3_Create_Lambda_1</a> for the same. For IAM role, instead of SQS, select cloud watch as service.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/5_Create_Lambda_2/images/5.1.png?raw=true alt="Create lambda">

  <li>Navigate to IAM. For the role created above, select below permissions.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/5_Create_Lambda_2/images/5.2.png?raw=true alt="Create lambda">
  <li>In code, enter code in <a href='https://github.com/MithileshSanam/AWS/blob/main/code/lambda_function_2.py'>Lambda function-2</a></li>
</ol>
</p>
