import {createRouter, createWebHistory} from 'vue-router'
import LoginView from "@/views/LoginView.vue";
import ProfileView from "@/views/ProfileView.vue";
import store from "@/store";
import NotFoundView from "@/views/NotFoundView.vue";
import CreateView from "@/views/CreateView.vue";
import Lologo from "@/views/Lologo.vue";

const routes = [
    {
        path: '/',
        name: 'create',
        component: CreateView,
        meta: {
            requiresAuth: true
        }
    },
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
        path: '/:pathMatch(.*)*',
        name: 'notFound',
        component: NotFoundView

    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

// router.beforeEach((to, _, next) => {
//     if (to.name == 'login') {
//         if (store.getters.getAuth) {
//             next('/profile');
//             return;
//         }
//         else {
//             next();
//         }
//     }
// })

router.beforeEach((to, _, next) => {
    if (to.name == 'login' && store.state.isAuth) {
            next('/profile');
            return;
    }
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (store.state.isAuth) {
            next();
            return;
        }
        next('/login');
    } else {
        next();
    }
});

export default router
