import { FloatLabel } from "primereact/floatlabel";
import styles from "./lk.module.css";
import { InputText } from "primereact/inputtext";
import { Password } from "primereact/password";
import { Button } from "primereact/button";
import { useState } from "react";

export const Login = () => {
    const [value, setValue] = useState();

    return (
        <>
            <header className={styles.header}>
                <h1>Личный кабинет</h1>
                <p className={styles.lk}>на главную</p>
            </header>
            <main className={styles.main}>
                <h2 className={styles.main__title}>Вход</h2>

                <div className={styles.login}>
                    <FloatLabel>
                        <InputText
                            id="email"
                            value={value}
                            onChange={(e) => setValue(e.target.value)}
                        />
                        <label htmlFor="email">Email</label>
                    </FloatLabel>
                    <p></p>
                    <p></p>
                    <br />
                    <FloatLabel>
                        <Password
                            id="email"
                            value={value}
                            onChange={(e) => setValue(e.target.value)}
                        />
                        <label htmlFor="email">Пароль</label>
                    </FloatLabel>
                    <p></p>
                    <Button label="Войти" severity="success" />
                </div>
            </main>
            <footer className={styles.footer}>
                <h1>ООО "Провайдер"</h1>
            </footer>
        </>
    );
};
