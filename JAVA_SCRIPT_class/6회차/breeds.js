const apiRandomDogs = "https://dog.ceo/api/breeds/image/random/42";
const apiAllBreeds = "https://dog.ceo/api/breeds/list/all";
const request_Dogs = new XMLHttpRequest();
const request_Breeds = new XMLHttpRequest();

const header = document.getElementById("header");
const main = document.getElementById("main");
const input = document.getElementById("filter-text");
const button = document.getElementById("filter-button");
const select = document.getElementById("filter-select");
const more = document.getElementById("more");
const tothetop = document.getElementById("tothetop");
const reset = document.getElementById("reset");

const currentDogs = [];

function displayDogs(item) {
  const dogImgDiv = document.createElement("div");
  dogImgDiv.classList.add("flex-item");
  dogImgDiv.innerHTML = `
        <img src=${item}>
        `;
  main.appendChild(dogImgDiv);
}

window.addEventListener("load", function () {
  // 강아지 사진 뿌리기
  request_Dogs.open("get", apiRandomDogs);
  request_Dogs.addEventListener("load", function () {
    const response = JSON.parse(request_Dogs.response);
    response.message.forEach(function (item) {
      currentDogs.push(item);
      displayDogs(item);
    });
  });
  request_Dogs.send();

  // 셀렉트에 견종 정보 뿌리기
  request_Breeds.open("get", apiAllBreeds);
  request_Breeds.addEventListener("load", function () {
    const response = JSON.parse(request_Breeds.response);
    Object.keys(response.message).forEach(function (item) {
      const option = document.createElement("option");
      option.textContent = item;
      option.value = item;
      select.appendChild(option);
    });
  });
  request_Breeds.send();
});

// input에 값을 넣고 필터링 버튼 눌렀을때 해당 값을 가진 이미지만 노출하기
button.addEventListener("click", function () {
  main.innerHTML = "";
  let filteredDogs = currentDogs.filter(function (item) {
    return item.indexOf(input.value) !== -1;
  });

  input.value = "";

  filteredDogs.forEach(function (item) {
    displayDogs(item);
  });
});

// select list에 있는 value중 하나를 선택시 해당 값을 가진 이미지만 노출하기
select.addEventListener("change", function () {
  main.innerHTML = "";
  let filteredDogs = currentDogs.filter(function (item) {
    return item.indexOf(select.value) !== -1;
  });

  filteredDogs.forEach(function (item) {
    displayDogs(item);
  });
});
// MORE 버튼 기능 만들기
more.addEventListener("click", function () {
  const response = JSON.parse(request_Dogs.response);
  response.message.forEach(function (item) {
    currentDogs.push(item);
    displayDogs(item);
  });
});

// TOP 버튼 기능 만들기
tothetop.addEventListener("click", function () {
  // scrollTo : 주어진 위치로 스크롤을 이동한다.
  window.scrollTo({ top: 0 });
});

// Reset 버튼 기능만들기
reset.addEventListener("click", function (e) {
  e.preventDefault();
  main.innerHTML = "";
  request_Dogs.open("get", apiRandomDogs);
  request_Dogs.addEventListener("load", function () {
    const response = JSON.parse(request_Dogs.response);
    response.message.forEach(function (item) {
      if (!currentDogs.includes(item)) {
        currentDogs.push(item);
        displayDogs(item);
      }
    });
  });
  request_Dogs.send();
});
