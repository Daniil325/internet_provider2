import { Button } from "primereact/button";
import { Card } from "primereact/card";
import { InputText } from "primereact/inputtext";
import { InputTextarea } from "primereact/inputtextarea";

export const TariffCreate = () => {
    return (
        <>
            <Card title="Создание тарифа">
                <div className="flex flex-column gap-2">
                    <label htmlFor="username">Название</label>
                    <InputText id="username" aria-describedby="username-help" />
                </div>
                <p></p>
                <div className="flex flex-column gap-2">
                    <label htmlFor="username">Описание</label>
                    <InputTextarea autoResize rows={5} cols={30} />
                </div>
                <p></p>
                <div className="flex flex-column gap-2">
                    <label htmlFor="username">Цена</label>
                    <InputText id="username" aria-describedby="username-help" />
                </div>
                <p></p>
                <Button label="Добавить" icon="pi pi-plus" severity="success" />
            </Card>
        </>
    );
};
