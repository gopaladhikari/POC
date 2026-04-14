const http = require("http");
const fs = require("fs");
const path = require("path");

const port = 8080;

http
  .createServer(function (req, res) {
    const filePath = path.join(
      __dirname,
      req.url === "/" ? "/index.html" : req.url,
    );

    console.log(filePath);

    const ext = path.extname(filePath).toString().toLocaleLowerCase();

    const mimeType = {
      ".html": "text/html",
      ".css": "text/css",
      ".js": "text/javascript",
    };

    const contentType = mimeType[ext] || "application/octet-stream";

    fs.readFile(filePath, (err, data) => {
      if (err) {
        console.error(err);
        res.writeHead(404);
        res.end("404 Not Found");
      } else {
        res.writeHead(200, { "Content-Type": contentType });
        res.end(data, "utf-8");
      }
    });
  })
  .listen(port, () => {
    console.log(`Server running on port ${port}`);
  });
