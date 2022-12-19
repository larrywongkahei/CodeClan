import {useState} from 'react';
import './App.css';


function App() {

  const [name, setName] = useState('');

  const [radiobutton, setButton] = useState('');

  const [items, setItem] = useState([
    {name : "Buy shopping", priority : "high"},
    {name : "Clean Bathroom", priority : "low"},
    {name : "Car's MOT", priority : "high"}
  ]);

  const items_list = items.map((item, index) => 
    <li key={index} id={item.priority === 'high' ? "high" : "low"}>{item.name}</li>)

  const getText = (event) => {
    setName(event.target.value)
  }

  const getResult = (event) => {
    setButton(event.target.value)
  }

  const saveItem = (event) => {
    event.preventDefault()
    const new_item = {
      name : name,
      priority : radiobutton,
    }
    const new_items = [...items]
    new_items.push(new_item)
    setItem(new_items)
    setButton('')
    setName('')
  }

  return (

    <div>
      <h1>ToDo's</h1>
      <form onSubmit={saveItem}>
        <span>
          <input type='text' value={name} onChange={getText} />
          <label>High</label>
          <input type='radio' value='high' onClick={getResult} checked={radiobutton === 'high'}></input>
          <label>Low</label>
          <input type='radio' value='low' onClick={getResult} checked={radiobutton === 'low'}></input>
          <button>Save Item</button>
        </span>
      </form>
      <ul>
        {items_list}
      </ul>
    </div>
  );
}

export default App;
