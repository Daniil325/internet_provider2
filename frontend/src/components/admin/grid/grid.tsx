import { DataTable } from "primereact/datatable"
import { Column } from "primereact/column"
import { ColumnMeta } from "../../../common"

type Props = {
    items: object[],
    columns: ColumnMeta[]
}

export const DataView = ({items, columns}: Props) => {
    return (
        <div className="card">
            <DataTable 
                value={items}
                showGridlines
                rowHover
            >
            {columns.map((col, i) => (
                    <Column key={col.field} field={col.field} header={col.header} body={col.body} />
                ))}
            </DataTable>
        </div>
    )
}