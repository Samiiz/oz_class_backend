const div = document.getElementById("container")


for(let a = 1; a <= 5; a +=1){
    const box = document.createElement("div")
    console.log(box)
    box.style.color = "blue"
    box.style.width = "500px"
    box.style.height = "500px"
    box.style.backgroundColor = "black"
    box.style.fontSize = "50px"
    box.textContent = `헷갈리지만 신기하고 재밌다 ${a}번째`

    div.appendChild(box)
}