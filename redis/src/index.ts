import express from "express";
import Redis from "ioredis";
import mongoose from "mongoose";

const app = express();

const redis = new Redis("redis://localhost:6379");

const BANNER_KEY = "app:banner";

app.get("/redis", async (req, res) => {
  const reply = await redis.ping();

  res.json({ redis: reply });
});

app.get("/mongo", async (req, res) => {
  const url = "mongodb://localhost:27017/redis";

  if (mongoose.connection.readyState === 0)
    await mongoose.connect(url);

  res.json({
    mongo: "connected",
    database: mongoose.connection.name,
  });
});

app.post("/banner", async (req, res) => {
  const banner = req.body.banner;

  await redis.set(BANNER_KEY, banner);

  res.json({ banner });
});

app.get("/banner", async (req, res) => {
  const banner = await redis.get(BANNER_KEY);

  if (!banner)
    return res.json({
      message: "No banner found",
    });

  res.json({ banner });
});

app.delete("/banner", async (req, res) => {
  await redis.del(BANNER_KEY);

  res.json({ message: "Banner deleted" });
});

app.get("/banners/exists", async (req, res) => {
  const banner = await redis.exists(BANNER_KEY);

  res.json({ exists: Boolean(banner) });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
