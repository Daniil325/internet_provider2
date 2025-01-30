import "primereact/resources/primereact.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";
import "primereact/resources/themes/saga-blue/theme.css";
import { Outlet, Routes, Route } from "react-router-dom";

import { Layout } from "../../components/layout";
import { ClientList } from "./client";
import { PaymentList } from "./payment";
import { TariffList } from "./tariff/list";
import { ChosenList } from "./chosen";
import { TariffCreate } from "./tariff/create";

export const AdminPanel = () => {
    return (
        <Routes>
            <Route
                path="/"
                element={
                    <Layout>
                        <Outlet />
                    </Layout>
                }
            >
                <Route path="/client" element={<ClientList />} />
                <Route path="/payment" element={<PaymentList />} />
                <Route path="/tariff" element={<TariffList />} />
                <Route path="/chosen" element={<ChosenList />} />
                <Route path="/tariff/create" element={<TariffCreate />} />
            </Route>
        </Routes>
    );
};
