import { Button } from "primereact/button";
import styles from "./lk.module.css";

export const Lk = () => {
    return (
        <>
            <header className={styles.header}>
                <h1>Личный кабинет</h1>
                <p className={styles.lk}>на главную</p>
            </header>
            <main className={styles.main}>
                <h2 className={styles.main__title}>Добро пожаловать, Иванов Иван</h2>
                <p>Сумма к выплате: 800 руб</p>
                <Button label="Оплатить"/>
                <h2>Ваши тарифы:</h2>
                <div className={styles.tariff__item}>
                        <h3 className={styles.tariff__item_title}>Тариф 1</h3>
                        <p className={styles.tariff__item_descr}>описание</p>
                        <p className={styles.tariff__item_price}>цена: 500 рублей</p>
                    </div>
                    <div className={styles.tariff__item}>
                        <h3 className={styles.tariff__item_title}>Тариф 2</h3>
                        <p className={styles.tariff__item_descr}>описание</p>
                        <p className={styles.tariff__item_price}>цена 1000 рублей</p>
                    </div>
            </main>
            <footer className={styles.footer}>
                <h1>ООО "Провайдер"</h1>
            </footer>
        </>

    )
}