# AWS Lambda

![](https://d0.awsstatic.com/Test%20Images/MasonTests/Lambda_HowItWorks.png)

## Advantages

- 서버 관리 불필요 (보안 패치, ...)
- 코드가 실행된 시간과 트리거된 회수를 기준으로 비용 부과
- 높은 가용성 제공 (확장, ...)

## Disadvantages

- 컨테이너 초기화로 latency 발생할 수 있음
- 실행 환경을 유연하게 변경할 수 없음

## Triggers

- Changes to data in an Amazon S3 bucket or an Amazon DynamoDB table
- In response to HTTP requests using Amazon API Gateway
- API calls made using AWS SDKs

## How It Works

http://docs.aws.amazon.com/ko_kr/lambda/latest/dg/lambda-introduction.html

- 개발자가 Lambda를 생성할 때 메모리 크기, 최대 실행시간 등을 설정
- AWS Lambda는 사용자의 설정을 참고하여 컨테이너를 실행
- AWS Lambda가 컨테이너의 creation 및 deletion 담당. 개발자가 이를 관리할 수 있는 API 제공하지 않음.
- 컨테이너를 로딩하는데 시간이 걸리므로 처음 실행하거나 코드가 변경되었을 때 latency가 발생
- 다음 Lambda 실행을 대비해 일정시간 컨테이너를 유지함(frozen)

### Considerations for Container Reuse

- DB connection 등 Lambda를 처음 실행했을 때 정의한 것들이 남아 있을 수 있어 이를 활용한 최적화를 고려해볼 수 있다.
- /tmp 디렉토리에 저장한 내용이 남아 있을 수 있으므로 이를 활용한 최적화를 고려해볼 수 있다.
- 백그라운드 프로세스 및 콜백이 다시 시작될 수 있기 때문에 Lambda가 끝나기 전에 이들이 확실히 끝나도록 구현해야 한다.

## Lambda Functions

https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/lambda-introduction-function.html

### Compute Requirements – Lambda Function Configuration

- **Compute Resources** – 메모리 크기만 설정할 수 있으며, CPU power는 메모리 크기에 비례한다.
- **Maximum execution time** – Lambda function이 영원히 실행되지 않도록 timeout 설정해야 한다. Timeout이 끝나면 실행중인 람다 함수가 중지된다.
- **IAM role**
- **Handler name** – AWS Lambda가 실행될 때 호출될 메서드 이름. event 정보와 parameter가 전달 된다.

### Invocation Types

- 2 invocation types – Synchronous(`RequestResponse`) vs Asynchronous(`Event`)
- Application에서 호출하거나 테스트 목적으로 CLI에서 호출할 때, invocation type을 지정할 수 있다.
- AWS Service에 의해서 호출될 때, 서비스에 따라 invocation type은 정해져 있고 개발자가 변경할 수 없다.
  - S3는 언제나 람다를 비동기로 호출
  - Cognito는 언제나 람다를 동기로 호출

### Building Lambda Functions

https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/lambda-app.html

람다 기반 애플리케이션의 라이프사이클

1. Authoring code for your Lambda function
1. Uploading code and creating Lambda functions
1. Monitoring and troubleshooting

#### Authoring Code for Your Lambda Function

- 지원 언어는 [Lambda Execution Environment and Available Libraries](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/current-supported-versions.html)를 참고
- AWS Lambda console, Eclipse, Visual Studio 등 다양한 도구를 사용할 수 있지만 사용할 프로그래밍 언어와 라이브러리에 따라 다를 수 있다.
  - Python을 사용하는 경우, 컴파일이 필요 없고 외부 라이브러리를 사용하지 않으며 소스코드가 하나의 파일로 구성된 경우에만 AWS Lambda console에서 코드를 작성할
    수 있다.
  - Node.js의 경우 Visual Studio를, Java의 경우 Eclipse를 사용할 수 있다.
- 언어와 상관없는 공통적인 패턴
  - How you write the handler method of your Lambda function?
  - How you pass events to the handler?
  - What statements you can use in your code to generate logs in CloudWatch Logs?
  - How to interact with AWS Lambda runtime and obtain information such as the time remaining before timeout?
  - How to handle exceptions?
- 언어마다 다른 내용은 [Programming Model](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/programming-model-v2.html) 참조

#### Deploying Code and Creating a Lambda Function

1. Creating a Deployment Package – Organizing Code and Dependencies
  - 언어마다 deployment package 생성 방법이 다르다.
  - Python, Node.js의 경우 Jenkins 플러그인 사용 가능
  - Java의 경우 Maven 플러그인 사용 가능
  - 자세한 내용은 [Creating a Deployment Package](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/deployment-package-v2.html) 참조
  - Console을 이용한 경우 deployment package를 생성하고 업로드까지 해준다.
1. Uploading a Deployment Package – Creating a Lambda Function
  - [CreateFunction](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/API_CreateFunction.html)으로 람다 함수 생성
  - AWS Lambda console, AWS CLI, AWS SDKs 모두 내부적으로 `CreateFunction`을 사용
  - 람다를 생성할 때 deployment package와 configuration information을 제공
1. Testing a Lambda Function
  - Sample event data를 사용해 람다 함수 테스트 가능
  - Console을 이용하거나 CLI에서 `Invoke` 메서드 호출

#### Monitoring and Troubleshooting

- Amazon CloudWatch에 의해 자동으로 모니터링(metric 제공) 되며, 로그가 기록됨

## Programming Model

https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/programming-model-v2.html

- **Handler** – 람다 함수 생성할 때 지정하는 시작 함수를 의미. `파일명.함수명`. Event data가 첫 번째 파라미터로 전달된다.
- **Context** – 두 번째 파라미터로 전달되는 context object를 통해 람다 실행 환경과 커뮤니케이션 가능. Timeout을 읽을 수 있다. Node.js의 경우 람다의 끝을 알리는
  callback을 세 번째 파라미터로 받는다.
- **Logging** – 언어마다 다른 statement를 통해 로그를 남기면 CloudWatch에 기록된다.
- **Exception** – 람다 함수는 결과를 AWS Lambda에 반환해야 한다. 요청에 대한 처리를 성공적으로 끝내거나 에러를 통지하는 다양한 방법이 있다. 동기로 호출한 경우
  AWS Lambda는 결과를 client에게 전달한다.

### Note

### Programming Model for Authoring Lambda Functions in Python

https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/python-programming-model.html

## Use Cases

## Questions

- 람다 실행 중 Configuration을 변경할 수 있는 API 존재하나?
- Timeout 전에 람다 실행 끝나도 비용은 청구되고 컨테이너는 활성화 되어 있나?
- IAM role의 의미와 역할은?

## References

1. [AWS Lambda](https://aws.amazon.com/ko/lambda/)
1. [시작 안내서](http://docs.aws.amazon.com/ko_kr/lambda/latest/dg/welcome.html)
1. [Lambda Execution Environment and Available Libraries](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/current-supported-versions.html)
1. [Programming Model](https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/programming-model-v2.html)
1. Realtime File Processing
  - [Diagram](https://s3.amazonaws.com/awslambda-reference-architectures/file-processing/lambda-refarch-fileprocessing.pdf)
  - [Sample Code](https://github.com/awslabs/lambda-refarch-fileprocessing)
1. Realtime Stream Processing
  - [Diagram](https://s3.amazonaws.com/awslambda-reference-architectures/stream-processing/lambda-refarch-streamprocessing.pdf)
  - [Sample Code](https://github.com/awslabs/lambda-refarch-streamprocessing)
