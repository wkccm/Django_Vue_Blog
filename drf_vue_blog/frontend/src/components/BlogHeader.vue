<template>
<div>
    <div id="header">
        <div class="grid">
            <div></div>
            <div>
                <div id="titlebox">
                    <router-link to="/" class="titlelink"><h1 id="blog-title">My Django-Vue Blog</h1></router-link>
                </div>
            </div>
            <SearchButton/>
        </div>
        <hr id="title-hr">
        <div class="login">
            <div v-if="hasLogin">
                <div class="dropdown">
                    <button class="dropbtn">欢迎, {{username}}!</button>
                    <div class="dropdown-content">
                        <router-link :to="{ name: 'UserCenter', params: { username: username }}">用户中心</router-link>
                        <router-link :to="{ name: 'ArticleCreate' }" v-if="isSuperuser">发表文章</router-link>
                        <router-link to="/" v-on:click.prevent="logout()">登出</router-link>
                    </div>
                </div>
            </div>
            <div v-else>
                <router-link to="/login" class="login-link dropdown">
                    <button class="dropbtn">登录 / 注册</button>
                </router-link>
            </div>
        </div>
    </div>

    <div id="header-place">

    </div>
</div>
</template>

<script>
    import authorization from '@/utils/authorization';
    
    import SearchButton from '@/components/SearchButton.vue'

    export default {
        name: 'BlogHeader',
        components: {SearchButton},
        data: function () {
            return {
                username: '',
                hasLogin: false,
                isSuperuser: JSON.parse(localStorage.getItem('isSuperuser.myblog')),
            }
        },
        mounted() {
            authorization().then((data) => [this.hasLogin, this.username] = data);
        },
        methods: {
            logout() {
                localStorage.clear();
                window.location.reload(false);
            },
            refresh() {
                this.username = localStorage.getItem('username.myblog');
            }
        }
    }
</script>

<style scoped>
    #header {
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        height: 160px;
        text-align: center;
        margin: 0 0;
        background-color: whitesmoke;
        z-index: 1;
    }

    #header-place{
        height: 160px;
        margin: 0 auto;
    }

    #titlebox{
        margin: 0 auto;
        width: 600px;
        background-color: lightblue;
        border-radius: 10px;
    }

    #blog-title{
        width: 600px;
        margin: 0 auto;
    }

    #title-hr{
        border: 3px solid grey;
    }

    .titlelink{
        text-decoration: none;
        color: black;
        width: 30%;
    }

    .grid {
        display: grid;
        grid-template-columns: 1fr 4fr 1fr;
    }

    .login-link {
        color: black;
    }

    .login {
        text-align: right;
        padding-right: 5px;
    }

    .dropbtn {
        background-color: mediumslateblue;
        color: white;
        padding: 8px 8px 30px 8px ;
        font-size: 16px;
        border: none;
        cursor: pointer;
        height: 16px;
        border-radius: 5px;
    }

    .dropdown {
        position: relative;
        display: inline-block;
    }

    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 120px;
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
        text-align: center;
    }

    .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }

    .dropdown-content a:hover {
        background-color: #f1f1f1
    }

    .dropdown:hover .dropdown-content {
        display: block;
    }

    .dropdown:hover .dropbtn {
        background-color: darkslateblue;
    }
</style>