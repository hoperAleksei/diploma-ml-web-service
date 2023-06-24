import {createStore} from 'vuex'
import createPersistedState from "vuex-persistedstate";

export default createStore({
    state: () => ({
        isAuth: false,
        username: '',
        role: '',
        token: ''
    }),
    getters: {
        getAuth(state) {
            return state.isAuth
        },
        getUsername(state) {
            return state.username
        },
        isAdmin(state) {
            return state.role === 'admin'
        },
        getToken(state) {
            return state.token
        }
    },
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
        // auth({state, commit}) {
        //     try {
        //         const res = GetAuth()
        //     }
        //     catch (e) {
        //         console.log(e)
        //     }
        //     finally {
        //
        //     }
        // }
    },
    // modules: {},
    plugins: [createPersistedState()]
})
