# Our mood diary 
<i>나만의 일기장과 Todolist를 작성할 수 있는 웹사이트</i> <br><br>
제가 만들고자 하는 웹사이트는 자신의 하루일상을 기록 할 수 있으며 , Todolist도 작성 할 수 있습니다. <br>
일기장에는 태그 기능을 추가하여 기분에 맞는 태그를 선택하여 글을 작성 할 수 있습니다. #기쁨 , #슬픔 ,#우울 ,, 등등 <br>
Todolist는 자신이 하고자 하는 일을 작성 할 수 있습니다. 완료한 일은 지울 수 있습니다. 완료하지 못한 일은 다음날로 미뤄집니다. 

<h3>Our mood diary flow chart</h3> 

![image](https://user-images.githubusercontent.com/82064490/172675100-61f54855-7768-4d5b-bcea-a07c75fa4395.png)


<h3>URL 패턴 설계</h3>


|  페이지  	|  URL   	|
|---	|---	|
|  메인페이지     	|  도메인   	|
|  일기장 페이지-목록  	|  도메인/diary/  	|
|  일기장 페이지-상세  	| 도메인/diary/포스트 pk   	|
|   투두리스트 페이지 - 목록	|  도메인/todolist/   	|
|  투두리스트 페이지 - 상세 	|   도메인/todolist/포스트 pk	|
  

