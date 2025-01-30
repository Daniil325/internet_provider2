import styles from "./main.module.css";

export const Main = () => {
    return (
        <>
            <main className={styles.main}>
                <h2 className={styles.main__title}>Наши тарифы</h2>
                <div>
                    <div className={styles.tariff__item}>
                        <h3 className={styles.tariff__item_title}>Тариф 1</h3>
                        <p className={styles.tariff__item_descr}>Интернет</p>
                        <p className={styles.tariff__item_price}>цена: 500 рублей</p>
                        <p className={styles.tariff__item_choise}>Выбрать</p>
                    </div>
                    <div className={styles.tariff__item}>
                        <h3 className={styles.tariff__item_title}>Тариф 2</h3>
                        <p className={styles.tariff__item_descr}>Интернет + ТВ-каналы</p>
                        <p className={styles.tariff__item_price}>цена 1000 рублей</p>
                        <p className={styles.tariff__item_choise}>Выбрать</p>
                    </div>
                    <div className={styles.tariff__item}>
                        <h3 className={styles.tariff__item_title}>Тариф 3</h3>
                        <p className={styles.tariff__item_descr}>Интернет + ТВ-каналы + подписки</p>
                        <p className={styles.tariff__item_price}>цена 1500 рублей</p>
                        <p className={styles.tariff__item_choise}>Выбрать</p>
                    </div>
                    <div className={styles.tariff__item}>
                        <h3 className={styles.tariff__item_title}>Тариф 4</h3>
                        <p className={styles.tariff__item_descr}>Интернет + ТВ-каналы + подписки + онлайн кинотеатр</p>
                        <p className={styles.tariff__item_price}>цена 2000 рублей</p>
                        <p className={styles.tariff__item_choise}>Выбрать</p>
                    </div>
                     <div className={styles.tariff__item}>
                        <h3 className={styles.tariff__item_title}>Тариф 5</h3>
                        <p className={styles.tariff__item_descr}>Интернет + ТВ-каналы + подписки + онлайн кинотеатр + бонусы в онлайн-игре</p>
                        <p className={styles.tariff__item_price}>цена 2500 рублей</p>
                        <p className={styles.tariff__item_choise}>Выбрать</p>
                    </div>
                </div>
            </main>

            <footer className={styles.footer}>
                <h1>ООО "Провайдер"</h1>
            </footer>
        </>
    );
};
