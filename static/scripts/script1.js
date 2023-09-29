const getNav = document.querySelectorAll(".navLink");
const sections = document.querySelectorAll("main section");

const navLinks = Array.from(getNav);

let Activelink;

let cordsSection = [];
function getPos() {
  sections.forEach((section) =>
    cordsSection.push({
      page: section.textContent,
      link: `#${section.id}`,
      positionTop: Math.floor(section.offsetTop),
      positionBottom: section.offsetHeight + section.offsetTop,
      height: Math.floor(section.offsetHeight)
    })
  );
}

window.onload = () => getPos();

window.addEventListener(
  "scroll",
  function () {
    var top = this.scrollY;
    document.querySelector("header").className = top > 0 ? "scrolled" : "";
    const active = cordsSection.find(
      (section) =>
        top >= section.positionTop - 90 && top <= section.positionBottom
    );
    navLinks.forEach((link) => link.classList.remove("active"));
    try {
      const link = navLinks.find(
        (link) => link.getAttribute("href") === active.link
      );
      link.classList.add("active");
    } catch (e) {}
  },
  false
);