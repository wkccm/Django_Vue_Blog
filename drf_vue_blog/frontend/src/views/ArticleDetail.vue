<template>
<div>
    <BlogHeader/>
    <LeftSideBar />
    <ArticleContent :key="$route.path"/>

    <BlogFooter/>
</div>
</template>

<script>
    import BlogHeader from '@/components/BlogHeader.vue'
    import BlogFooter from '@/components/BlogFooter.vue'
    import LeftSideBar from '@/components/LeftSideBar.vue'
    import ArticleContent from '@/components/ArticleContent.vue'


    export default {
        name: 'ArticleDetail',
        components: { BlogHeader, BlogFooter, LeftSideBar, ArticleContent, ArticleContent },
    }
</script>

