const { spawn } = require('child_process');

const button = document.querySelector("#button");

// is [] in this necessary?
button.onclick = script([]);

button.innerText = '';


function script() {
    fetch('https://alex-gallagher.github.io/NEA/run-python')
        .then(response => response.json())
        .then(data => {
            console.log(data.output);
        })
        .catch(error => console.error('Error:', error));
};

