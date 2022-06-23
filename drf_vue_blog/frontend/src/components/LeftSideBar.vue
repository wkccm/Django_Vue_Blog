<template>
    <div id="LeftSideBar">
        <div class="content-left">
            <div class="left-title">文章导航</div>
            <div class="nav">
                <div v-for="category in category_info" :key="category.id"  class="nav-menu">
                    <div @click="helper($event)" class="nav-title">{{ category.title }}</div>

                    <!-- <div v-for="article in article_info.results" :key="article.url" class="nav-content">
                        <div v-if="article.category.id == category.id">
                            <router-link :to="{ name: 'ArticleDetail', params: { id: article.id }}" class="article-title">{{ article.title }}</router-link>
                        </div>
                    </div> -->

                    <div v-for="article in category.articles" :key="article.id" class="nav-content">
                        <router-link :to="{ name: 'ArticleDetail', params: { id: article.id }}" class="article-title">{{ article.title }}</router-link>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'LeftSideBar',
        data: function () {
            return {
                category_info: '',
            }
        },
        mounted() {
            this.get_category_list();
        },
        methods: {
            get_category_list: function(){
                let url = '/api/category';

                axios
                    .get(url)
                    .then(response => (this.category_info = response.data))
            },
            helper(){
                console.log($(event.target));
                $(event.target).siblings('.nav-content').stop().toggle(100).parent().siblings('.nav-menu').children('.nav-content').hide(500);
            }
        },
        watch: {

            $route() {

            }
        }
    };

</script>


<style scoped>
    #LeftSideBar {
        position: fixed;
        left: 0;
        top: 160px;
        bottom: 50px;
        height: auto;
        width: 260px;
        background: whitesmoke;
        text-align: center;
        font-weight: bold;
    }


    .content-left {
      width: 250px;
      height: 100%;
      background-image: linear-gradient(0deg, whitesmoke, white);
      float: left;
      overflow-x: hidden;
      overflow-y: scroll;
      scrollbar-width: none;
      scroll-behavior: auto;
    }


    .content-left a {
      text-decoration: none;
      color: #fff;
    }

    .content-left .left-title {
      height: 60px;
      width: 100%;
      font-size: 24px;
      text-align: center;
      line-height: 60px;
    }

    .content-left .seg {
      width: 100%;
      height: 2px;
      background-color: rgba(0, 0, 0, .2);
      margin: 5px 0;
    }

    .content-left .nav .nav-menu .nav-title {
      color: black;
      text-align: center;
      width: 100%;
      height: 50px;
      line-height: 50px;
      font-size: 16px;
      cursor: pointer;
    }

    .content-left .nav .nav-menu .nav-content {
      display: none;
    }

    .content-left .nav .nav-menu .nav-content a {
      color: black;
      display: block;
      width: 100%;
      height: 50px;
      text-align: center;
      line-height: 50px;
      font-size: 12px;
      background-color: rgba(0, 0, 0, .1);
    }

    .content-left .nav .nav-menu .nav-content a:hover {
      background-color: rgba(0, 0, 0, .2);
      color: brown;
    }


</style>