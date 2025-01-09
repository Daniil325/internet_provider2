import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

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
            email: email, password: password
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
            console.log(result)
            user = result;
            setUserData("goooooooooool");
        });
    }


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
        <>
            <div>
                <input
                    type="text"
                    name="email"
                    id=""
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    type="text"
                    name="password"
                    id=""
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <p onClick={onLogin}>
                    login
                </p>
            </div>
            {userData ? <div>пользователь {userData}</div> : <div>данные не получены</div>}
        </>
    );
}

export default App;
