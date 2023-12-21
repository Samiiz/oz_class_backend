const nameElement = document.querySelector("#name")
let name = prompt("당신의 이름은?")
nameElement.textContent = `내 이름은 ${name}이에요`

const hobbyElement =  document.querySelector("#hobby")
let hobby = prompt("당신의 취미는?")
hobbyElement.textContent = `나는 ${hobby}하는것을 좋아해요`

document.querySelector("#song")
.textContent = `내 최애곡은 ${prompt("당신의 최애곡은?")}이에요`