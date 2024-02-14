const todaySpan = document.querySelector("#today");
const numbersDiv = document.querySelector(".numbers");
const drawButton = document.querySelector("#draw");
const resetButton = document.querySelector("#reset");
const colors = ["orange", "skyblue", "red", "purple", "green"];

const today = new Date();
let year = today.getFullYear();
let month = today.getMonth() + 1;
let date = today.getDate();
todaySpan.textContent = `${year}년 ${month}월 ${date}일`;

let lottoNumbers = [];

function paintNumber(number) {
  const eachNumDiv = document.createElement("div");
  eachNumDiv.classList.add("eachnum");
  let colorIndex = Math.floor(number / 10);
  eachNumDiv.style.backgroundColor = colors[colorIndex];
  eachNumDiv.textContent = number;
  numbersDiv.appendChild(eachNumDiv);
}

drawButton.addEventListener("click", function () {
  if (lottoNumbers.length < 6) {
    while (lottoNumbers.length < 6) {
      let rn = Math.floor(Math.random() * 45) + 1;

      if (lottoNumbers.indexOf(rn) === -1) {
        lottoNumbers.push(rn);
        paintNumber(rn);
      }
    }
  } else {
    lottoNumbers.splice(0, 6);
    numbersDiv.innerHTML = "";

    while (lottoNumbers.length < 6) {
      let rn = Math.floor(Math.random() * 45) + 1;

      if (lottoNumbers.indexOf(rn) === -1) {
        lottoNumbers.push(rn);
        paintNumber(rn);
      }
    }
  }
});

resetButton.addEventListener("click", function () {
  lottoNumbers.splice(0, 6);
  numbersDiv.innerHTML = "";
});
