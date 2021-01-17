# 3-Tier Architecture

There are multiple ways to do this. I have provided 2 options - 1 is using serverless option. Other is using EC2 instance to run the backend.

3 tiers are given below,
<li>Backend - can be Java, Go etc</li>
<li>DynamoDB for Database</li>
<li>Frontend (any Javascript framework like React JS) can be deployed using AWS Amplify and this is not included in the yaml/terraform script</li>


For 1st option, serverless framework is being used. serverless.yaml file contains all the script.
<li>Java REST API published as lambda functions served by API Gateway.</li>
<li>DynamoDB for Database</li>
<li>Frontend (any Javascript framework like React JS) can be deployed using AWS Amplify and this is not included in the yaml script</li>


For 2nd option, terraform is being used. Here, I have given for EC2. Instead of EC2, it can be container cluster using ECS or EKS
To make it modular and reusable, code is provided as main, variable and outputs
