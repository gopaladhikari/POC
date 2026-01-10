import type { Metadata } from "next";
import { Providers } from "./providers";
import { Menu } from "@/components/navbar";
import { Footer } from "@/components/footer";
import "@/styles/globals.css";

export const metadata: Metadata = {
  title: "Auth Lift",
  description:
    "A production-ready, authentication project built with Next.js 16, Better Auth, MongoDB, Resend, and Arcjet. ",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="antialiased" suppressHydrationWarning>
        <Providers>
          <Menu />
          <main>{children}</main>
          <Footer />
        </Providers>
      </body>
    </html>
  );
}
