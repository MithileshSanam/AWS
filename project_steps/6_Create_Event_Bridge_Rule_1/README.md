<h1>6. Create EventBridge Rule-1</h1>
<p><h3>Tools used</h3>
<ul>
<li>EventBridge</li>
<li>IAM</li>
</ul>
</p>

<p><h3>Steps</h3>
<ol>

  <li>Enter EventBridge in search bar to find and click EventBridge in the result.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/6_Create_Event_Bridge_Rule_1/images/6.1.png?raw=true alt="Create EventBridge rule">

  <li>Select create rule</li>

  <li>Step-1 Enter rule name. Click next</li>
  <li>Step-2 Event source Select others. Select custom pattern for creation method and edit the json to below. Same is available in <a href="https://github.com/MithileshSanam/AWS/blob/main/code/eventbridge_rule_1.json?raw=true">Rule-1 JSON</a></li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/6_Create_Event_Bridge_Rule_1/images/6.2.png?raw=true alt="Create EventBridge rule">
  <li>Step-3 Select Target as AWS services. Select Lambda and chose lambda function-2 created recently.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/6_Create_Event_Bridge_Rule_1/images/6.3.png?raw=true alt="Create EventBridge rule">
  <li>Click Next and in Step-5 click review and create.</li>
</ol>
</p>
