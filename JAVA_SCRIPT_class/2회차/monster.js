let monsterHP = 100
const container = document.getElementById("container")
const h1 = document.createElement("h1")
h1.textContent = "몬스터 잡기 게임을 시작합니다!!"
container.appendChild(h1)

let attackDamge = parseInt(prompt("1회 공격시 데미지는? (양의 정수)"))
let attackCount = 0

if(attackDamge > 0){
    while(monsterHP > 0){
        monsterHP -= attackDamge
        attackCount += 1

        const p = document.createElement("p")
        p.textContent = `몬스터를 ${attackCount}회 공격했다!`
        container.append(p)
        
        const strong = document.createElement("strong")
        strong.textContent = `몬스터의 남은 HP는 ${monsterHP}입니다!`
        container.append(strong)
    }
    
    const h2 = document.createElement("h2")
    h2.textContent = `수고하셨습니다! ${attackCount}의 공격을 끝으로 몬스터를 잡았습니다!`
    h2.style.color = "orange"
    h2.title = `게임을 다시 시작하고 싶으면 새로고침 하세요!`
    container.appendChild(h2)

}else{
    alert("데미지를 잘못 입력하여 게임을 취소합니다")
}