import { Button } from "primereact/button";
import { DataView } from "../../../components/admin/grid/grid";

const items = [
    {
        id: "1",
        name: "Тариф 1",
        descripiton: "Интернет",
        price: 500,
    },
    {
        id: "1",
        name: "Тариф 2",
        descripiton: "Интернет + ТВ-каналы",
        price: 1000,
    },
    {
        id: "1",
        name: "Тариф 3",
        descripiton: "Интернет + ТВ-каналы + подписки",
        price: 1500,
    },
    {
        id: "1",
        name: "Тариф 4",
        descripiton: "Интернет + ТВ-каналы + подписки + онлайн кинотеатр",
        price: 2000,
    },
    {
        id: "1",
        name: "Тариф 5",
        descripiton: "Интернет + ТВ-каналы + подписки + онлайн кинотеатр + бонусы в онлайн-игре",
        price: 2500,
    },
];

export const TariffList = () => {
    const columns = [
        { header: "Название", field: "name" },
        { header: "Описание", field: "descripiton" },
        { header: "Цена", field: "price" },
    ];
    return (
        <>
            <DataView items={items} columns={columns} title="Список тарифов" />
            <Button label="Добавить тариф" icon="pi pi-plus" severity="success" />
        </>
    );
};
