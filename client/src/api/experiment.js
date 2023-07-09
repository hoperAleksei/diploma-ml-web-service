import {API_BASE} from "@/api/config";

async function getState(token) {
    let res = await fetch(API_BASE + 'state', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    return await res.json()
}

async function createExperiment(token, name) {
    try {
        let res = await fetch(API_BASE + 'state/experiment', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({name: name})
        })
        if (res.ok) {
            return {status: true}
        } else {
            return {status: false}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }
}

async function deleteExperiment(token, name) {
    try {
        let res = await fetch(API_BASE + 'state/experiment', {
            method: 'DELETE',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            }
        })
        if (res.ok) {
            return {status: true}
        } else {
            return {status: false}
        }
    } catch (e) {
        console.log(e)
        return {status: false}
    }
}


async function getExperiments(token) {
    return {}
    // let res = await fetch(API_BASE + 'state/get_experiments', {
    //     method: 'GET',
    //     headers: {
    //         'Authorization': 'Bearer ' + token
    //     }
    // })
    // return await res.json()
}

export {getState, getExperiments, createExperiment, deleteExperiment}
