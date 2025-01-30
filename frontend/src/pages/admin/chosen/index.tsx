import { DataView } from "../../../components/admin/grid/grid"

const items = [
    {
        id: "1",
        client: "Иванов Иван Иванович",
        tariff: "Тариф 1",
    },
    {
        id: "1",
        client: "Иванов Иван Иванович",
        tariff: "Тариф 2",
    },
    {
        id: "1",
        client: "Петров Петр Петрович",
        tariff: "Тариф 1",
    },
    
]

export const ChosenList = () => {
    const columns = [
        { header: "Клиент", field: "client" },
        { header: "Тариф", field: "tariff" },
    ]
    return (
        <DataView
            items={items}
            columns={columns}
            title="Список выбранных тарифов"
        />
    )
}