import React from "react";


const SearchBar = ({filter, value}) =>{

    return (
        <form >
            <label>Keywords:</label>
            <input value={value} type='text' placeholder='Enter your keywords' onChange={filter}/>
        </form>
    )

}

export default SearchBar;