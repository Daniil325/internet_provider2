import { Button } from "primereact/button";
import styles from "./payment.module.css";
import { useState } from "react";
import { Dropdown } from "primereact/dropdown";
import { InputText } from "primereact/inputtext";

export const Payment = () => {
    const [selectedCity, setSelectedCity] = useState(null);
    const cities = [
        { name: "Тариф 1", code: "NY" },
        { name: "Тариф 2", code: "RM" },
        { name: "Тариф 3", code: "LDN" },
        { name: "Тариф 4", code: "IST" },
        { name: "Тариф 5", code: "PRS" },
    ];
    const [value, setValue] = useState("");

    return (
        <>
            <header className={styles.header}>
                <h1>Личный кабинет</h1>
                <p className={styles.lk}>на главную</p>
            </header>
            <main className={styles.main}>
                <h2 className={styles.main__title}>Оплата</h2>

                <div className="flex flex-column gap-2">
                    <label htmlFor="username">Тариф</label>
                    <Dropdown
                        value={selectedCity}
                        onChange={(e) => setSelectedCity(e.value)}
                        options={cities}
                        optionLabel="name"
                        placeholder="Тариф"
                        className=""
                    />
                </div>

                <p></p>
                <p></p>
                <br />

                <div className="flex flex-column gap-2">
                    <label htmlFor="username">Сумма к оплате</label>
                    <InputText id="username" aria-describedby="username-help" />
                </div>
                <p></p>
                <Button label="Оплатить" severity="success" />
            </main>
            <footer className={styles.footer}>
                <h1>ООО "Провайдер"</h1>
            </footer>
        </>
    );
};
