# 3-Tier Architecture

There are multiple ways to do this. I have provided 2 options - 1 is using serverless framework. Other is using EC2 instance to run the backend.
3 tiers are given below,
<li>Java REST API published as lambda functions served by API Gateway.</li>
<li>DynamoDB for Database</li>
<li>Frontend (any Javascript framework like React JS) can be deployed using AWS Amplify and this is not included in the yaml script</li>

For 2nd option, terraform is being used.
To make it modular and reusable, code is provided as main, variable and outputs
