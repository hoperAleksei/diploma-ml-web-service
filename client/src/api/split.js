import {API_BASE} from "@/api/config";

async function split(token, splits) {
    try {
        let res = await fetch(API_BASE + 'split', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(splits),
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

export {split}
