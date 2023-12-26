alert("지금부터 자기소개를 해봐요")

document.querySelector("#name")
.textContent = `내 이름은 ${prompt("당신의 이름은?")}이에요`

document.querySelector("#from")
.textContent = `나는 ${prompt("당신이 사는 지역은?")}에 사는 ${prompt("당신의 성별은?")}에요`

document.querySelector("#hobby")
.textContent = `나는 ${prompt("당신의 취미는?")}하는것을 좋아해요`

document.querySelector("#song")
.textContent = `내 최애곡은 ${prompt("당신의 최애곡은?")}이에요`