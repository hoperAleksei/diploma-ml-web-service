import {API_BASE} from "@/api/config";

async function getDatasets(token) {
    try {
        let res = await fetch(API_BASE + 'ds/get_datasets', {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + token
            }
        })
        if (res.ok) {
            return await res.json()
        } else {
            console.log(e)
            throw new Error('Cannot get datasets')
        }
    } catch (e) {
        console.log(e)
        throw new Error('Cannot get datasets')
    }

}

async function useDataset(token, id) {
    try {
        let res = await fetch(API_BASE + 'ds/use_dataset', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({id: id})
        })
        let ans = await res.json()
        if (res.ok && ans.status === 'ok') {
            return {status: true}
        } else {
            return {status: false}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }
}

async function uploadDsFile(token, file) {
    try {
        let form_data = new FormData()
        form_data.append("file", file)

        let res = await fetch(API_BASE + 'ds/upload_file', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
            },
            body: form_data
        })
        let ans = await res.json()
        if (res.ok) {
            return {status: true}
        } else {
            return {status: false, detail: ans.detail}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }
}

async function uploadDsUrl(token, url) {
    try {
        let res = await fetch(API_BASE + 'ds/upload_url', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({url: url})
        })
        let ans = await res.json()
        if (res.ok) {
            return {status: true}
        } else {
            return {status: false, detail: ans.detail}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }
}

async function getTable(token) {
    try {
        let res = await fetch(API_BASE + 'ds/get_use', {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + token,
            },
        })
        let ans = await res.json()
        if (res.ok) {
            return {status: true, table: ans}
        } else {
            return {status: false, detail: ans.detail}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }
}

async function getDsNames(token) {
    let res = await fetch(API_BASE + 'ds/names', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    return await res.json()
}

async function restoreDs(token) {
    let res = await fetch(API_BASE + 'ds/restore', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    return await res.json()
}

export {getDatasets, useDataset, uploadDsFile, uploadDsUrl, getTable, getDsNames, restoreDs}
