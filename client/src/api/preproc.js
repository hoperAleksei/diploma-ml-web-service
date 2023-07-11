import {API_BASE} from "@/api/config";

async function getPre(token) {
    let res = await fetch(API_BASE + 'pre/types', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    return await res.json()
}

async function prepro(token, req) {
    try {
        let res = await fetch(API_BASE + 'pre', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(req),
        })
        const resp = await res.json()
        if (res.ok) {
            return {status: true, res: resp}
        } else {
            return {status: false}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }


    return await res.json()
}

async function preCommit(token) {
    try {
        let res = await fetch(API_BASE + 'pre/commit', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token
            }
        })
        const resp = await res.json()
        if (res.ok && resp.status === 'ok') {
            return {status: true}
        } else {
            return {status: false}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }

}

export {getPre, prepro, preCommit}
