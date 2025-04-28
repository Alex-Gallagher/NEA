var http = require('http');
var fs = require('fs');
var index = fs.readFileSync('index.html');
var script = fs.readFileSync('script.js');

const PORT = 3000;

http.createServer(function (req, res) {
  if (req.path.endsWith('script.js')) {
    res.writeHead(200, {'Content-Type': 'text/javascript'});
    res.end(script);
  } else {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(index);
  }
}).listen(PORT);

console.log(`Listening on port ${PORT}`);

const app = express();
app.use(cors());

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
