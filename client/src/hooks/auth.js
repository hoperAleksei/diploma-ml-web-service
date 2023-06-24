import {API_BASE} from "@/hooks/api";
// import {mapState, mapGetters, mapActions, mapMutations} from 'vuex'
import store from "@/store"

async function getMe() {
    let res = await fetch(API_BASE + 'auth/users/me', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + store.getters.getToken
        }
    })
    return await res.json()
}

async function getAuth(username, password) {
    try {
        let res = await fetch(API_BASE + 'auth/token', {
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
            store.commit('setToken', (await res.json()).access_token)
            store.commit('setAuth', true)
            let me = await getMe()
            store.commit('setUsername', me.username)
            store.commit('setRole', me.role)
            return true
        } else {
            return false
        }

    } catch (e) {
        console.log(e)
        return false
    } finally {

    }

}

async function getReg(username, password) {
    try {
        let res = await fetch(API_BASE + 'auth/register', {
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
            store.commit('setToken', (await res.json()).access_token)
            store.commit('setAuth', true)
            let me = await getMe()
            store.commit('setUsername', me.username)
            store.commit('setRole', me.role)
            return true
        } else {
            return false
        }
    } catch (e) {
        console.log(e)
        return false
    } finally {

    }

}

function logout() {
    store.commit('setToken', '')
    store.commit('setAuth', false)
    store.commit('setUsername', '')
    store.commit('setRole', '')
}

export {
    getAuth,
    getReg,
    logout
}

