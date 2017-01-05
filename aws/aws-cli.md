# AWS CLI

## Install

https://docs.aws.amazon.com/cli/latest/userguide/installing.html

[get-pip.py](https://bootstrap.pypa.io/get-pip.py) 다운로드

```
$ sudo python get-pip.py
```

```
$ sudo pip install --ignore-installed six
$ sudo pip install --ignore-installed python-dateutil
$ sudo pip install awscli
```

## Setup

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html

### Create access key

1. [IAM console](https://console.aws.amazon.com/iam/home?#/home)에서 user 생성
1. 생성한 user 페이지에서 Security credentails 탭으로 이동
1. Create access key 버튼 클릭
1. Download .csv file 버튼 클릭
1. 파일 안에 Access key ID와 Secret access key가 저장되어 있다.

### Configure CLI

```
$ aws configure
AWS Access Key ID [None]: AKIAJM7CY4LAKD3OG3AQ
AWS Secret Access Key [None]: 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
Default region name [None]: us-east-1
Default output format [None]: json
```

## References

- [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#gamelift-region)

## Use Cases

### Lambda

```
$ aws lambda create-function \
> --region us-east-1 \
> --function-name LambdaFunctionOverHttps  \
> --zip-file fileb://LambdaFunctionOverHttps.zip \
> --role arn:aws:iam::067884960258:role/lambda-gateway-execution-role \
> --handler LambdaFunctionOverHttps.handler \
> --runtime python2.7
{
    "CodeSha256": "KJ+1hRkwFJAok8eLi+9P40Jc4rpEKRTtshmyKutLstw=",
    "FunctionName": "LambdaFunctionOverHttps",
    "CodeSize": 690,
    "MemorySize": 128,
    "FunctionArn": "arn:aws:lambda:us-east-1:067884960258:function:LambdaFunctionOverHttps",
    "Version": "$LATEST",
    "Role": "arn:aws:iam::067884960258:role/lambda-gateway-execution-role",
    "Timeout": 3,
    "LastModified": "2016-12-01T12:16:09.190+0000",
    "Handler": "LambdaFunctionOverHttps.handler",
    "Runtime": "python2.7",
    "Description": ""
}
```

```
$ aws lambda list-functions
{
    "Functions": [
        {
            "Version": "$LATEST",
            "CodeSha256": "KJ+1hRkwFJAok8eLi+9P40Jc4rpEKRTtshmyKutLstw=",
            "FunctionName": "LambdaFunctionOverHttps",
            "MemorySize": 128,
            "CodeSize": 690,
            "FunctionArn": "arn:aws:lambda:us-east-1:067884960258:function:LambdaFunctionOverHttps",
            "Handler": "LambdaFunctionOverHttps.handler",
            "Role": "arn:aws:iam::067884960258:role/lambda-gateway-execution-role",
            "Timeout": 3,
            "LastModified": "2016-12-01T12:16:09.190+0000",
            "Runtime": "python2.7",
            "Description": ""
        }
    ]
}
```

```
aws lambda update-function-code \
--function-name AlexaSkillWhisen \
--zip-file fileb://lambda.zip 
```

```
aws lambda invoke \
--invocation-type Event \
--function-name LambdaFunctionOverHttps \
--region us-east-1 \
--payload file://input.txt \
outputfile.txt
>>>>>>> 10efd9bb305c45edbc22f8078aeaa73e566284df
{
    "StatusCode": 202
}
```

### API Gateway

```
aws apigateway create-rest-api \
--name DynamoDBOperations
{
    "name": "DynamoDBOperations",
    "id": "gkxnl9yril",
    "createdDate": 1480596292
}
```

```
aws apigateway get-resources \
--rest-api-id gkxnl9yril
{
    "items": [
        {
            "path": "/",
            "id": "95qkesnz4k"
        }
    ]
}
```

```
aws apigateway create-resource \
--rest-api-id gkxnl9yril \
--parent-id 95qkesnz4k \
--path-part DynamoDBManager
{
    "path": "/DynamoDBManager",
    "pathPart": "DynamoDBManager",
    "id": "umhk73",
    "parentId": "95qkesnz4k"
}
```

```
aws apigateway put-method \
--rest-api-id gkxnl9yril \
--resource-id umhk73 \
--http-method POST \
--authorization-type NONE
{
    "apiKeyRequired": false,
    "httpMethod": "POST",
    "authorizationType": "NONE"
}
```

```
aws apigateway put-integration \
--rest-api-id gkxnl9yril \
--resource-id umhk73 \
--http-method POST \
--type AWS \
--integration-http-method POST \
--uri arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:067884960258:function:LambdaFunctionOverHttps/invocations
{
    "httpMethod": "POST",
    "passthroughBehavior": "WHEN_NO_MATCH",
    "cacheKeyParameters": [],
    "type": "AWS",
    "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:067884960258:function:LambdaFunctionOverHttps/invocations",
    "cacheNamespace": "umhk73"
}
```

```
aws apigateway put-method-response \
--rest-api-id gkxnl9yril \
--resource-id umhk73 \
--http-method POST \
--status-code 200 \
--response-models "{\"application/json\": \"Empty\"}"
{
    "responseModels": {
        "application/json": "Empty"
    },
    "statusCode": "200"
}
```

```
aws apigateway put-integration-response \
--rest-api-id gkxnl9yril \
--resource-id umhk73 \
--http-method POST \
--status-code 200 \
--response-templates "{\"application/json\": \"\"}"
{
    "statusCode": "200",
    "responseTemplates": {
        "application/json": null
    }
}
```

```
aws apigateway create-deployment \
--rest-api-id gkxnl9yril \
--stage-name prod
{
    "id": "j89rck",
    "createdDate": 1480636899
}
```

```
aws lambda add-permission \
--function-name LambdaFunctionOverHttps \
--statement-id apigateway-test-2 \
--action lambda:InvokeFunction \
--principal apigateway.amazonaws.com \
--source-arn "arn:aws:execute-api:us-east-1:067884960258:gkxnl9yril/*/POST/DynamoDBManager"
{
    "Statement": "{\"Sid\":\"apigateway-test-2\",\"Resource\":\"arn:aws:lambda:us-east-1:067884960258:function:LambdaFunctionOverHttps\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"apigateway.amazonaws.com\"},\"Action\":[\"lambda:InvokeFunction\"],\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:execute-api:us-east-1:067884960258:gkxnl9yril/*/POST/DynamoDBManager\"}}}"
}
```

```
aws lambda add-permission \
--function-name LambdaFunctionOverHttps \
--statement-id apigateway-prod-2 \
--action lambda:InvokeFunction \
--principal apigateway.amazonaws.com \
--source-arn "arn:aws:execute-api:us-east-1:067884960258:gkxnl9yril/prod/POST/DynamoDBManager"
{
    "Statement": "{\"Sid\":\"apigateway-prod-2\",\"Resource\":\"arn:aws:lambda:us-east-1:067884960258:function:LambdaFunctionOverHttps\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"apigateway.amazonaws.com\"},\"Action\":[\"lambda:InvokeFunction\"],\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:execute-api:us-east-1:067884960258:gkxnl9yril/prod/POST/DynamoDBManager\"}}}"
}
```

```
aws apigateway test-invoke-method \
> --rest-api-id gkxnl9yril \
> --resource-id umhk73 \
> --http-method POST \
> --path-with-query-string "" \
> --body "{\"operation\":\"create\",\"tableName\":\"LambdaTable\",\"payload\":{\"Item\":{\"Id\":\"7\",\"name\":\"Kim\"}}}"
{
    "status": 200,
    "body": "{\"ResponseMetadata\": {\"RetryAttempts\": 0, \"HTTPStatusCode\": 200, \"RequestId\": \"DCFE83EB1EJAV8FFH5UIMD5CMBVV4KQNSO5AEMVJF66Q9ASUAAJG\", \"HTTPHeaders\": {\"x-amzn-requestid\": \"DCFE83EB1EJAV8FFH5UIMD5CMBVV4KQNSO5AEMVJF66Q9ASUAAJG\", \"date\": \"Sat, 03 Dec 2016 01:39:37 GMT\", \"content-length\": \"2\", \"content-type\": \"application/x-amz-json-1.0\", \"x-amz-crc32\": \"2745614147\"}}}",
    "log": "Execution log for request test-request\nSat Dec 03 01:39:37 UTC 2016 : Starting execution for request: test-invoke-request\nSat Dec 03 01:39:37 UTC 2016 : HTTP Method: POST, Resource Path: /DynamoDBManager\nSat Dec 03 01:39:37 UTC 2016 : Method request path: {}\nSat Dec 03 01:39:37 UTC 2016 : Method request query string: {}\nSat Dec 03 01:39:37 UTC 2016 : Method request headers: {}\nSat Dec 03 01:39:37 UTC 2016 : Method request body before transformations: {\"operation\":\"create\",\"tableName\":\"LambdaTable\",\"payload\":{\"Item\":{\"Id\":\"7\",\"name\":\"Kim\"}}}\nSat Dec 03 01:39:37 UTC 2016 : Endpoint request URI: https://lambda.us-east-1.amazonaws.com/2015-03-31/functions/arn:aws:lambda:us-east-1:067884960258:function:LambdaFunctionOverHttps/invocations\nSat Dec 03 01:39:37 UTC 2016 : Endpoint request headers: {x-amzn-lambda-integration-tag=test-request, Authorization=****************************************************************************************************************************************************************************************************************************************************************************************************************************************27f552, X-Amz-Date=20161203T013937Z, x-amzn-apigateway-api-id=gkxnl9yril, X-Amz-Source-Arn=arn:aws:execute-api:us-east-1:067884960258:gkxnl9yril/null/POST/DynamoDBManager, Accept=application/json, User-Agent=AmazonAPIGateway_gkxnl9yril, Host=lambda.us-east-1.amazonaws.com, X-Amz-Content-Sha256=331319bd9869a223d25dfd1ca5ffe6c2213ea63c74983f109be0d2d0d0f18f5e, X-Amzn-Trace-Id=Root=1-58422259-97da760e4d0f35d07106ebf9, Content-Type=application/json}\nSat Dec 03 01:39:37 UTC 2016 : Endpoint request body after transformations: {\"operation\":\"create\",\"tableName\":\"LambdaTable\",\"payload\":{\"Item\":{\"Id\":\"7\",\"name\":\"Kim\"}}}\nSat Dec 03 01:39:37 UTC 2016 : Endpoint response body before transformations: {\"ResponseMetadata\": {\"RetryAttempts\": 0, \"HTTPStatusCode\": 200, \"RequestId\": \"DCFE83EB1EJAV8FFH5UIMD5CMBVV4KQNSO5AEMVJF66Q9ASUAAJG\", \"HTTPHeaders\": {\"x-amzn-requestid\": \"DCFE83EB1EJAV8FFH5UIMD5CMBVV4KQNSO5AEMVJF66Q9ASUAAJG\", \"date\": \"Sat, 03 Dec 2016 01:39:37 GMT\", \"content-length\": \"2\", \"content-type\": \"application/x-amz-json-1.0\", \"x-amz-crc32\": \"2745614147\"}}}\nSat Dec 03 01:39:37 UTC 2016 : Endpoint response headers: {x-amzn-Remapped-Content-Length=0, x-amzn-RequestId=59af801b-b8f9-11e6-b200-7d58a248a566, Connection=keep-alive, Content-Length=366, Date=Sat, 03 Dec 2016 01:39:37 GMT, Content-Type=application/json}\nSat Dec 03 01:39:37 UTC 2016 : Method response body after transformations: {\"ResponseMetadata\": {\"RetryAttempts\": 0, \"HTTPStatusCode\": 200, \"RequestId\": \"DCFE83EB1EJAV8FFH5UIMD5CMBVV4KQNSO5AEMVJF66Q9ASUAAJG\", \"HTTPHeaders\": {\"x-amzn-requestid\": \"DCFE83EB1EJAV8FFH5UIMD5CMBVV4KQNSO5AEMVJF66Q9ASUAAJG\", \"date\": \"Sat, 03 Dec 2016 01:39:37 GMT\", \"content-length\": \"2\", \"content-type\": \"application/x-amz-json-1.0\", \"x-amz-crc32\": \"2745614147\"}}}\nSat Dec 03 01:39:37 UTC 2016 : Method response headers: {X-Amzn-Trace-Id=Root=1-58422259-97da760e4d0f35d07106ebf9, Content-Type=application/json}\nSat Dec 03 01:39:37 UTC 2016 : Successfully completed execution\nSat Dec 03 01:39:37 UTC 2016 : Method completed with status: 200\n",
    "latency": 279,
    "headers": {
        "X-Amzn-Trace-Id": "Root=1-58422259-97da760e4d0f35d07106ebf9",
        "Content-Type": "application/json"
    }
}
```
