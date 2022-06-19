# DRF_study
DRF관련 리포

## 1주차 과제
#### 1. args, kwargs를 사용하는 예제 코드 짜보기
![image](https://user-images.githubusercontent.com/101394490/173819607-3dc48030-72cd-4edb-8292-51620eafca46.png)


#### 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
#####  - mutable은 가변적이다.
mutable은 주소를 가르켜준다.

x = [1,2]
y = x
y.append[3]
print(x) >>> [1,2,3]

이 나오게된다. 이유는 y=x를 해 주었을 떄 x의 값이 아닌 x의 주소를 명시 해 주었기 때문이다.
이렇듯 mutable은 주소를 가르켜서 값을 가져오기에 가변적이다.

#####  - immutable은 불변적이다.
mutable과는 다르게 코드에 대입하여 보면

x = [1,2]
y = x
y.append[3]
print(x) >>> [1,2]

이렇게 나온다. 이유는 y = x를 해 주었을 때 imutable은 주소가 아닌 그 값 자체를 명시하기 떄문이다.
이렇듯 imutable은 값을 가르키기에 불변적이라고 할 수 있다.

#### 3. DB Field에서 사용되는 Key 종류와 특징 서술하기

##### AutoField
ID(pk)로 사용 가능한 자동으로 증가하는 IntegerField다. 직접 사용할 필요는 없다. 모델의 기본키 필드는 별도로 지정하지 않으면 자동으로 추가됨.

##### BigAutoField
AutoField와 매우 유사한 64비트 정수다.

##### BigIntergerField
IntegerField와 매우 유사한 64비트 정수다.

##### BinaryField
raw binary 데이터를 저장하기 위한 필드이다. 바이트 할당만을 지원한다. 이 필드는 기능이 제한적이다. Binary값에 쿼리셋을 필터링할 수 없다. ModelForm에 BinaryField를 포함시킬 수 없다.

##### BooleanField
논리 필드이다. true, false필드이고, 기본 폼 위젯은 CheckboxInput 이다. null 값 허용이 필요하면 NullBooleanField를 사용하자. Field.default가 정의되지 않았을 때, BooleanField의 기본 값은 None 이다. default None을 사용하고 해당 필드에 값을 넣지 않을 경우, migrate 시 에러가 발생하지 않고 실제 모델이 저장될때 DBMS에서 제약조건 에러가 난다.

##### CharField
작은 문자열에서 큰 사이즈의 문자열을 위한 필드이다. 많은 양의 경우 TextField를 사용한다. 기본 위젯은 TextInput이고, CharField는 필수 인수가 추가로 하나 있다.
CharField.max_length : 필드의 최대길이 (문자 수)이다.

##### DateField
파이썬의 datetime.date 인스턴스에 의해 표현되는 날짜다.

#### 4. django에서 queryset과 object는 어떻게 다른지 서술하기
##### queryset은 Database에서 전달받은 object들의 모음(list)이다. DB(SQL)에서는 row에 해당한다.
데이터베이스로부터 데이터를 읽고 필터를 걸거나 정렬 등을 할 수 있다. 
리스트와 구조는 같지만 파이썬 기본 자료구조가 아니기에 읽고 쓰기 위해서는 자료형 변환을 해줘야한다. 
.all()
테이블 데이터를 전부 갖고온다. 즉, 해당 쿼리셋의 모든 요소를 반환한다. 현재 쿼리셋의 복사본을 반환한다고 볼 수 있다.

.values()
쿼리셋의 내용을 딕셔너리로 각 객체정보를 갖는 리스트 형태로 반환한다.

.filter()
특정 조건에 맞는 Row들을 갖고오기 위해서 사용되는 메소드이다.

.exclude()
특정 조건을 제외한 나머지 Row들을 갖고오기 위해서 사용되는 메소드이다.
지정된 parameter(매개변수)와 일치하지 않는 객체를 포함한 QuerySet을 반환한다. filter()와 반대로 동작한다.

.get()
하나의 Row만 갖고오기 위해서 사용되는 메소드이다.
특정 column 조건에 해당하는 결과를 객체로 반환하는 함수이다. 즉, .get()은 쿼리셋을 호출하는 것이 아니라서 뒤에 다른 메소드를 추가할 수 없다.
