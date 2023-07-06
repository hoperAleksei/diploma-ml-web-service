import {API_BASE} from "@/api/config";

async function getMe(token) {
    let res = await fetch(API_BASE + 'auth/users/me', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    return await res.json()
}

async function getAuth(method='login', username, password) {
    let auth_url
    switch (method) {
        case 'login':
            auth_url = API_BASE + 'auth/token'
            break
        case 'register':
            auth_url = API_BASE + 'auth/register'
            break
        default:
            throw 'not support method'
    }
    try {
        let res = await fetch(auth_url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                'username': username,
                'password': password
            })
        })

        if (res.ok) {
            let token = (await res.json()).access_token
            return {status: true, token: token}
        } else {
            return {status: false}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }
}

export {
    getAuth,
    getMe
}
