const perm_duration_day = document.querySelectorAll("#perm-duration-day");

perm_duration_day.forEach((element) => {
  const content = element.textContent;
  const [hours, minutes] = content.split(":").map(Number);

  if (hours >= 2) {
    element.style.backgroundColor = "#E50000";
  }
});
