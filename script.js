const { spawn } = require('child_process');

const button = document.querySelector("#button");

// is [] in this necessary?
button.onclick = script([]);




function script(input) {

    const prog = spawn('python', ['/backend/testing.py'].concat(input));

    prog.stdout.on('data', (out) => {
        console.log(out);
    });

    prog.stderr.on('data', (err) => {
        console.log('ERROR; ', err);
    });

    prog.on('close', (code) => {
        console.log('EXIT; ', code);
    });
}
