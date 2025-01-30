import { Link } from "react-router-dom";
import styles from "./header.module.css";

export const Header = () => {
    return (
        <header className={styles.header}>
            <h1>ООО "Провайдер"</h1>
            <p></p>
            <Link to="/lk" className={styles.lk}>личный кабинет</Link>
        </header>
    );
};
