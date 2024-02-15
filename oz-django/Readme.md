# 구현기능

- 최신업데이트 2 / 16
<br/>[Boards](#boards), [Users](#customusers)

## Feeds

1. /feeds 로 들어갈시 "show feed" 출력  
<br/><img src=contents/:feed.png>

2. /feeds/all 로 들어갈시 "all feed" 출력  
<br/><img src=contents/:feeds:all.png>

3. /feeds/(int)student_id/(str)content 로 들어갈 시  
아래 화면처럼 출력  
<br/><img src=contents/:feeds:id:content.png>

## Questions

1. /questions 로 들어 갈시  
아래 화면 처럼 출력  
<br/><img src=contents/:questions.png>

2. /questions/(str)student_id/(int)questionNum 로 들어갈시  
아래 화면처럼 출력  
<br/><img src=contents/:questions:id:num.gif>

## Boards

- boards 테이블을 생성  
<br/><img src=contents/:Boards.png>

## CustomUsers

1. admin의 User를 상속받아 CustomUsers테이블을 생성  
<br/><img src=contents/:Users.png>

2. CustomUsers의 fieldset 내용중 Permissions의 내용을  
`'classes': ('collapse')` 를 사용하여 긴내용을 필요할때만 보도록 수정  
<br/><img src=contents/:Users_detail.gif>

## Common

- Common app 생성으로 django 기본기능인 models의 Model과 함께  
`created_at` `updated_at` 모델을 사용 할 수 있게 함  
<br/><img src=contents/:Common.png>

# you need more

send me Discord DM