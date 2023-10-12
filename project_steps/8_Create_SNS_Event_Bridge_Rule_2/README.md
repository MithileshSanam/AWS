<h1>8. Create SNS and EventBridge Rule-2</h1>
<p><h3>Tools used</h3>
<ul>
<li>EventBridge</li>
<li>SNS</li>
</ul>
</p>

<p><h3>Steps</h3>
<ol>

  <li>Enter SNS in search bar and click on SNS</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/8_Create_SNS_Event_Bridge_Rule_2/images/8.1.png?raw=true alt="Create EventBridge rule">

  <li>Click Create Topic</li>
  <li>Select Standard Type. Enter topic name. Enter email address in Display name</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/8_Create_SNS_Event_Bridge_Rule_2/images/8.2.png?raw=true alt="Create EventBridge rule">

  <li>Click create subscription</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/8_Create_SNS_Event_Bridge_Rule_2/images/8.3.png?raw=true alt="Create EventBridge rule">

  <li>SNS ARN is prepopulated. Select EMAIL protocol. Enter email address in EndPoint. Click create subscription</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/8_Create_SNS_Event_Bridge_Rule_2/images/8.4.png?raw=true alt="Create EventBridge rule">


  <li>Navigate to EventBridge</li>
  <li>Follow steps in <a href="https://github.com/MithileshSanam/AWS/tree/main/project_steps/6_Create_Event_Bridge_Rule_1">6_Create_Event_Bridge_Rule_1</a> to create another event. In step-2, enter below pattern <a href="https://github.com/MithileshSanam/AWS/blob/main/code/eventbridge_rule_2.json">Rule-2 JSON</a></li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/8_Create_SNS_Event_Bridge_Rule_2/images/8.5.png?raw=true alt="Create EventBridge rule">

  <li>In Step-3, Select AWS Service. Select SNS as target. Select topic created above.</li>
  <img src="https://github.com/MithileshSanam/AWS/blob/main/project_steps/8_Create_SNS_Event_Bridge_Rule_2/images/8.6.png?raw=true alt="Create EventBridge rule">

  <li>Click Review and Create</li>

</ol>
</p>
