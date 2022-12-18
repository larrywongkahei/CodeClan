document.addEventListener('DOMContentLoaded', () => {
  console.log('JavaScript loaded');
  const save = document.querySelector('#new-item-form');
  save.addEventListener('submit', handle_form);
  const delete_button = document.createElement('button');
  delete_button.textContent = "Delete All"
  body = document.querySelector('body');
  body.appendChild(delete_button);
  delete_button.addEventListener('click', handle_delete)
})
const handle_form = function(event){
  event.preventDefault();
  const form_title = document.querySelector('#title');
  const form_category = document.querySelector('#category');
  const form_author = document.querySelector('#author');
  const div = document.createElement('div');
  const form_data = [form_title, form_author, form_category]
  form_data.forEach((data) => {
    const p = document.createElement('p');
    p.textContent = data.value;
    div.appendChild(p)
    console.log(`done logging${data.value}`)
  })
  console.log('Loaded')
  const reading_list = document.querySelector('#reading-list');
  reading_list.appendChild(div)
  document.querySelector('#new-item-form').reset();
}

const handle_delete = function(event){
  event.preventDefault();
  document.querySelector('#reading-list').textContent = '';
  console.log('deleted everything')
}