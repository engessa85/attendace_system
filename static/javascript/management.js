const wrapper = document.querySelector(".wrapper");
const model = document.querySelector(".model");
const look_button = document.querySelectorAll(".look");
const model_close = document.querySelectorAll(".model-close");

const leave_time_1 = document.querySelector(".leave-time-1")
const enter_time_1 = document.querySelector(".enter-time-1")

const leave_time_2 = document.querySelector(".leave-time-2")
const enter_time_2 = document.querySelector(".enter-time-2")


const leave_time_3 = document.querySelector(".leave-time-3")
const enter_time_3 = document.querySelector(".enter-time-3")



const fetchingData = async (employeeId) => {

  const url = `https://yehia85.pythonanywhere.com/managment/get-permissions/${employeeId}`;
  response = await fetch(url);
  let data = response.json();
  return data;
};

const open_model = async (event) => {
  wrapper.classList.add("opacity");
  model.style.display = "flex";
  const employee_id = event.target.getAttribute("employeeID");
  const res = await fetchingData(employee_id);
  console.log(res.data);
  const data = res.data
  leave_time_1.textContent = data.permission_leaving_time
  enter_time_1.textContent = data.permission_entering_time

  leave_time_2.textContent = data.permission_leaving_time_2
  enter_time_2.textContent = data.permission_entering_time_2

  leave_time_3.textContent = data.permission_leaving_time_3
  enter_time_3.textContent = data.permission_entering_time_3

};

const close_model = () => {
  wrapper.classList.remove("opacity");
  model.style.display = "none";
};

look_button.forEach((element) => {
  element.addEventListener("click", open_model);
});

model_close.forEach((element) => {
  element.addEventListener("click", close_model);
});
