"use client";

import { Icon } from "@iconify/react";
import { Spinner } from "@heroui/spinner";
import { AnimatePresence, motion } from "framer-motion";

export default function LoadingPage() {
  return (
    <AnimatePresence>
      <motion.main
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="flex h-screen w-screen items-center justify-center">
          <div className="flex flex-col items-center gap-4">
            <Spinner />
            <h1 className="text-3xl font-bold">Loading...</h1>
            <p className="text-sm text-default-500">
              Please wait while we load the page
            </p>
            <Icon
              icon="ant-design:loading"
              className="text-5xl animate-spin"
            />
          </div>
        </div>
      </motion.main>
    </AnimatePresence>
  );
}
