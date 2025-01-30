import { DataView } from "../../../components/admin/grid/grid"

const items = [
    {
        id: "1",
        fio: "Иванов Иван Иванович",
        phone: "89132405930",
        email: "ivan@mail.ru",
        username: "ivan20"
    }, {
        id: "1",
        fio: "Петров Петр Петрович",
        phone: "9231234504",
        email: "ppp@mail.ru",
        username: "petr123"
    }, {
        id: "1",
        fio: "Волков Сергей Иванович",
        phone: "88001235049",
        email: "serega@mail.ru",
        username: "segey39393@mail.ru"
    }, {
        id: "1",
        fio: "Козлов Денис Юрьевич",
        phone: "89132049650",
        email: "ddd@mail.ru",
        username: "denis51"
    },
]

export const ClientList = () => {
    const columns = [
        {header: "ФИО", field: "fio"},
        {header: "Номер телефона", field: "phone"},
        {header: "Email", field: "email"},
        {header: "Имя пользователя", field: "username"},
    ]
    return (
        <DataView
            items={items}
            columns={columns}
            title="Список клиентов"
        />
    )
}