let htmlTextarea = document.querySelector(".html .text");
let cssTextarea = document.querySelector(".css .text");
let jsTextarea = document.querySelector(".js .text");

let iframe = document.querySelector(".preview");

function render() {
  const html = htmlTextarea.value;
  const css = cssTextarea.value;
  const js = jsTextarea.value;

  iframe.contentDocument.body.innerHTML = html;

  const style = iframe.contentDocument.createElement("style");
  style.textContent = css;

  iframe.contentDocument.head.appendChild(style);
  const script = iframe.contentDocument.createElement("script");
  script.textContent = js;
  iframe.contentDocument.head.appendChild(script);
}

htmlTextarea.addEventListener("input", render);
cssTextarea.addEventListener("input", render);
jsTextarea.addEventListener("input", render);
