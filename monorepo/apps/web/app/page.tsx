import styles from "./page.module.css";
import { formatDate } from "@repo/utils";

export default function Home() {
  return (
    <div className={styles.page}>
      <p>{formatDate(new Date())}</p>
    </div>
  );
}
