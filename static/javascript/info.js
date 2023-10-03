const perm_duration_day = document.querySelectorAll("#perm-duration-day");

perm_duration_day.forEach((element) => {
  const content = element.textContent;
  const [hours, minutes] = content.split(":").map(Number);

  if (hours >= 2) {
    element.style.backgroundColor = "#E50000";
  }
});

const generatePDF = () => {
  const pdfOptions = {
    margin: 10,
    filename: 'my_document.pdf',
    image: { type: 'jpeg', quality: 0.98 },
    html2canvas: { scale: 2 },
    jsPDF: { unit: 'mm', format: 'a3', orientation: 'landscape' }
};
  const wrapper = document.querySelector(".wrapper");
  html2pdf().from(wrapper).set(pdfOptions).save();
};

const handelPDF = () => {
  console.log("pdf generator");
  generatePDF()
};

const pdf_buttton = document.querySelector("#pdf-buttton");
pdf_buttton.addEventListener("click", handelPDF);
