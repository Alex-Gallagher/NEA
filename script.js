const { spawn } = require('child_process');

const button = document.querySelector("#button");

// is [] in this necessary?
button.onclick = script([]);


function script() {
    fetch('https://alex-gallagher.github.io/NEA/run-python')
        .then(response => response.json())
        .then(data => {
            console.log(data.output);
        })
        .catch(error => console.error('Error:', error));
    
    button.innerText = '';

};

/*
const container = document.querySelector("#container"),  
tile = document.querySelector(".tile");

for(let i = 0; i < 1599; i++) {
  container.appendChild(tile.cloneNode());
}

*/