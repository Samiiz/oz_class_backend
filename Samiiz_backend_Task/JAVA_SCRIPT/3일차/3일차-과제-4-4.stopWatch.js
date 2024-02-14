const time = document.getElementsByClassName("stopWatch")[0];
let s = 0;
let m = 0;
let h = 0;
let m_count = 0;
let h_count = 0;

let timer;

function Start() {
  Timer();
  timer = setTimeout(Start, 1000);
}

function Stop() {
  clearTimeout(timer);
}

function Clear() {
  s = 0;
  m = 0;
  h = 0;
  m_count = 0;
  h_count = 0;
  time.innerHTML = "00:00:00";
  clearTimeout(timer);
}

function Timer() {
  s++;

  if (s >= 60) {
    s = 0;
    m_count = 0;
    m++;
  }

  if (m >= 60) {
    m = 0;
    h_count = 0;
    h++;
  }

  if (s < 10) {
    s = "0" + s;
  }

  if (m < 10) {
    if (m_count == 0) {
      m = "0" + m;
      m_count = 1;
    }
  }

  if (h < 10) {
    if (h_count == 0) {
      h = "0" + h;
      h_count = 1;
    }
  }

  time.innerHTML = h + ":" + m + ":" + s;
}
