import './App.css';
import React, {useState} from 'react';

function App() {

  const [items, setItems] = useState([
    {name : "Bread", isPurchased : false},
    {name : "Cheese", isPurchased : true}, 
    {name : "Bow and Arrow", isPurchased : false},
  ])

  const [newItem, setNewItem] = useState("")

  const saveNewItem = (event) => {
    event.preventDefault()
    const copyItems = [...items]
    copyItems.push({name: newItem, isPurchased: false})
    setItems(copyItems)
    setNewItem("")
  }

  const handleInput = (event) => {
    setNewItem(event.target.value)

  }

  const purchaseItem = (index) => {
    const copyItems = [...items]
    const updatedItem = {...copyItems[index]}
    updatedItem.isPurchased = true
    copyItems[index] = updatedItem
    setItems(copyItems)
  }

  const itemNodes = items.map((item, index) =>
    <li key={index} className={item.isPurchased ? "purchased" : "not-purchased"}>
      <span>{item.name}</span>
      {item.isPurchased ? <span className="purchased">Purchased!</span> : <button onClick={() => purchaseItem(index)}>Purchase</button>}
    </li>
)
  


  return (
    <div className="App">

      <h1>Shopping List</h1>
      <hr></hr>

      <ul>
        {itemNodes}
      </ul>

      <form onSubmit={saveNewItem}>
        <label htmlFor="new-item">Add a new item:</label>
        <input id="new-item" type="text" value={newItem} onChange={handleInput}/>
        <input type="submit" value="Save new item"/>
      </form>

    </div>
  );
}

export default App;
