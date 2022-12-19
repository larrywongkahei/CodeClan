const names = ["Fred", "Kate", "Cindy", "Ricky", "Keith"];
console.log(names);



const [fred, kate, ..._] = names;
console.log(_);