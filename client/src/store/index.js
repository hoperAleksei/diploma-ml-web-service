import {createStore} from 'vuex'
import createPersistedState from "vuex-persistedstate";
import {getMe, getAuth} from "@/api/auth";

function setLogin(context, token, username, role) {
    context.commit('setToken', token)
    context.commit('setAuth', true)
    context.commit('setUsername', username)
    context.commit('setRole', role)
}

export default createStore({
    state: () => ({
        isAuth: false,
        username: '',
        role: '',
        token: ''
    }),
    getters: {},
    mutations: {
        setAuth(state, isAuth) {
            state.isAuth = isAuth
        },
        setUsername(state, username) {
            state.username = username
        },
        setToken(state, token) {
            state.token = token
        },
        setRole(state, role) {
            state.role = role
        }
    },
    actions: {
        logout(context) {
            context.commit('setToken', '')
            context.commit('setAuth', false)
            context.commit('setUsername', '')
            context.commit('setRole', '')
        },
        async login(context, {username, password}) {
            let res = await getAuth('login', username, password)
            if (res.status === true) {
                let user = await getMe(res.token)
                setLogin(context, res.token, user.username, user.role)
            } else {
                throw new Error('Invalid user or password')
            }
        },
        async register(context, {username, password}) {
            let res = await getAuth('register', username, password)
            if (res.status === true) {
                let user = await getMe(res.token)
                setLogin(context, res.token, user.username, user.role)
            } else {
                throw new Error('Invalid user or password')
            }
        },
    },
    // modules: {},
    plugins: [createPersistedState()]
})
