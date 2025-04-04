const { spawn } = require('child_process');
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());  // Allow cross-origin requests

app.get('/run-python', (req, res) => {
    const prog = spawn('python', ['testing.py']);

    let output = '';
    prog.stdout.on('data', (data) => {
        output += data.toString();
    });

    prog.stderr.on('data', (err) => {
        console.error(`Error: ${err}`);
    });

    prog.on('close', (code) => {
        res.json({ output, exitCode: code });
    });
});

app.listen(3000, () => console.log('Server running on port 3000'));
