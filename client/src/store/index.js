import {createStore} from 'vuex'
import createPersistedState from "vuex-persistedstate";
import {getAuth, getMe} from "@/api/auth";
import {createExperiment, deleteExperiment, getState} from "@/api/experiment";
import {getDatasets, getDsNames, getTable, restoreDs, uploadDsFile, uploadDsUrl, useDataset} from "@/api/datasets";
import {getPre, preCommit, prepro} from "@/api/preproc";

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
        token: '',
        state: 'ready',
        expName: '',
        dataset: null
    }),
    getters: {},
    mutations: {
        setState(state, newState) {
            state.state = newState
        },
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
        },
        setExpName(state, name) {
            state.expName = name
        },
        setDataset(state, id) {
            state.dataset = id
        },
    },
    actions: {
        async updateState(context) {
            let res = await getState(context.state.token)
            context.commit('setState', res.state)
            context.commit('setExpName', res.name)
        },
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
        async createExp(context, {name}) {
            let res = await createExperiment(context.state.token, name)
            return !!res.status
        },
        async cancelExp(context) {
            let res = await deleteExperiment(context.state.token)
            if (res) {
                context.commit('setExpName', '')
                await context.dispatch("updateState")
            }
            return !!res.status
        },
        async getDatasets(context) {
            try {
                return await getDatasets(context.state.token)
            } catch (e) {
                console.log(e)
            }
        },
        async useDataset(context, {id}) {
            let res = await useDataset(context.state.token, id)
            if (res.status) {
                context.commit("setDataset", id)
                await context.dispatch("updateState")
            }
            return !!res.status
        },
        async postDsFile(context, {file}) {
            return await uploadDsFile(context.state.token, file)
        },
        async postDsUrl(context, {url}) {
            return await uploadDsUrl(context.state.token, url)
        },
        async getTable(context) {
            return await getTable(context.state.token)
        },
        async getDsNames(context) {
            return await getDsNames(context.state.token)
        },
        async restoreDs(context) {
            return await restoreDs(context.state.token)
        },
        async getPre(context) {
            return await getPre(context.state.token)
        },
        async prepro(context, {req}) {
            return await prepro(context.state.token, req)
        },
        async preCommit(context) {
            const res = await preCommit(context.state.token)
            await context.dispatch("updateState")
            return res
        },
    },
    // modules: {},
    plugins: [createPersistedState()]
})
