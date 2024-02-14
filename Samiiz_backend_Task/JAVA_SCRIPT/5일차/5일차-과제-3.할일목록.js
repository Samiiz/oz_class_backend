const todoList = document.getElementById('todo-list')
const todoForm = document.getElementById('todo-form')
let todoArr = []

loadTodos()

// 할일 저장 기능 만들기
function saveTodos(){
    const todoString = JSON.stringify(todoArr)
    localStorage.setItem("myTodos", todoString)
}


// 저장한 것 가져오기
function loadTodos(){
    const myTodos = localStorage.getItem("myTodos")
    if(myTodos !== null){
        todoArr = JSON.parse(myTodos)
        displayTodos()
    }
}

// 할일 삭제 기능 만들기
function handleTodoDelBtnClick(clickedId){
    todoArr = todoArr.filter(function(aTodo){
        return aTodo.todoId !== clickedId
    })
    displayTodos()
    saveTodos()
}


// 할일 수정 기능 만들기
function handleTodoItemClick(clickedId){
    todoArr = todoArr.map(function(aTodo){
        if(aTodo.todoId === clickedId){
            return {
                ...aTodo, todoDone: !aTodo.todoDone
            }
        }else{
            return aTodo
        }
    })
    displayTodos()
    saveTodos()
}


// 할일 보여주기
function displayTodos(){
    todoList.innerHTML = ""
    todoArr.forEach(function(aTodo){
        const todoItem = document.createElement("li")
        const todoDelBtn = document.createElement('span')
        todoDelBtn.textContent = "x"
        todoItem.textContent = aTodo.todoText
        todoItem.title = "클릭시 완료!!"
        if (aTodo.todoDone){
            todoItem.classList.add("done")    
        }else{
            todoItem.classList.add("yet")
        }
        todoDelBtn.title = "삭제"

        todoItem.addEventListener("click", function(){
            handleTodoItemClick(aTodo.todoId)
        })

        todoDelBtn.addEventListener("click", function(){
            handleTodoDelBtnClick(aTodo.todoId)
        })

        todoItem.appendChild(todoDelBtn)
        todoList.appendChild(todoItem)
    })
}


// 할일 추가하기
todoForm.addEventListener("submit", function(e){
    e.preventDefault()
    const toBeAdded = {
        todoText : todoForm.todo.value,
        todoId : new Date().getTime(),
        todoDone : false
    }
    todoForm.todo.value = ""
    todoArr.push(toBeAdded)
    displayTodos()
    saveTodos()
})