<template>
<div>
    <BlogHeader/>

    <LeftSideBar/>
    <ArticleList/>
    <BlogFooter/>
</div>
</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import ArticleList from '@/components/ArticleList.vue'
    import LeftSideBar from '@/components/LeftSideBar.vue'

    export default {
        name: 'Home',
        components: { BlogHeader, BlogFooter, ArticleList, LeftSideBar }
    }
</script>


<style>

#spkj{
    position: absolute;
    left: 800px;
    top: 200px;
    width: 600px;
    height: 456px;
    
    
}

.mce_SELRES_start{
    display: inline-block; width: 0px; overflow: hidden; line-height: 0;
}

</style>


<!-- document.getElementById("spkj").style.height=document.getElementById("spkj").scrollWidth*0.76+"px"; -->