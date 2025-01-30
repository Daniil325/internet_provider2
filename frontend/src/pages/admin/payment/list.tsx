import { DataView } from "../../../components/admin/grid/grid"

const items = [
    {
        id: "1",
        client: "Иванов Иван Иванович",
        amount: 200,
    }, {
        id: "1",
        client: "Иванов Иван Иванович",
        amount: 250,
    }, {
        id: "1",
        client: "Петров Петр Петрович",
        amount: 300,
    }, {
        id: "1",
        client: "Волков Сергей Иванович",
        amount: 50,
    }, {
        id: "1",
        client: "Волков Сергей Иванович",
        amount: 100,
    },
]

export const PaymentList = () => {
    const columns = [
        { header: "ФИО", field: "client" },
        { header: "Сумма", field: "amount" },
    ]
    return (
        <DataView
            items={items}
            columns={columns}
            title="Список платежей"
        />
    )
}