<template>
<div>


    <router-view />

    <audio id="global-bgm" loop="true" autoplay="autoplay" controls="controls">
        <source src="./assets/uno(IOSYS).mp3" />
    </audio>
</div>
</template>

<script>
    export default {
        name: 'App'
    }
</script>

<style>
    #app {
        font-family: Georgia, Arial, sans-serif;

    }

    #global-bgm{
        position: fixed;
        left: 10px;
        bottom: 0px;
        height: 50px;
    }
    html{
        scroll-padding-top: 160px;
    }

</style>