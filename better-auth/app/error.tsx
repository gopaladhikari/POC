"use client";

import { Button } from "@heroui/button";
import { Link } from "@heroui/link";

import { Icon } from "@iconify/react";
import { AnimatePresence, motion } from "framer-motion";

export default function Page({
  error,
}: {
  error: Error & { digest?: string };
}) {
  return (
    <AnimatePresence>
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{
          duration: 0.5,
          type: "tween",
        }}
        className="mt-36"
      >
        <div className="flex h-full w-full items-center justify-center">
          <div className="rounded-large bg-content1 shadow-small flex flex-col items-center justify-center p-12">
            <Icon
              icon="ant-design:warning-filled"
              className="text-5xl text-accent fill-accent"
            />
            <div className="mt-4 text-h3 font-medium">Oops {error.message}</div>
            <div className="mt-2 text-body-small text-default-500">
              Our team has been notified and we&apos;ll do our best to resolve
              the issue as soon as possible.
            </div>
            <Button className="mt-4" color="primary" as={Link} href="/">
              Go back home
            </Button>
          </div>
        </div>
      </motion.div>
    </AnimatePresence>
  );
}
