import { DataTable } from "primereact/datatable"
import { Column } from "primereact/column"
import { ColumnMeta } from "../../../common"
import { Card } from "primereact/card"

type Props = {
    items: object[],
    columns: ColumnMeta[], 
    title: string
}

export const DataView = ({items, columns, title}: Props) => {
    return (
        <Card title={title}>
            <DataTable 
                value={items}
                showGridlines
                rowHover
            >
            {columns.map((col, i) => (
                    <Column key={col.field} field={col.field} header={col.header} body={col.body} />
                ))}
            </DataTable>
        </Card>
    )
}