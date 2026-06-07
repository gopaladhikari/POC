import express from "express";
import { WebSocketServer } from "ws";
import http from "http";
import fs from "fs";
import path from "path";

const app = express();

const server = http.createServer(app);

const webSocketServer = new WebSocketServer({ server });

webSocketServer.on("connection", (socket) => {
  console.log("New connection...");

  socket.on("message", (data) => {
    webSocketServer.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(data.toString());
      }
    });
  });
});

app.get("/", async (req, res) => {
  const currentDir = process.cwd();

  const indexHtml = fs.readFileSync(
    path.join(currentDir, "index.html"),
    "utf-8",
  );

  res.setHeader("Content-Type", "text/html");

  res.send(indexHtml);
});

server.listen(3000, () => {
  console.log("Server is running on port 3000");
});
