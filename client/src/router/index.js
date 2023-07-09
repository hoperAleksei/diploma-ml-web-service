import {createRouter, createWebHistory} from 'vue-router'
import LoginView from "@/views/LoginView.vue";
import ProfileView from "@/views/ProfileView.vue";
import store from "@/store";
import NotFoundView from "@/views/NotFoundView.vue";
import CreateView from "@/views/CreateView.vue";
import AdminView from "@/views/AdminView.vue";
import PreproView from "@/views/PreproView.vue";
import DatasetsView from "@/views/DatasetsView.vue";
import AutofitView from "@/views/AutofitView.vue";
import SplitView from "@/views/SplitView.vue";
import resultView from "@/views/ResultView.vue";

const routes = [
    {
        path: '/login',
        name: 'login',
        component: LoginView
    },
    {
        path: '/profile',
        name: 'profile',
        component: ProfileView,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/admin',
        name: 'admin',
        component: AdminView,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: '/result/:id',
        name: 'result',
        component: resultView,
        props: true,
    },
    {
        path: '/',
        name: 'create',
        component: CreateView,
        meta: {
            requiresAuth: true,
            checkState: true
        },
    },
    {
        path: '/datasets',
        name: 'datasets',
        component: DatasetsView,
        meta: {
            requiresAuth: true,
            checkState: true
        },
    },
    {
        path: '/preprocess',
        name: 'preprocess',
        component: PreproView,
        meta: {
            requiresAuth: true,
            checkState: true
        },
    },
    {
        path: '/split',
        name: 'split',
        component: SplitView,
        meta: {
            requiresAuth: true,
            checkState: true
        },
    },
    {
        path: '/autofit',
        name: 'autofit',
        component: AutofitView,
        meta: {
            requiresAuth: true,
            checkState: true
        },
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'notFound',
        component: NotFoundView,
        meta: {
            requiresAuth: true
        }

    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach(async (to, _, next) => {
    if (to.name === 'login' && store.state.isAuth) {
        next('/profile')
        return
    }
    if (to.matched.some(record => record.meta.requiresAuth) && !store.state.isAuth) {
        next('/login')
    }
    if (to.matched.some(record => record.meta.checkState)) {
        await store.dispatch('updateState')
        // console.log({state: store.state.state, route: true})
        if (store.state.state === 'ready' && to.name !== 'create') {
            next('/')
            return
        }
        if (store.state.state === 'start' && to.name !== 'datasets') {
            next('/datasets')
            return
        }
        if (store.state.state === 'prepro' && to.name !== 'preprocess') {
            next('/preprocess')
            return
        }
        if (store.state.state === 'split' && to.name !== 'split') {
            next('/split')
            return
        }
        if (store.state.state === 'autofit' && to.name !== 'autofit') {
            next('/autofit')
            return
        }
    }
    next()
})

export default router
