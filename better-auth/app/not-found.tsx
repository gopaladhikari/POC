"use client";

import { AnimatePresence, motion } from "framer-motion";
import { Button } from "@heroui/button";
import { Icon } from "@iconify/react";
import { Link } from "@heroui/link";

export default function Page() {
  return (
    <main className="flex h-screen w-screen items-center justify-center">
      <AnimatePresence>
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 0.8 }}
          transition={{ duration: 0.5 }}
        >
          <div className="flex flex-col items-center gap-8">
            <Icon
              icon="ant-design:warning-filled"
              className="text-5xl text-accent fill-accent"
            />
            <h1 className="text-3xl font-medium">Oops! Page not found</h1>
            <p className="text-lg text-default-500">
              We can&apos;t seem to find the page you&apos;re looking for.
            </p>
            <Button color="primary" className="mt-4">
              <Link href="/">Go back home</Link>
            </Button>
          </div>
        </motion.div>
      </AnimatePresence>
    </main>
  );
}
