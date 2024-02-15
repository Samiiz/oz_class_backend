from django.db import models

# Create your models here.
class CommonModel(models.Model):

    # auto_now_add : 현재 데이터 생성 시간기준으로 생성 -> 데이터 업데이트시에도 최초 생성시간으로 고정
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now : 현재 데이터 생성 시간기준으로 생성 -> 데이터 업데이트시 수정된 시간기준으로 업데이트
    updated_at = models.DateTimeField(auto_now=True)

    # 데이터베이스의 테이블에 위와 같은 컬럼이 추가되지 않게하는 옵션
    class Meta:  # Meta : 내부 클래스 / Django모델의 동작방식을 사용자정의하는데 사용
        abstract = True