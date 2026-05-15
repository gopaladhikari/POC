import express from "express";
import Redis from "ioredis";
import mongoose from "mongoose";

const app = express();

const redis = new Redis("redis://localhost:6379");

const BANNER_KEY = "app:banner";

function otpKey(phone: string) {
  return `otp:${phone}`;
}

// Setup

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

// Banner

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

// OTP

app.post("/otp", async (req, res) => {
  const phone = req.body.phone;

  const otp = Math.floor(100000 + Math.random() * 900000).toString();

  await redis.set(otpKey(phone), otp, "EX", 300);

  res.json({ otp });
});

app.post("/otp/verify", async (req, res) => {
  const { phone, otp } = req.query;

  const exists = await redis.exists(otpKey(phone as string));

  if (!exists) return res.json({ message: "OTP not found" });

  const redisOtp = await redis.get(otpKey(phone as string));

  if (redisOtp !== otp) return res.json({ message: "OTP not valid" });

  await redis.del(otpKey(phone as string));

  res.json({ otp });
});

app.get("/otp/:phone/ttl", async (req, res) => {
  const phone = req.params.phone;
  const ttl = await redis.ttl(otpKey(phone as string));

  res.json({ ttl });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
