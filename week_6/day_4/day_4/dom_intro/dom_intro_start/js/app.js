console.log('app loaded', window);

document.addEventListener('DOMContentLoaded', () => {
    const fruits = ["apple", "orange", "banana"];
	console.table(fruits);

	const person = {
		name: "Jane",
		age: 40
	};
	console.table(person);
    const title = document.querySelector('h1');
    title.textContent = "Javascript says, BOO";
    console.log('BOOO!')
    const button = document.querySelector('#button'); // MODIFIED
    button.addEventListener('click', handleButtonClick); // NEW
    const textInput = document.querySelector('#input'); // NEW
    textInput.addEventListener('input', handleInput); // NEW
    const select = document.querySelector('#select');
    select.addEventListener('input', handleSelect);
    const form = document.querySelector('#form');
    form.addEventListener('submit', handle_form)
  });
const handleButtonClick = function () {
    const resultParagraph = document.querySelector('#button-result'); // NEW
    resultParagraph.textContent = 'That button has definitely been clicked.';
    const result = document.querySelector('#input-result');
    result.textContent = 'You have type'; // NEW
};

const handleInput = function (event) {
    console.log(event);
}

const handleSelect = function(event){
    console.log('You went with ', event.target.value)
}

const handle_form = function(event){
    event.preventDefault()
    const form_data = document.querySelector('#form-result');
    form_data.textContent = `Your name :${event.target.first_name.value} ${event.target.last_name.value}`;
}

// const handle_form = function (event) {
//     event.preventDefault();
//     const resultParagraph = document.querySelector('#form-result');
//     resultParagraph.textContent = `
//       Your name:
//       ${event.target.first_name.value}
//       ${event.target.last_name.value}
//     `
//   };
