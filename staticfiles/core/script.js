const panels = document.querySelectorAll(".panel");
let activePanel = null;


function setActive(panel) {
  panels.forEach((p) => p.classList.remove("active"));
  panel.classList.add("active");
  activePanel = panel;
}


panels.forEach((panel) => {
  panel.addEventListener("mouseenter", () => setActive(panel));
});


window.addEventListener("load", () => {
  setActive(document.querySelector(".panel.ccenter"));


  document.addEventListener(
    "mousemove",
    (e) => {
      const hovered = Array.from(panels).find((panel) => {
        const rect = panel.getBoundingClientRect();
        return (
          e.clientX >= rect.left &&
          e.clientX <= rect.right &&
          e.clientY >= rect.top &&
          e.clientY <= rect.bottom
        );
      });
      if (hovered && hovered !== activePanel) {
        setActive(hovered);
      }
    },
    { once: true } 
  );
});
