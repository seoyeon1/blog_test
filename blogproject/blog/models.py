from django.db import models
#models.py : class를 사용해 어떤 data를 처리할지 알려줌.


# Create your models here.
class Blog(models.Model):#blog Class에서 어떤 data를 처리할지 정의.
    title = models.CharField(max_length=200)#title은 models의 charfield를 이용해 가져와 사용, 최대길이 지정.
    pub_date = models.DateTimeField('date published')#pub_date는 날짜, 시간알아내는 변수 이용해 날짜,시간 가져옴.
    body = models.TextField()#body:긴 글 형식을 저장하기 위해 textfield를 사용.


    #블로그에서 title이 바로 보이게 함.
    def __str__(self):#(객체 자기자신을 인자로 받아)문자열화 해주는 함수 선언.
        return self.title#자기 자신의 title변수를 문자열화하여 리턴


    #Blog class속 body에 담긴 글자를 100개 까지만 보이게 해줌.
    def summary(self):
        return self.body[:100]