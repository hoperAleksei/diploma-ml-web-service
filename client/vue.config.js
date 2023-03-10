const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    configureWebpack: {
        entry: "./src/main.js",
        devServer: {
            hot: true,
        },
        watch: true,
        watchOptions: {
            ignored: /node_modules/,
            poll: 1000,
        },
    },
    transpileDependencies: true,
});
