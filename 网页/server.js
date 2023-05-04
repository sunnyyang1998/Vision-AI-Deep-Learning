const http = require("http");
const fs = require("fs");
const path = require("path");
const url = require("url");

const hostname = "127.0.0.1";
const port = 3000;

const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  let filePath = "";

  if (parsedUrl.pathname === "/") {
    filePath = path.join(__dirname, "menu/menu.html");
  } else {
    filePath = path.join(__dirname, parsedUrl.pathname);
  }

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.statusCode = 404;
      res.setHeader("Content-Type", "text/plain");
      res.end("File not found");
    } else {
      res.statusCode = 200;
      res.setHeader("Content-Type", getContentType(filePath));
      res.end(data);
    }
  });
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

function getContentType(filePath) {
  const ext = path.extname(filePath);
  switch (ext) {
    case ".html":
      return "text/html";
    case ".css":
      return "text/css";
    case ".js":
      return "text/javascript";
    case ".json":
      return "application/json";
    default:
      return "text/plain";
  }
}
