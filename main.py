#하나 출력하기
print(10), print("안녕"), print('안녕'), print("#안녕")

#여러개 출력하기
print(10, 20)

#줄바꿈하기
print()

#파일로 만들어서 프로그램을 작성하는게 일반적이고 파일로 작성할땐 print 함수써야
#출력이 되기때문에 출력할때는 반드시 print함수 사용

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ######

#6강 자료형=자료의형식. 생각할수있는 모든것들이 자료고 자료를 의미있게정리하면 정보.
#기본자료형-매우쉽게 분류해서 사용할수있는 작고 가벼운것들.
##대표적 기본자료형3개는
#문자열 - 글자를 나타낼때사용하는 자료형. str(String)
"안녕하세요"
#숫자-10은정수, 10.0은 부동소수점. int(Integer), float(Floating Point)
10
#불-참과 거짓을 표현하기위한 자료형. bool(Boolean)    ex) treu false
#복합자료형 = 기본자료형이 복합적으로 섞여있는것
#자료형 확인할땐 type 함수 사용. 함수안의 함수는 안쪽부터 실행. 즉 type부터실행.
print(type("안녕하세요"))