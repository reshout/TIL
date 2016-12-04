# AWS DynamoDB

## 시작 안내서

http://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/gettingstartedguide/Welcome.html

### DynamoDB 개념 소개

- 테이블 — 다른 DB와 마찬가지로 DynamoDB는 데이터를 테이블에 저장. 
- 항목 — 각 테이블은 여러 항목으로 구성. RDB의 Row와 유사. 테이블에 저장할 수 있는 항목의 수에는 제한이 없음.
- 속성 — 각 항목은 하나 이상의 속성으로 구성. 더이상 나뉠 수 없는 기본적 데이터 요소. RDB의 Column과 유사.
- 기본 키 — 각 항목을 나타내는 고유의 식별자. 테이블에 항목을 추가, 업데이트, 삭제할 때 기본 키 속성 값을 지정해야 함.
  - 파티션 키 — 내부 해시 함수에 대한 입력으로 사용. 이 해시 함수의 출력이 항목을 저장할 파티션을 결정
  - 파티션 키(해시 속성) 및 정렬 키(범위 속성) - 두 개의 속성으로 구성되는 복합 기본 키. 첫 번째 속성은 파티션 키. 두 번째 속성은 정렬 키. 파티션 키를 내부 해시 함수에 대한 입력으로 사용. 이 해시 함수의 출력이 항목을 저장할 파티션을 결정. **파티션 키가 동일한 모든 항목은 정렬 키 값을 기준으로 정렬되어 저장 함께 저장된다.** 두 항목이 동일한 파티션 키 값을 가질 수는 있지만 정렬 키 값은 서로 달라야 한다.
- 보조 인덱스 — 키가 아닌 속성을 사용하는 데이터를 읽고 싶다면 보조 인덱스를 사용할 수 있다.

### 자습서: 기본 DynamoDB 작업

http://docs.aws.amazon.com/ko_kr/amazondynamodb/latest/gettingstartedguide/GettingStarted.JsShell.html

- 기본적으로 PutItem은 무조건 overwrite 한다. 조건이 성립할 때만 overwrite하게 하려면 `ConditionExpression` 파라미터를 적용해야 한다.
- `ConditionExpression`으로 조건부 삭제할 수 있지만 키 값에 의해 선택된 하나의 항목에 대해 삭제 여부를 결정하기 위한 것이다.

## Note

- 파티션 키만 정의한 경우 특정 파티션 키 값을 가지는 항목은 하나만 존재할 수 있다.
- 정렬 키도 정의한 경우 정렬 키 값은 다르고 파티션 키 값은 다른 항목이 여러개 존재할 수 있다.
- 쿼리할 때 파티션 키, 정렬 키만 사용할 수 있다.
- 다른 키로도 쿼리하고 싶다면 보조 인덱스를 생성해야 한다.

## References

- [Developer Guide](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
  - [Working with Tables in DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithTables.html)
  - [Working with Items in DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.AtomicCounters)
  - [Query and Scan Operations in DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html)
  - [Improving Data Access with Secondary Indexes in DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html)
  - [Best Practices for DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html)

- [Performing Conditional Writes with Condition Expressions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html)
- [Reserved Words in DynamoDB](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html)

