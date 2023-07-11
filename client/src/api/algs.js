import {API_BASE} from "@/api/config";

async function getAvailable(token) {
    let res = await fetch(API_BASE + 'alg/available', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    return await res.json()
}

async function uploadAlgFile(token, file) {
    try {
        let form_data = new FormData()
        form_data.append("file", file)

        let res = await fetch(API_BASE + 'alg', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
            },
            body: form_data
        })
        let ans = await res.json()
        if (res.ok && (ans.status === 'ok')) {
            return {status: true}
        } else {
            return {status: false, detail: ans.detail}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }
}

async function getAllAlgs(token) {
    let res = await fetch(API_BASE + 'alg', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    return await res.json()
}


export {getAvailable, uploadAlgFile, getAllAlgs}
