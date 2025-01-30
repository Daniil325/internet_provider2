import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";
import { Header } from "./components/main/header";
import { Main } from "./components/main/main";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { PrimeReactProvider } from "primereact/api";
import { Lk } from "./components/main/lk";
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';
import 'primereact/resources/primereact.css';
import 'primereact/resources/themes/lara-light-indigo/theme.css';
import { Login } from "./pages/main/login";
import { Payment } from "./pages/main/payment";
import { ClientList } from "./pages/admin/client";
import { PaymentList } from "./pages/admin/payment";
import { AdminPanel } from "./pages/admin";

const setToken = (token: string) => {
    localStorage.setItem("Token", token);
};

const getToken = () => {
    return localStorage.getItem("Token");
};

async function getUserByToken(token: string) {
    var ans = false;

    const res = await axios
        .post(`http://127.0.0.1:8000/client/login`, {
            token: token,
        })
        .then((resp: any) => {
            if (resp.status === 200) {
                const response = resp.data;
                ans = response;
            } else {
                ans = false;
            }
        })
        .catch((error: any) => console.error(error));
    return ans;
}

async function loginUser(email: string, password: string) {
    var ans = false;
    const res = await axios
        .post(`http://127.0.0.1:8000/client/login`, {
            email: email,
            password: password,
        })
        .then((resp: any) => {
            if (resp.status === 200) {
                const response = resp.data;
                ans = response;
            } else {
                ans = false;
            }
        })
        .catch((error: any) => console.error(error));
    return ans;
}

function App() {
    const [userData, setUserData] = useState();

    const [email, setEmail] = useState();
    const [password, setPassword] = useState();

    const onLogin = () => {
        let user = loginUser(email, password);
        user.then(function (result) {
            console.log(result);
            user = result;
            setUserData("goooooooooool");
        });
    };

    // используем UseEffect, чтобы запросить данные при загрузке страницы
    useEffect(() => {
        let token = getToken();
        if (token) {
            let user = getUserByToken(token);
            user.then(function (result) {
                user = result;
                setUserData(user);
            });
        }
    }, []);

    return (
        <BrowserRouter>
            <PrimeReactProvider>
                <Routes>
                    <Route path="/">
                        <Route
                            index
                            element={
                                <>
                                    <Header />
                                    <Main />
                                </>
                            }
                        />
                        <Route
                            path="/lk"
                            element={
                                <Lk />
                            }
                        />
                        <Route
                            path="/login"
                            element={
                                <Login />
                            }
                        />
                        <Route
                            path="/payment"
                            element={
                                <Payment />
                            }
                        />
                        <Route path="admin/*" element={<AdminPanel/>}/>
                        
                    </Route>
                </Routes>
            </PrimeReactProvider>
        </BrowserRouter>
    );
}

export default App;
