import { Worker } from "bullmq";

import { connection } from "./queue";

const worker = new Worker(
  "emails",
  async (job) => {
    console.log("Email job received", job.name);

    await new Promise((resolve) => setTimeout(resolve, 1000));

    console.log("Email job completed", job);
  },
  {
    connection,
  },
);

worker.on("completed", (job) => {
  console.log("Job completed", job);
});

worker.on("failed", (job, err) => {
  console.log("Job failed", job, err);
});

export { worker };
