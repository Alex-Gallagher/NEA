const { spawn } = require('child_process');

function runPythonScript(scriptPath, input) {

    const prog = spawn('python', [scriptPath].concat(input));

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

runPythonScript('/backend/testing.py', []);