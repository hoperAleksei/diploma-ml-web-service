import {API_BASE} from "@/api/config";

async function getDatasets(token) {
    let res = await fetch(API_BASE + 'ds/get_datasets', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    return await res.json()
}

// async function useDataset(token) {
//     let res = await fetch(API_BASE + 'ds/use_dataset', {
//         method: 'POST',
//         headers: {
//             'Authorization': 'Bearer ' + token
//         }
//     })
//     return await res.json()
// }
