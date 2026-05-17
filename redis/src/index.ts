import express from "express";
import Redis from "ioredis";
import mongoose from "mongoose";
import { emailQueue } from "./queue";

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

// User

function getUserkey(id: string) {
  return `user:${id}`;
}

app.post("/user", async (req, res) => {
  const { id } = req.params as { id: string };

  const user = await redis.set(
    getUserkey(id),
    JSON.stringify(req.body),
  );

  return res.json({ user });
});

app.get("/user/:id", async (req, res) => {
  const { id } = req.params as { id: string };

  const user = await redis.get(getUserkey(id));

  if (!user) return res.json({ message: "User not found" });

  return res.json({ user: JSON.parse(user) });
});

app.delete("/user/:id", async (req, res) => {
  const { id } = req.params as { id: string };

  await redis.del(getUserkey(id));

  return res.json({ message: "User deleted" });
});

app.post("/user/:id/hash", async (req, res) => {
  const { id } = req.params as { id: string };

  const user = await redis.hset(getUserkey(id), req.body);

  return res.json({ user });
});

app.get("/user/:id/hash", async (req, res) => {
  const { id } = req.params as { id: string };

  const user = await redis.hgetall(getUserkey(id));

  if (!user) return res.json({ message: "User not found" });

  return res.json({ user });
});

app.delete("/user/:id/hash", async (req, res) => {
  const { id } = req.params as { id: string };

  await redis.hdel(getUserkey(id));

  return res.json({ message: "User deleted" });
});

// Email Queue

const QUEUE_NAME = "queue:email";

app.post("/emails", async (req, res) => {
  const job = {
    to: req.body.to,
    subject: req.body.subject,
    body: req.body.body,
    createdAt: new Date().toISOString(),
  };

  await redis.lpush(QUEUE_NAME, JSON.stringify(job));

  res.json({ message: "Email added to queue" });
});

app.get("/emails", async (req, res) => {
  const rawJobs = await redis.rpop(QUEUE_NAME);

  res.json({ jobs: rawJobs ? JSON.parse(rawJobs) : [] });
});

// BullMQ

app.post("/welcome-emails", async (req, res) => {
  const { email } = req.body;

  const job = await emailQueue.add(
    "send-welcome-email",
    {
      name: "welcome-email",
      data: {
        to: email,
        subject: "Welcome to Redis",
        body: "Welcome to Redis",
      },
    },
    {
      attempts: 3,
      backoff: {
        type: "exponential",
        delay: 5000,
      },
    },
  );

  console.log("Job added", job);

  res.json({ job });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
