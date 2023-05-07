function copyToClipboard(elementId) {
  const element = document.getElementById(elementId);
  if (!element) {
    console.error(`No se encontró ningún elemento con el id ${elementId}`);
    return;
  }
  const textToCopy = element.value;
  navigator.clipboard.writeText(textToCopy).then(
    function () {
      console.log("Texto copiado correctamente.");
    },
    function () {
      console.error("No se pudo copiar el texto.");
    }
  );
}

function copyToClipboardP(elementId) {
  const element = document.getElementById(elementId);
  if (!element) {
    console.error(`No se encontró ningún elemento con el id ${elementId}`);
    return;
  }
  const textToCopy = element.innerText;
  navigator.clipboard.writeText(textToCopy).then(
    function () {
      console.log("Texto copiado correctamente.");
    },
    function () {
      console.error("No se pudo copiar el texto.");
    }
  );
}
