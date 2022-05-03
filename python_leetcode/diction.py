# 궁금증
# 딕셔너리에 key값과 value값을 넣으면 딕셔너리에 들어간다
# 딕셔너리이름[key] = value 로 적었을 때 key가 없다면 key value가 생성된다

# key 값으로 정수가 들어갈 수 있는데
# key 값인지 index 값인지 구분할 수 있을까?
# 결론 : 딕셔너리이름[key] 로만 찾고 index와는 관계가 없다

dic={}
dic[1]=2
print(dic)
dic["1"]=4
dic[2]=6
print(dic[1])
# index 라면 4를 출력해야 하지만! 실제로는 2를 출력
# 즉 [] 안에는 무조건 key로 인식한다
print(dic[0])
# 즉 dic[0]을 할 경우 인덱스가 아닌 key값 0으로 인식하기에 에러가 나온다