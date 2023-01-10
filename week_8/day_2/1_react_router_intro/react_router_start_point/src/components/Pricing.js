import React from "react";

const Pricing = ({prices}) => {
  const pricesItems = prices.map((price, index)=>{
    return <li key={index}>{price.level}: £{price.cost}</li>
  });

  return(
    <div>
      <h4>{pricesItems}</h4>
    </div>
  )

};

export default Pricing;
